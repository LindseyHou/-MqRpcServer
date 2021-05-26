from asyncio import run
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
async def getFireDataStatistics(companyID: str) -> schema.FireDataStatistics:
    Vsize_1 = 50
    Vsize_2 = 200
    Vsize_3 = 500
    day_res = await get_points("Day")
    week_res = await get_points("Week")
    month_res = await get_points("Month")
    data = {
        "Day": {
            "VSize": Vsize_1,
            "Categories": [
                {"Name": "电气故障", "Points": day_res[fireType.WATER]},
                {"Name": "用火不慎", "Points": day_res[fireType.SMOKE]},
                {"Name": "违章作业", "Points": day_res[fireType.EVACU]},
                {"Name": "违规吸烟", "Points": day_res[fireType.ALARM]},
                {"Name": "其他", "Points": day_res[fireType.OTHER]},
            ],
        },
        "Week": {
            "VSize": Vsize_2,
            "Categories": [
                {"Name": "电气故障", "Points": week_res[fireType.WATER]},
                {"Name": "用火不慎", "Points": week_res[fireType.SMOKE]},
                {"Name": "违章作业", "Points": week_res[fireType.EVACU]},
                {"Name": "违规吸烟", "Points": week_res[fireType.ALARM]},
                {"Name": "其他", "Points": week_res[fireType.OTHER]},
            ],
        },
        "Month": {
            "VSize": Vsize_3,
            "Categories": [
                {"Name": "电气故障", "Points": month_res[fireType.WATER]},
                {"Name": "用火不慎", "Points": month_res[fireType.SMOKE]},
                {"Name": "违章作业", "Points": month_res[fireType.EVACU]},
                {"Name": "违规吸烟", "Points": month_res[fireType.ALARM]},
                {"Name": "其他", "Points": month_res[fireType.OTHER]},
            ],
        },
    }
    return schema.FireDataStatistics(**data)  # type: ignore


# FIXME 编造毗邻单位；毗邻单位分数怎么调用？
async def getSafetyScore(companyID: str) -> List[schema.SafetyScore]:
    datas = [
        {
            "CompanyName": "上海国际会议中心",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "SHICC.png",
            "SceneName": "SHICC",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["港务大厦", "浦东美术馆", "浦东海关大楼", "万向大厦"],
        },
        {
            "CompanyName": "浦东美术馆",
            "PercentageOfIoT": await get_wellRateWhole(companyID),  # fake
            "SafetyRating": await get_safetyScore(companyID),  # fake
            "ImageUrl": "MeiShuGuan.png",
            "SceneName": "SHICC",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["港务大厦", "上海国际会议中心", "浦东海关大楼", "万向大厦"],
        },
        {
            "CompanyName": "港务大厦",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "GangWuDaSha.png",
            "SceneName": "SHICC",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["上海国际会议中心", "浦东美术馆", "浦东海关大楼", "港务大厦"],
        },
        {
            "CompanyName": "浦东海关大楼",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "HaiGuanDaLou.png",
            "SceneName": "SHICC",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["港务大厦", "上海国际会议中心", "浦东美术馆", "万向大厦"],
        },
        {
            "CompanyName": "正大广场",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "ZhengDaGuangChang.png",
            "SceneName": "SHICC",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["港务大厦", "上海国际会议中心", "浦东海关大楼", "万向大厦"],
        },
        {
            "CompanyName": "万向大厦",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "WanXiangDaSha.png",
            "SceneName": "SHICC",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["港务大厦", "上海国际会议中心", "浦东海关大楼", "正大广场"],
        },
        {
            "CompanyName": "复兴馆",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "FuXingGuan.png",
            "SceneName": "FuXingGuan",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["花栖堂", "世纪馆", "花艺馆", "竹藤馆"],
        },
        {
            "CompanyName": "花栖堂",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "HuaQiTang.png",
            "SceneName": "HuaQiTang",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["复兴馆", "世纪馆", "花艺馆", "竹藤馆"],
        },
        {
            "CompanyName": "世纪馆",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "ShiJiGuan.png",
            "SceneName": "",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["复兴馆", "花栖堂", "花艺馆", "竹藤馆"],
        },
        {
            "CompanyName": "花艺馆",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "HuaYiGuan.png",
            "SceneName": "",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["港务大厦", "上海国际会议中心", "浦东美术馆", "万向大厦"],
        },
        {
            "CompanyName": "竹藤馆",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "ZhuTengGuan.png",
            "SceneName": "",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["百花馆", "花艺馆", "世纪馆", "花栖堂"],
        },
        {
            "CompanyName": "百花馆",
            "PercentageOfIoT": await get_wellRateWhole(companyID),
            "SafetyRating": await get_safetyScore(companyID),
            "ImageUrl": "BaiHuaGuan.png",
            "SceneName": "",
            "FireStatistics": 6,
            "WarningStatistics": 8,
            "FailureStatistics": 3,
            "AbnormalStatistics": 7,
            "HiddenDangerStatistics": 10,
            "AdjacentUnits": ["竹藤馆", "花艺馆", "世纪馆", "花栖堂"],
        },
    ]
    return [schema.SafetyScore(**data) for data in datas]  # type: ignore


# FIXME 和安信沟通如何编造这个假数据
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


# FIXME 和安信沟通如何调用这个假数据
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
        "RecommendedNames": await get_priorRect(companyID),
        "WeiHuBaoYang": {
            "Headline": "设施维护保养",
            "HeadlineScore": str(ds[1]),
            "SourceItems": errormonthRes,
        },
        "YunXingZhuangTai": {"Headline": "", "HeanlineScore": "", "SourceItems": []},
        "JianChanQingKuang": {
            "Headline": "消防整改情况",
            "HeadlineScore": str(ds[2]),
            "SourceItems": [],
        },
        "JiuYuanNengLi": {"Headline": "", "HeanlineScore": "", "SourceItems": []},
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
        "MaxAlarmsCount": max(numList),
        "DeviceInfos": infoList,
    }
    return schema.AlarmRecordsDay(**data)  # type: ignore


METHODNAME_2_METHOD: Dict[str, Callable[[str], Any]] = {
    "fireDataStatistics": getFireDataStatistics,
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


# NOTE ok
async def getData(groupName: str, methodName: str) -> str:
    if methodName not in METHODNAME_2_METHOD.keys():
        raise ValueError()
    res = await METHODNAME_2_METHOD[methodName](groupName)
    if isinstance(res, BaseModel):
        return res.json(ensure_ascii=False)
    return f"[{','.join([item.json(ensure_ascii=False) for item in res])}]"


# def run(coroutine: Any) -> Any:
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value
async def fun() -> None:
    for k, v in METHODNAME_2_METHOD.items():
        try:
            res = await getData("CPYTEMP107747", k)
        except ValueError:
            res = "ValueError"
            # if k == "fireDataStatistics":
            print("k: " + res)


if __name__ == "__main__":
    run(fun())
