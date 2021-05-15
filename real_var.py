import logging
from datetime import datetime
from typing import Any

import pymongo

from db import get_col


def getScores(companyID: str) -> Any:
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = (
        score_col.find({"companyID": companyID_int})
        .sort({"time", pymongo.DESCENDING})
        .limit(1)
    )
    logging.info("find the latest doc in time: " + doc["time"].strftime(""))
    res = {
        "wellRateWhole": doc["wellRateWhole"],
        "wellRateType": doc["wellRateType"],
        "safetyScore": doc["saftyScore"],
        "priorRect": doc["priorRect"],
        "firePartCode": doc["tempFireFacilityNameList"],
        "errorPartCode": doc["tempErrorFacilityNameList"],
        "errorPartCodeMonth": doc["errorFacilities"],
        "detailScore": doc["detailScore"],
        "errorRankType": doc["errorRankType"],
        "errorRankNum": doc["errorRankNum"],
        "avgRectTime": 0,
    }
    return res
