from asyncio import run
from logging import info, warn
from random import randint
from typing import Any, Callable, Dict, List, Tuple, Type, Union

from pydantic.main import BaseModel
from pymongo import ASCENDING, DESCENDING

import schema
from const import PARTTYPE2NAME
from db import get_col
from real_var import *


# NOTE ok
async def get_name_by_companyID(companyID: str) -> str:
    info_col = get_col("info")
    doc = await info_col.find_one({"companyID": companyID})
    if doc is None:
        return ""
    else:
        return doc["projName"]


# NOTE ok
async def get_buildinfo_by_companyID(companyID: str) -> Dict[str, Any]:
    nm = await get_name_by_companyID(companyID)
    buildinfo_col = get_col("buildinfo")
    doc = await buildinfo_col.find_one({"companyName": nm})
    return doc


# NOTE ok
async def getFireDataStatistics(companyIDs: List[str]) -> schema.FireDataStatistics:
    query_dict: Any = {}
    query_dict["companyID"] = {}
    query_dict["companyID"]["$in"] = companyIDs
    partCodes: List[str] = []
    async for doc in get_col("info").find(query_dict):
        datas = doc["datas"]
        for d in datas:
            partCodes.append(d["partCode"])
    # info("partCodes: " + str(partCodes))

    day_res = await get_points("Day", partCodes)
    week_res = await get_points("Week", partCodes)
    month_res = await get_points("Month", partCodes)
    data = {
        "Day": {
            "Categories": [
                {"Name": "消防给水与灭火系统", "Points": day_res[fireType.WATER]},
                {"Name": "防排烟系统", "Points": day_res[fireType.SMOKE]},
                {"Name": "应急疏散系统", "Points": day_res[fireType.EVACU]},
                {"Name": "火灾探测报警系统", "Points": day_res[fireType.ALARM]},
                {"Name": "其他", "Points": day_res[fireType.OTHER]},
            ]
        },
        "Week": {
            "Categories": [
                {"Name": "消防给水与灭火系统", "Points": week_res[fireType.WATER]},
                {"Name": "防排烟系统", "Points": week_res[fireType.SMOKE]},
                {"Name": "应急疏散系统", "Points": week_res[fireType.EVACU]},
                {"Name": "火灾探测报警系统", "Points": week_res[fireType.ALARM]},
                {"Name": "其他", "Points": week_res[fireType.OTHER]},
            ]
        },
        "Month": {
            "Categories": [
                {"Name": "消防给水与灭火系统", "Points": month_res[fireType.WATER]},
                {"Name": "防排烟系统", "Points": month_res[fireType.SMOKE]},
                {"Name": "应急疏散系统", "Points": month_res[fireType.EVACU]},
                {"Name": "火灾探测报警系统", "Points": month_res[fireType.ALARM]},
                {"Name": "其他", "Points": month_res[fireType.OTHER]},
            ]
        },
    }
    return schema.FireDataStatistics(**data)  # type: ignore


# NOTE ok
async def get_number_by_companyID(companyID: str) -> List[int]:
    alarm_num = 0
    error_num = 0
    warn_num = 0
    info_col = get_col("info")
    partCode_list = []
    data_doc = await info_col.find_one({"companyID": companyID})
    if data_doc == None:
        return [0, 0, 0]
    for part in data_doc["datas"]:
        partCode_list.append(part["partCode"])

    data_col = get_col("data")
    for partCode in partCode_list:
        async for doc in data_col.find({"partCode": partCode}).sort(
            "time", DESCENDING
        ).limit(1):
            if doc["algoType"] == 100:
                alarm_num += 1
            elif doc["algoType"] == 200:
                error_num += 1
            elif doc["algoType"] == 300:
                warn_num += 1
            else:
                pass

    return [alarm_num, error_num, warn_num]


# NOTE ok
async def getSafetyScore(companyID: str) -> List[schema.SafetyScore]:
    from math import isnan

    id_list = ["CPYTEMP107747", "CPYTEMP107748", "CPYTEMP116584"]
    num_list0 = await get_number_by_companyID(id_list[0])
    num_list1 = await get_number_by_companyID(id_list[1])
    num_list2 = await get_number_by_companyID(id_list[2])
    s0 = await get_safetyScore(id_list[0])
    s1 = await get_safetyScore(id_list[1])
    s2 = await get_safetyScore(id_list[2])
    datas = [
        {
            "CompanyName": await get_name_by_companyID(id_list[0]),
            "PercentageOfIoT": await get_wellRateWhole(id_list[0]),
            "SafetyRating": s0 if not isnan(s0) else -1,
            "ImageUrl": "SHICC.png",
            "SceneName": "SHICC",
            "FireStatistics": num_list0[0],
            "WarningStatistics": num_list0[1],
            "FailureStatistics": num_list0[2],
            "AbnormalStatistics": randint(1, 10),
            "HiddenDangerStatistics": randint(1, 10),
        },
        {
            "CompanyName": await get_name_by_companyID(id_list[1]),
            "PercentageOfIoT": await get_wellRateWhole(id_list[1]),
            "SafetyRating": s1 if not isnan(s1) else -1,
            "ImageUrl": "MeiShuGuan.png",
            "SceneName": "SHICC",
            "FireStatistics": num_list1[0],
            "WarningStatistics": num_list1[1],
            "FailureStatistics": num_list1[2],
            "AbnormalStatistics": randint(1, 10),
            "HiddenDangerStatistics": randint(1, 10),
        },
        {
            "CompanyName": await get_name_by_companyID(id_list[2]),
            "PercentageOfIoT": await get_wellRateWhole(id_list[2]),
            "SafetyRating": s2 if not isnan(s2) else -1,
            "ImageUrl": "GangWuDaSha.png",
            "SceneName": "SHICC",
            "FireStatistics": num_list2[0],
            "WarningStatistics": num_list2[1],
            "FailureStatistics": num_list2[2],
            "AbnormalStatistics": randint(1, 10),
            "HiddenDangerStatistics": randint(1, 10),
        },
    ]
    return [schema.SafetyScore(**data) for data in datas]  # type: ignore


