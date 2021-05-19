import asyncio as asy
import heapq
import logging
import sys
from datetime import datetime
from enum import IntEnum
from typing import Any, Dict, List

import pymongo
from dateutil.relativedelta import relativedelta

from db import get_col
from partType_classify import (
    ALARM_LIST,
    EVACU_LIST,
    OTHER_LIST,
    PARTTYPE2NAME,
    SMOKE_LIST,
    WATER_LIST,
)


class fireType(IntEnum):
    "隐患Type"
    WATER = 0
    SMOKE = 1
    EVACU = 2
    ALARM = 3
    OTHER = 4


def get_fireType(partType: int) -> fireType:
    if partType in WATER_LIST:
        return fireType.WATER
    elif partType in SMOKE_LIST:
        return fireType.SMOKE
    elif partType in EVACU_LIST:
        return fireType.EVACU
    elif partType in ALARM_LIST:
        return fireType.ALARM
    else:
        return fireType.OTHER


# from excel 1-15
async def get_points(timeslot: str) -> List[List[Dict[str, int]]]:
    res: List[List[Dict[str, int]]] = [[] for i in range(5)]
    now = datetime.now()
    interval: relativedelta = relativedelta(days=0)
    if timeslot == "Day":
        interval = relativedelta(days=1)
    elif timeslot == "Week":
        interval = relativedelta(weeks=1)
    elif timeslot == "Month":
        interval = relativedelta(months=1)
    start_date = now - 10 * interval
    query_dict: Any = {}
    for i in range(10):
        end_date = start_date + interval
        query_dict["time"] = {}
        query_dict["time"]["$lte"] = end_date
        query_dict["time"]["$gte"] = start_date
        count: List[int] = [
            0,
            0,
            0,
            0,
            0,
        ]  # count[fireType.WATER] refers to the water隐患 in a single time interval
        async for doc in get_col("data").find(query_dict):
            algo: int = doc["algoType"]
            partType: int = doc["partType"]
            if algo == 100 or algo == 200 or algo == 300:
                _fireType = get_fireType(partType=partType)
                count[_fireType] += 1
        res[fireType.WATER].append({"X": i + 1, "Y": count[fireType.WATER]})
        res[fireType.SMOKE].append({"X": i + 1, "Y": count[fireType.SMOKE]})
        res[fireType.EVACU].append({"X": i + 1, "Y": count[fireType.EVACU]})
        res[fireType.ALARM].append({"X": i + 1, "Y": count[fireType.ALARM]})
        res[fireType.OTHER].append({"X": i + 1, "Y": count[fireType.OTHER]})
        start_date += interval

    return res


# from excel 16-26. Basically directly obtained from collection "score"
# Do not modify these functions' names!
async def get_wellRateWhole(companyID: str) -> int:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    query_dict: Any = {}
    query_dict["time"] = {}

    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


