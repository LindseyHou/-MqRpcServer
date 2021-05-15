from db import get_col
import pymongo
from datetime import datetime
import logging

def getScores(companyID: str):
    companyID_int: int = int(companyID[7:])
    score_col = get_col("score")
    doc = score_col.find({"companyID": companyID_int}).sort({"time",pymongo.DESCENDING}).limit(1)
    logging.info("find the latest doc in time: " + doc["time"].strftime(""))
    res = {
        "wellRateWhole":doc["wellRateWhole"],
        "safetyScore": doc["saftyScore"],
        "priorRect": doc["priorRect"],
        "tempFireFacilityNameList": doc["tempFireFacilityNameList"],
        "tempErrorFacilityNameList": doc["tempErrorFacilityNameList"],
        "errorFacilities": doc["errorFacilities"],
        "detailScore": doc["detailScore"],
        "errorRankType":doc["errorRankType"],
        "errorRankNum": doc["errorRankNum"],
        "avgRectTime":0 
    }
    return res