# FIXME
async def getRealTimeAlarm(companyID: str) -> List[schema.RealTimeAlarm]:
    datas = [
        {"CompanyName": "上海国际会议中心", "CompanyAddress": "上海市浦东新区滨江大道2727号"},
        {"CompanyName": "复兴馆", "CompanyAddress": "上海市浦东新区金科路1800号"},
        {
            "CompanyName": "上海浦东新区百货有限公司天丽园宾馆",
            "CompanyAddress": "上海市浦东新区川沙新镇城厢社区新川路351号",
        },
    ]
    return [schema.RealTimeAlarm(**data) for data in datas]


# FIXME
async def getGiveAlarmRecord(companyID: str) -> List[schema.GiveAlarmRecord]:
    datas = [
        {
            "Date": "12-12",
            "Details": "1楼中间办公室烟感报警器发生报警",
            "Types": "火警",
            "Result": "已归档",
            "EquipmentList": [
                {
                    "Name": "SmokeDetector1",
                    "Interval": 5.0,
                    "Hour": 11,
                    "Minute": 13,
                    "Second": 10,
                    "HistoryEvent": "三层1号烟感探测器开始报警",
                }
            ],
        },
        {
            "Date": "08-12",
            "Details": "2楼华夏厅烟感报警器发生报警",
            "Types": "故障",
            "Result": "已归档",
            "EquipmentList": [],
        },
    ]
    return [schema.GiveAlarmRecord(**data) for data in datas]  # type: ignore


# NOTE ok
async def getBuildingInfo(companyID: str) -> schema.BuildingInfo:
    buildinfo = await get_buildinfo_by_companyID(companyID)
    if not buildinfo:
        data = {
            "CompanyName": "",
            "CompanyAddress": "",
            "ContactPerson": "",
            "ContactPhone": "",
            "FireLevel": 0,
            "BuildingHeight": 0,
            "BuildingArea": 0,
            "FireLift": 0,
            "SecurityExit": 0,
        }
    else:
        data = {
            "CompanyName": buildinfo["CompanyName"],
            "CompanyAddress": buildinfo["CompanyAddress"],
            "ContactPerson": buildinfo["ContactPerson"],
            "ContactPhone": buildinfo["ContactPhone"],
            "FireLevel": buildinfo["FireLevel"],
            "BuildingHeight": buildinfo["BuildingHeight"],
            "BuildingArea": buildinfo["BuildingArea"],
            "FireLift": buildinfo["FireLift"],
            "SecurityExit": buildinfo["SecurityExit"],
        }
    return schema.BuildingInfo(**data)  # type: ignore


# NOTE ok
async def getAlarmInfo(companyID: str) -> schema.AlarmInfo:
    data = {
        "DailyAlarm": await get_fireDay(companyID),
        "MonthlyAlarm": await get_fireMonth(companyID),
        "PendingTasks": await get_riskNum(companyID),
    }
    return schema.AlarmInfo(**data)


async def get_name_and_pos_by_partCode(partCode: str) -> str:
    data_col = get_col("data")
    name = ""
    pos = ""
    async for doc in data_col.find({"partCode": partCode}).sort(
        "time", DESCENDING
    ).limit(1):
        name = PARTTYPE2NAME[int(doc["partType"])]
        pos = doc["pos"]
    return str(name) + " \t " + str(pos)


