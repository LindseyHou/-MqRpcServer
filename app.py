import logging
from typing import List

from fastapi import FastAPI, Query

from crud import getData, getDatas

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
    response: str = ""
    logging.info(f" [.] getData({methodName}, {groupName})")
    if not is_valid_id(groupName):
        logging.warning("companyID not valid: " + groupName)
        response = "InValidID"
    else:
        try:
            response = await getData(groupName, methodName)
        except ValueError as e:
            logging.exception("ValueError: ")
            response = "ValueError"
    return response


@app.get("/datas")
async def endpoint_get_datas(methodName: str, groupNames: List[str] = Query([])) -> str:
    response: str = ""
    logging.info(f" [.] getDatas({methodName}, {', '.join(groupNames)})")
    try:
        for groupName in groupNames:
            if not is_valid_id(groupName):
                logging.warning("companyID not valid: " + groupName)
                raise ValueError()
    except ValueError:
        response = "InValidID"
    try:
        response = await getDatas(groupNames, methodName)
    except ValueError:
        response = "ValueError"
    return response