async def get_wellRateType(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


async def get_safetyScore(companyID: str) -> float:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


async def get_priorRect(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


async def get_firePartCode(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc["tempFireFacilityNameList"]


async def get_errorPartCode(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc["tempErrorFacilityNameList"]


async def get_errorPartCodeMonth(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc["errorFacilities"]


async def get_detailScore(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


async def get_errorRankType(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


async def get_errorRankNum(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


async def get_avgRectTime(companyID: str) -> int:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    docs = (
        score_col.find({"companyID": companyID_int})
        .sort("time", pymongo.DESCENDING)
        .limit(1)
    )
    doc = {}
    async for d in docs:
        doc = d
    var_name = sys._getframe().f_code.co_name[4:]
    logging.debug(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


# from excel 27-33
async def get_avgRepeatTime(companyID: str) -> float:
    "27"
    companyID_int: int = int(companyID[7:])
    datas = (await get_col("info").find_one({"projID": companyID_int}))["datas"]
    partCodes = []
    for data in datas:
        partCodes.append(data["partCode"])
    now = datetime.now()
    start_time = now - relativedelta(days=30)
    query_dict: Any = {}
    query_dict["time"] = {}
    query_dict["time"]["$lte"] = now
    query_dict["time"]["$gte"] = start_time
    query_dict["algoType"] = {"$in": [100, 200, 300]}
    query_dict["partType"] = {"$in": partCodes}
    documents = get_col("data").find(query_dict)
    count: Dict[int, Dict[str, int]] = {}
    async for doc in documents:
        partType: int = doc["partType"]
        partCode: str = doc["partCode"]
        if partType not in count.keys():
            count[partType] = {}
        else:
            if partCode not in count[partType].keys():
                count[partType][partCode] = 1
            else:
                count[partType][partCode] += 1
    sum: float = 0
    for pT in count.keys():
        codeNum: int = len(count[pT])
        dataNum: int = 0
        for n in count[pT].values():
            dataNum += n
        repT: float = 30 / (dataNum / codeNum)
        sum += repT
    if len(count.keys()) == 0:
        return 0
    avgRepT: float = sum / len(count.keys())
    return avgRepT


async def get_fireDay(companyID: str) -> int:
    "28"
    companyID_int: int = int(companyID[7:])
    datas = (await get_col("info").find_one({"projID": companyID_int}))["datas"]
    partCodes = []
    for data in datas:
        partCodes.append(data["partCode"])
    now = datetime.now()
    start_time = now - relativedelta(days=1)
    query_dict: Any = {}
    query_dict["time"] = {}
    query_dict["time"]["$lte"] = now
    query_dict["time"]["$gte"] = start_time
    query_dict["algoType"] = 100
    query_dict["partType"] = {"$in": partCodes}
    documents = get_col("data").find(query_dict)
    res = 0
    async for d in documents:
        res += 1
    logging.debug(
        "[fireDay]From "
        + start_time.strftime("%Y-%m-%d")
        + " to "
        + now.strftime("%Y-%m-%d")
        + ": "
        + str(res)
    )
    return res


async def get_fireMonth(companyID: str) -> int:
    "29"
    companyID_int: int = int(companyID[7:])
    datas = (await get_col("info").find_one({"projID": companyID_int}))["datas"]
    partCodes = []
    for data in datas:
        partCodes.append(data["partCode"])
    now = datetime.now()
    start_time = now - relativedelta(months=1)
    query_dict: Any = {}
    query_dict["time"] = {}
    query_dict["time"]["$lte"] = now
    query_dict["time"]["$gte"] = start_time
    query_dict["algoType"] = 100
    query_dict["partType"] = {"$in": partCodes}
    documents = get_col("data").find(query_dict)
    res = 0
    async for d in documents:
        res += 1
    logging.debug(
        "[fireMonth]From "
        + start_time.strftime("%Y-%m-%d")
        + " to "
        + now.strftime("%Y-%m-%d")
        + ": "
        + str(res)
    )
    return res


async def get_riskNum(companyID: str) -> int:
    "30"
    companyID_int: int = int(companyID[7:])
    datas = (await get_col("info").find_one({"projID": companyID_int}))["datas"]
    partCodes = []
    for data in datas:
        partCodes.append(data["partCode"])
    now = datetime.now()
    start_time = now - relativedelta(weeks=1)
    query_dict: Any = {}
    query_dict["time"] = {}
    query_dict["time"]["$lte"] = now
    query_dict["time"]["$gte"] = start_time
    query_dict["algoType"] = {"$in": [100, 200, 300]}
    query_dict["partType"] = {"$in": partCodes}
    documents = get_col("data").find(query_dict)
    res = 0
    async for d in documents:
        res += 1
    logging.debug(
        "[riskNum]From "
        + start_time.strftime("%Y-%m-%d")
        + " to "
        + now.strftime("%Y-%m-%d")
        + ": "
        + str(res)
    )
    return res


async def get_fireRankType(companyID: str) -> List[int]:
    "31"
    companyID_int: int = int(companyID[7:])
    datas = (await get_col("info").find_one({"projID": companyID_int}))["datas"]
    partCodes = []
    for data in datas:
        partCodes.append(data["partCode"])

    count: Dict[int, int] = {}

    now = datetime.now()
    start_time = now - relativedelta(weeks=1)
    query_dict: Any = {}
    query_dict["time"] = {}
    query_dict["time"]["$lte"] = now
    query_dict["time"]["$gte"] = start_time
    query_dict["algoType"] = 100
    query_dict["partType"] = {"$in": partCodes}
    documents = get_col("data").find(query_dict)
    async for doc in documents:
        partType = doc["partType"]
        if partType in count.keys():
            count[partType] += 1
        else:
            count[partType] = 1
    max_10 = heapq.nlargest(10, count.items(), key=lambda x: x[1])
    res: List[int] = []
    for m in max_10:
        res.append(m[0])
    return res


async def get_fireRankNum(companyID: str) -> List[int]:
    "32"
    companyID_int: int = int(companyID[7:])
    datas = (await get_col("info").find_one({"projID": companyID_int}))["datas"]
    partCodes = []
    for data in datas:
        partCodes.append(data["partCode"])

    count: Dict[int, int] = {}

    now = datetime.now()
    start_time = now - relativedelta(weeks=1)
    query_dict: Any = {}
    query_dict["time"] = {}
    query_dict["time"]["$lte"] = now
    query_dict["time"]["$gte"] = start_time
    query_dict["algoType"] = 100
    query_dict["partType"] = {"$in": partCodes}
    documents = get_col("data").find(query_dict)
    async for doc in documents:
        partType = doc["partType"]
        if partType in count.keys():
            count[partType] += 1
        else:
            count[partType] = 1
    max_10 = heapq.nlargest(10, count.items(), key=lambda x: x[1])
    res: List[int] = []
    for m in max_10:
        res.append(m[1])
    return res


async def get_riskList(companyID: str) -> List[str]:
    "33"
    companyID_int: int = int(companyID[7:])
    datas = (await get_col("info").find_one({"projID": companyID_int}))["datas"]
    partCodes = []
    for data in datas:
        partCodes.append(data["partCode"])
    now = datetime.now()
    start_time = now - relativedelta(weeks=1)
    query_dict: Any = {}
    query_dict["time"] = {}
    query_dict["time"]["$lte"] = now
    query_dict["time"]["$gte"] = start_time
    query_dict["algoType"] = {"$in": [100, 200, 300]}
    query_dict["partType"] = {"$in": partCodes}
    documents = get_col("data").find(query_dict)
    res: List[str] = []
    ALGO2NAME: Dict[int, str] = {0: "正常", 100: "火警", 200: "故障", 300: "预警"}
    async for doc in documents:
        sentence: str = ""
        sentence = (
            PARTTYPE2NAME[doc["partType"]]
            + ", "
            + doc["pos"]
            + ", "
            + ALGO2NAME[doc["algoType"]]
        )
        res.append(sentence)

    return res


async def main() -> None:
    logging.basicConfig(level=logging.INFO, filename="real_var.log", filemode="w")
    day_res = await get_points("Day")
    week_res = await get_points("Week")
    month_res = await get_points("Month")
    companyID = sys.argv[1]

    wellRateWhole = await get_wellRateWhole(companyID)
    wellRateType = await get_wellRateType(companyID)
    safetyScore = await get_safetyScore(companyID)
    priorRect = await get_priorRect(companyID)
    firePartCode = await get_firePartCode(companyID)
    errorPartCode = await get_errorPartCode(companyID)
    errorPartCodeMonth = await get_errorPartCodeMonth(companyID)
    detailScore = await get_detailScore(companyID)
    errorRankType = await get_errorRankType(companyID)
    errorRankNum = await get_errorRankNum(companyID)
    avgRectTime = await get_avgRectTime(companyID)
    avgRepeatTime = await get_avgRepeatTime(companyID)
    fireDay = await get_fireDay(companyID)
    fireMonth = await get_fireMonth(companyID)
    riskNum = await get_riskNum(companyID)
    fireRankType = await get_fireRankType(companyID)
    fireRankNum = await get_fireRankNum(companyID)
    riskList = await get_riskList(companyID)

    logging.info("1.waterRiskDay: " + day_res[fireType.WATER].__str__())
    logging.info("2.smokeRiskDay: " + day_res[fireType.SMOKE].__str__())
    logging.info("3.evacuRiskDay: " + day_res[fireType.EVACU].__str__())
    logging.info("4.alarmRiskDay: " + day_res[fireType.ALARM].__str__())
    logging.info("5.otherRiskDay: " + day_res[fireType.OTHER].__str__())

    logging.info("6.waterRiskWeek: " + week_res[fireType.WATER].__str__())
    logging.info("7.smokeRiskWeek: " + week_res[fireType.SMOKE].__str__())
    logging.info("8.evacuRiskWeek: " + week_res[fireType.EVACU].__str__())
    logging.info("9.alarmRiskWeek: " + week_res[fireType.ALARM].__str__())
    logging.info("10.otherRiskWeek: " + week_res[fireType.OTHER].__str__())

    logging.info("11.waterRiskMonth: " + month_res[fireType.WATER].__str__())
    logging.info("12.smokeRiskMonth: " + month_res[fireType.SMOKE].__str__())
    logging.info("13.evacuRiskMonth: " + month_res[fireType.EVACU].__str__())
    logging.info("14.alarmRiskMonth: " + month_res[fireType.ALARM].__str__())
    logging.info("15.otherRiskMonth: " + month_res[fireType.OTHER].__str__())

    logging.info("16.wellRateWhole: " + wellRateWhole.__str__())
    logging.info("17.wellRateType: " + wellRateType.__str__())
    logging.info("18.safetyScore: " + safetyScore.__str__())
    logging.info("19.priorRect: " + priorRect.__str__())
    logging.info("20.firePartCode: " + firePartCode.__str__())
    logging.info("21.errorPartCode: " + errorPartCode.__str__())
    logging.info("22.errorPartCodeMonth: " + errorPartCodeMonth.__str__())
    logging.info("23.detailScore: " + detailScore.__str__())
    logging.info("24.errorRankType: " + errorRankType.__str__())
    logging.info("25.errorRankNum: " + errorRankNum.__str__())
    logging.info("26.avgRectTime: " + avgRectTime.__str__())
    logging.info("27.avgRepeatTime: " + avgRepeatTime.__str__())
    logging.info("28.fireDay: " + fireDay.__str__())
    logging.info("29.fireMonth: " + fireMonth.__str__())
    logging.info("30.riskNum: " + riskNum.__str__())
    logging.info("31.fireRankType: " + fireRankType.__str__())
    logging.info("32.fireRankNum: " + fireRankNum.__str__())
    logging.info("33.riskList: " + riskList.__str__())


if __name__ == "__main__":
    asy.run(main())