# NOTE ok! 获取了故障设备的信息
async def getScoreDetail(companyID: str) -> schema.ScoreDetail:
    ds = await get_detailScore(companyID)
    fireList = await get_firePartCode(companyID)
    errorList = await get_errorPartCode(companyID)
    errormonthList = await get_errorPartCodeMonth(companyID)

    # get all the names and positions for the device
    fireRes = []
    errorRes = []
    errormonthRes = []
    for part in fireList:
        temp = await get_name_and_pos_by_partCode(part)
        fireRes.append({"Details": temp})

    for part in errorList:
        temp = await get_name_and_pos_by_partCode(part)
        errorRes.append({"Details": temp})

    for part in errormonthList:
        temp = await get_name_and_pos_by_partCode(part)
        errormonthRes.append({"Details": temp})

    data = {
        "CompanyName": await get_name_by_companyID(companyID),
        "RecommendedNames": await get_priorRect(companyID),
        "Title": "综合得分: " + str(await get_safetyScore(companyID)),
        "WeiHuBaoYang": {
            "Headline": "设施维护保养",
            "HeadlineScore": str(ds[1]),
            "SourceItems": errormonthRes,
        },
        "YunXingZhuangTai": {"Headline": "", "HeadlineScore": "", "SourceItems": []},
        "JianChanQingKuang": {
            "Headline": "消防整改情况",
            "HeadlineScore": str(ds[2]),
            "SourceItems": [],
        },
        "JiuYuanNengLi": {"Headline": "", "HeadlineScore": "", "SourceItems": []},
        "XiaoFangGuanLi": {
            "Headline": "消防设施运行状态",
            "HeadlineScore": str(ds[0]),
            "SourceItems": fireRes + errorRes,
        },
    }
    return schema.ScoreDetail(**data)  # type: ignore


# NOTE ok
def getDeviceIntactInfo(wellRateType: List[List[float]]) -> List[Dict[str, object]]:
    res = []
    for info in wellRateType:
        nm = PARTTYPE2NAME[int(info[0])]
        temp = {"DeviceType": nm, "IconName": nm, "IntactRate": info[1] / 100}
        res.append(temp)
    return res


# NOTE ok
async def getDeviceAccess(companyID: str) -> schema.DeviceAccess:
    data = {
        "CompanyName": "",
        "DeviceIntactInfo": getDeviceIntactInfo(await get_wellRateType(companyID)),
    }
    return schema.DeviceAccess(**data)  # type: ignore


# NOTE ok
async def getRectification(companyID: str) -> schema.Rectification:
    rankList = await get_errorRankType(companyID)
    numList = await get_errorRankNum(companyID)
    firesysList = []
    for i, part in enumerate(rankList):
        firesysList.append(
            {"Categories": PARTTYPE2NAME[int(part)], "Amount": numList[i]}
        )
    data = {
        "CompanyName": await get_name_by_companyID(companyID),
        "Numbers": 0,
        "Rate": 0,
        "MTTR": await get_avgRectTime(companyID),
        "MTBF": await get_avgRepeatTime(companyID),
        "FireSystems": firesysList,
    }
    return schema.Rectification(**data)  # type: ignore


# NOTE ok
async def getAlarmRecordsDay(companyID: str) -> schema.AlarmRecordsDay:
    data = {
        "CompanyName": "",
        "MaxAlarmsCount": 0,
        "DeviceInfos": [{"DeviceName": "", "AlarmsCount": 0}],
    }
    numList = await get_fireRankNum(companyID)
    typeList = await get_fireRankType(companyID)
    infoList = []
    for i, part in enumerate(typeList):
        infoList.append(
            {"DeviceName": PARTTYPE2NAME[int(part)], "AlarmsCount": numList[i]}
        )
    data = {
        "CompanyName": await get_name_by_companyID(companyID),
        "MaxAlarmsCount": max(numList) * 1.2,
        "DeviceInfos": infoList,
    }
    return schema.AlarmRecordsDay(**data)  # type: ignore


METHODNAME_2_METHOD: Dict[str, Callable[[str], Any]] = {
    "safetyScore": getSafetyScore,
    "realTimeAlarm": getRealTimeAlarm,
    "giveAlarmRecord": getGiveAlarmRecord,
    "buildingInfo": getBuildingInfo,
    "alarmInfo": getAlarmInfo,
    "scoreDetail": getScoreDetail,
    "deviceAccess": getDeviceAccess,
    "rectification": getRectification,
    "alarmRecordsDay": getAlarmRecordsDay,
}
METHODNAME_2_METHOD_MULTI: Dict[str, Callable[[List[str]], Any]] = {
    "fireDataStatistics": getFireDataStatistics
}

# NOTE ok


async def getData(groupName: str, methodName: str) -> str:
    if methodName not in METHODNAME_2_METHOD.keys():
        raise ValueError()
    res = await METHODNAME_2_METHOD[methodName](groupName)
    if isinstance(res, BaseModel):
        return res.json(ensure_ascii=False)
    return f"[{','.join([item.json(ensure_ascii=False) for item in res])}]"


# FIXME log!
async def getDatas(groupNames: List[str], methodName: str) -> str:
    if methodName not in METHODNAME_2_METHOD_MULTI.keys():
        raise ValueError()
    res = await METHODNAME_2_METHOD_MULTI[methodName](groupNames)
    if isinstance(res, BaseModel):
        return res.json(ensure_ascii=False)
    return f"[{','.join([item.json(ensure_ascii=False) for item in res])}]"


async def test_crud() -> None:
    for k, v in METHODNAME_2_METHOD.items():
        try:
            res = await getData("CPYTEMP107748", k)
        except ValueError:
            res = "ValueError"
            # if k == "fireDataStatistics":
        print(k + ": " + res)
        print("\n")


if __name__ == "__main__":
    run(test_crud())
