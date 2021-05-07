from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from db import get_col


async def get_partCodes_by_companyID(companyID: int) -> List[str]:
    info_col = get_col("info")
    doc = await info_col.find_one({"projID": companyID})
    if doc is None:
        return []
    return [item["partCode"] for item in doc["datas"]]


async def get_data(
    companyID: int, time_gte: datetime, time_lte: Optional[datetime] = None
) -> Tuple[np.ndarray, List[str]]:
    data_col = get_col("data")
    partCodes = await get_partCodes_by_companyID(companyID)
    res = []
    arr = np.zeros((0, 4), dtype=np.int64)
    index = 1
    find_dict: Dict[str, Any] = {
        "partCode": {"$in": partCodes},
        "algoType": {"$ne": 0},
        "time": {"$gte": time_gte},
    }
    if time_lte is not None:
        find_dict["time"]["$lte"] = time_lte
    async for document in data_col.find(find_dict):
        res.append(document["partCode"])
        arr = np.append(
            arr,
            [
                [
                    index,
                    document["partType"],
                    300 - document["algoType"] * 100,
                    int(datetime.timestamp(document["time"])),
                ]
            ],
            axis=0,
        )
        index += 1
    return arr, res


async def get_bn(companyID: int) -> Tuple[List[str], List[int]]:
    info_col = get_col("info")
    doc = await info_col.find_one({"projID": companyID})
    if doc is None:
        return [], []
    bnDict: Dict[str, int] = {}
    for item in doc["datas"]:
        if bnDict.get(item["partType"]) is None:
            bnDict[item["partType"]] = 0
        bnDict[item["partType"]] += 1
    b = []
    n = []
    for k, v in bnDict.items():
        b.append(k)
        n.append(v)
    return b, n


import asyncio

if __name__ == "__main__":
    b, n = asyncio.run(get_bn(107747))
    print("b", b)
    print("n", n)
    # data, dataName = asyncio.run(get_data(107747, datetime.now() - timedelta(days=30)))
    # print("data", data)
    # print("dataName", dataName)
