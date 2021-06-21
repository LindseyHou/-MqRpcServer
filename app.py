import json
import logging
from typing import List

from fastapi import FastAPI, Query
from fastapi_utils.tasks import repeat_every
from uvicorn.config import logger

from crud import getData, getDatas, getDeviceAccess
from mq import send_mq

logging.basicConfig(
    handlers=[logging.FileHandler("mq.log"), logging.StreamHandler()],
    format="%(asctime)s %(levelname)-8s: %(filename)s %(funcName)s %(lineno)s %(message)s",
    datefmt="%m-%d %H:%M:%S",
    level=logging.INFO,
)

app = FastAPI()


def is_upper_char(s: str) -> bool:
    for c in s:
        if c < "A" or c > "Z":
            return False
    return True


def is_numbers(s: str) -> bool:
    for c in s:
        if c < "0" or c > "9":
            return False
    return True


def is_valid_id(companyID: str) -> bool:
    if companyID == "":
        return True
    if len(companyID) <= 7:
        return False
    prefix = companyID[0:7]
    leftover = companyID[7:]
    return is_upper_char(prefix) and is_numbers(leftover)


@app.get("/data")
async def endpoint_get_data(methodName: str, groupName: str = "") -> str:
    logging.info(f" [.] getData({methodName}, {groupName})")
    if not is_valid_id(groupName):
        logging.warning("companyID not valid: " + groupName)
        return "InValidID"
    else:
        try:
            res = await getData(groupName, methodName)
            if isinstance(res, str):
                return json.loads(res)
            return res
        except ValueError as e:
            logging.exception("ValueError: ")
            return "ValueError"


@app.get("/datas")
async def endpoint_get_datas(methodName: str, groupNames: List[str] = Query([])) -> str:
    logging.info(f" [.] getDatas({methodName}, {', '.join(groupNames)})")
    try:
        for groupName in groupNames:
            if not is_valid_id(groupName):
                logging.warning("companyID not valid: " + groupName)
                raise ValueError()
    except ValueError:
        return "InValidID"
    try:
        res = await getDatas(groupNames, methodName)
        if isinstance(res, str):
            return json.loads(res)
        return res
    except ValueError:
        return "ValueError"


@app.on_event("startup")
@repeat_every(seconds=5 * 60, logger=logger)  # 5 minutes
async def device_access_task() -> None:
    for companyID in ["CPYTEMP107747", "CPYTEMP107748", "CPYTEMP116584"]:
        res = (await getDeviceAccess(companyID)).json(ensure_ascii=False)
        logger.info(f"data pushed to {companyID}: {res}")
        send_mq(companyID, "deviceAccess", res)
