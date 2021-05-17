import logging
import sys
from datetime import datetime
from enum import IntEnum
from typing import Any, Dict, List

import pymongo
from dateutil.relativedelta import relativedelta

from db import get_col
from partType_classify import ALARM_LIST, EVACU_LIST, OTHER_LIST, SMOKE_LIST, WATER_LIST


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
def get_points(timeslot: str) -> List[List[Dict[str, int]]]:
    res: List[List[Dict[str, int]]] = []
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
        query_dict["time"]["$lte"] = end_date
        query_dict["time"]["$gte"] = start_date
        count: List[
            int
        ] = []  # count[fireType.WATER] refers to the water隐患 in a single time interval
        for doc in get_col("data").find(query_dict):
            algo: int = doc["algoType"]
            partType: int = doc["partType"]
            count = [0, 0, 0, 0, 0]
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
def get_wellRateWhole(companyID: str) -> int:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


def get_wellRateType(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


def get_safetyScore(companyID: str) -> float:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


def get_priorRect(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


def get_firePartCode(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc["tempFireFacilityNameList"]


def get_errorPartCode(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc["tempErrorFacilityNameList"]


def get_errorPartCodeMonth(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc["errorFacilities"]


def get_detailScore(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


def get_errorRankType(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


def get_errorRankNum(companyID: str) -> List[Any]:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


def get_avgRectTime(companyID: str) -> int:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    var_name = sys._getframe().f_code.co_name[4:]
    logging.info(
        "Latest "
        + var_name
        + ", companyID: "
        + companyID
        + " time: "
        + doc["time"].strftime("")
    )
    return doc[var_name]


# from excel 27-33
def get_avgRepeatTime(companyID: str) -> int:
    pass


def get_fireDay() -> Any:
    pass


def get_fireMonth() -> Any:
    pass


def get_riskNum() -> Any:
    pass


def get_fireRankType() -> Any:
    pass


def get_fireRankNum() -> Any:
    pass


def get_riskList() -> Any:
    pass
