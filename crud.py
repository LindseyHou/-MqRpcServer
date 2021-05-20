from typing import Any, Callable, Dict, List, Type, Union

from pydantic.main import BaseModel

import schema
from anxin_var import *
from real_var import *
from const import PARTTYPE2NAME
from asyncio import run


def getFireDataStatistics(companyID: str) -> schema.FireDataStatistics:
    Vsize_1 = 50
    Vsize_2 = 200
    Vsize_3 = 500
    day_res = run(get_points("Day"))
    week_res = run(get_points("Week"))
    month_res = run(get_points("Month"))
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


def getSafetyScore(companyID: str) -> List[schema.SafetyScore]:
    datas = [
        {
            "CompanyName": "上海国际会议中心",
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),  # FIXME: why float???
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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
            "PercentageOfIoT": get_wellRateWhole(companyID),
            "SafetyRating": get_safetyScore(companyID),
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


def getRealTimeAlarm(companyID: str) -> List[schema.RealTimeAlarm]:
    datas = [
        {"CompanyName": "上海国际会议中心", "CompanyAddress": "上海市浦东新区滨江大道2727号"},
        {"CompanyName": "复兴馆", "CompanyAddress": "上海市浦东新区金科路1800号"},
        {
            "CompanyName": "上海浦东新区百货有限公司天丽园宾馆",
            "CompanyAddress": "上海市浦东新区川沙新镇城厢社区新川路351号",
        },
    ]
    return [schema.RealTimeAlarm(**data) for data in datas]


def getGiveAlarmRecord(companyID: str) -> List[schema.GiveAlarmRecord]:
    datas = []
    if companyID == "CPY3101120001":
        datas = [
            {
                "Date": "09-18",
                "Details": "3楼中间办公室烟感报警器发生报警",
                "Types": "火警",
                "Result": "已归档",
                "EquipmentList": [
                    {
                        "Name": "SmokeDetector1",
                        "Interval": 5.0,
                        "Hour": 11,
                        "Minute": 15,
                        "Second": 0,
                        "HistoryEvent": "三层1号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector2",
                        "Interval": 5.0,
                        "Hour": 11,
                        "Minute": 15,
                        "Second": 15,
                        "HistoryEvent": "三层2号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector3",
                        "Interval": 10.0,
                        "Hour": 11,
                        "Minute": 15,
                        "Second": 20,
                        "HistoryEvent": "三层3号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector4",
                        "Interval": 20.0,
                        "Hour": 11,
                        "Minute": 16,
                        "Second": 0,
                        "HistoryEvent": "四层4号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector5",
                        "Interval": 5.0,
                        "Hour": 11,
                        "Minute": 17,
                        "Second": 0,
                        "HistoryEvent": "七层5号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector6",
                        "Interval": 0.0,
                        "Hour": 11,
                        "Minute": 17,
                        "Second": 5,
                        "HistoryEvent": "七层6号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector7",
                        "Interval": 0.0,
                        "Hour": 11,
                        "Minute": 17,
                        "Second": 5,
                        "HistoryEvent": "七层7号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector8",
                        "Interval": 0.0,
                        "Hour": 11,
                        "Minute": 17,
                        "Second": 5,
                        "HistoryEvent": "七层8号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector9",
                        "Interval": 0.0,
                        "Hour": 11,
                        "Minute": 17,
                        "Second": 5,
                        "HistoryEvent": "七层9号烟感探测器开始报警",
                    },
                ],
            },
            {
                "Date": "09-05",
                "Details": "1楼华夏厅烟感报警器发生报警",
                "Types": "故障",
                "Result": "已归档",
                "EquipmentList": [],
            },
        ]
    elif companyID == "CPY3101120002":
        datas = [
            {
                "Date": "05-20",
                "Details": "5楼中间办公室烟感报警器发生报警",
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
                    },
                    {
                        "Name": "SmokeDetector8",
                        "Interval": 0.0,
                        "Hour": 11,
                        "Minute": 13,
                        "Second": 10,
                        "HistoryEvent": "七层8号烟感探测器开始报警",
                    },
                    {
                        "Name": "SmokeDetector9",
                        "Interval": 0.0,
                        "Hour": 11,
                        "Minute": 13,
                        "Second": 10,
                        "HistoryEvent": "七层9号烟感探测器开始报警",
                    },
                ],
            },
            {
                "Date": "09-05",
                "Details": "2楼华夏厅烟感报警器发生报警",
                "Types": "故障",
                "Result": "已归档",
                "EquipmentList": [],
            },
        ]
    elif companyID == "CPY3101120003":
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


def getBuildingInfo(companyID: str) -> schema.BuildingInfo:
    data = {
        "CompanyName": "None",
        "CompanyAddress": "None",
        "ContactPerson": "None",
        "ContactPhone": "0",
        "FireLevel": "0",
        "BuildingHeight": "0",
        "BuildingArea": "0",
        "FireLift": "0",
        "SecurityExit": "0",
    }
    if companyID == "CPY3101120001":
        data = {
            "CompanyName": "复兴馆",
            "CompanyAddress": "上海市浦东新区滨江大道2727号",
            "ContactPerson": "刘总:18510550819",
            "ContactPhone": "1",
            "FireLevel": "1",
            "BuildingHeight": "1",
            "BuildingArea": "1",
            "FireLift": "1",
            "SecurityExit": "1",
        }

    elif companyID == "CPY3101120002":
        data = {
            "CompanyName": "花栖馆",
            "CompanyAddress": "上海市浦东新区滨江大道2727号",
            "ContactPerson": "赵总:17813554839",
            "ContactPhone": "1",
            "FireLevel": "1",
            "BuildingHeight": "1",
            "BuildingArea": "1",
            "FireLift": "1",
            "SecurityExit": "1",
        }

    elif companyID == "CPY3101120003":
        data = {
            "CompanyName": "竹藤馆",
            "CompanyAddress": "上海市浦东新区滨江大道2727号",
            "ContactPerson": "王总:13211558321",
            "ContactPhone": "1",
            "FireLevel": "1",
            "BuildingHeight": "1",
            "BuildingArea": "1",
            "FireLift": "1",
            "SecurityExit": "1",
        }

    return schema.BuildingInfo(**data)  # type: ignore


def getAlarmInfo(companyID: str) -> schema.AlarmInfo:
    data = {"DailyAlarm": 0, "MonthlyAlarm": 0, "PendingTasks": 0}
    if companyID == "CPY3101120001":
        data = {
            "DailyAlarm": run(get_fireDay(companyID)),
            "MonthlyAlarm": run(get_fireMonth(companyID)),
            "PendingTasks": run(get_riskNum(companyID)),
        }
    elif companyID == "CPY3101120002":
        data = {
            "DailyAlarm":   run(get_fireDay(companyID)),
            "MonthlyAlarm": run(get_fireMonth(companyID)),
            "PendingTasks": run(get_riskNum(companyID)),
        }
    elif companyID == "CPY3101120003":
        data = {
            "DailyAlarm": run(get_fireDay(companyID)),
            "MonthlyAlarm": run(get_fireMonth(companyID)),
            "PendingTasks": run(get_riskNum(companyID)),
        }
    return schema.AlarmInfo(**data)


def getScoreDetail(companyID: str) -> schema.ScoreDetail:
    data = {
        "RecommendedNames": [],
        "WeiHuBaoYang": {
            "Headline": "",
            "HeadlineScore": "",
            "SourceItems": [{"Details": ""}],
        },
        "YunXingZhuangTai": {
            "Headline": "",
            "HeadlineScore": "",
            "SourceItems": [{"Details": ""}],
        },
        "JianChanQingKuang": {
            "Headline": "",
            "HeadlineScore": "",
            "SourceItems": [{"Details": ""}],
        },
        "JiuYuanNengLi": {
            "Headline": "",
            "HeadlineScore": "",
            "SourceItems": [{"Details": ""}]
        },
        "XiaoFangGuanLi": {
            "Headline": "",
            "HeadlineScore": "",
            "SourceItems": [{"Details": ""}],
        },
    }
    if companyID == "CPY3101120001":
        data = {
            "RecommendedNames": run(get_priorRect(companyID)),
            "WeiHuBaoYang": {
                "Headline": "设施维护保养",
                "SourceItems": [
                    {"Details": "维修时间", "Score": -4.0},
                    {"Details": "维修成功率", "Score": -4.0},
                ],
            },
            "YunXingZhuangTai": {
                "Headline": "消防设施运行状态",
                "SourceItems": [
                    {"Details": "火灾探测器完好率", "Score": -10.0},
                    {"Details": "火灾报警次数", "Score": -8.0},
                    {"Details": "控制器完好率", "Score": -4.0},
                    {"Details": "应急照明备用电源供电时间", "Score": -4.0},
                    {"Details": "机械排烟系统的排烟量", "Score": -4.0},
                ],
            },
            "JianChanQingKuang": {
                "Headline": "消防监督检查情况",
                "SourceItems": [
                    {"Details": "疏散通道、安全出口和消防通道保持畅通", "Score": -6.0},
                    {"Details": "电气线路定期检查", "Score": -3.0},
                    {"Details": "燃气管路定期检测", "Score": -3.0},
                    {"Details": "消防设施符合技术标准", "Score": -3.0},
                ],
            },
            "JiuYuanNengLi": {
                "Headline": "灭火救援能力",
                "SourceItems": [
                    {"Details": "员工参加初起火灾扑救操作培训", "Score": -5.0},
                    {"Details": "定期组织疏散演练", "Score": -5.0},
                    {"Details": "建立应急疏散预案", "Score": -2.0},
                    {"Details": "对员工进行消防器材使用培训", "Score": -1.0},
                ],
            },
            "XiaoFangGuanLi": {
                "Headline": "消防管理",
                "SourceItems": [
                    {"Details": "定期进行消防安全教育和培训", "Score": -6.0},
                    {"Details": "建立防火档案", "Score": -5.0},
                    {"Details": "建立消防设施操作与故障记录", "Score": -4.0},
                    {"Details": "定期开展防火检查与巡查", "Score": -4.0},
                ],
            },
        }
    elif companyID == "CPY3101120002":
        data = {
            "RecommendedNames": run(get_priorRect(companyID)),
            "WeiHuBaoYang": {
                "Headline": "设施维护保养",
                "SourceItems": [
                    {"Details": "维修时间", "Score": -2.0},
                    {"Details": "维修成功率", "Score": -2.0},
                ],
            },
            "YunXingZhuangTai": {
                "Headline": "消防设施运行状态",
                "SourceItems": [
                    {"Details": "火灾探测器完好率", "Score": -8.0},
                    {"Details": "火灾报警次数", "Score": -8.0},
                    {"Details": "控制器完好率", "Score": -2.0},
                    {"Details": "应急照明备用电源供电时间", "Score": -1.0},
                    {"Details": "机械排烟系统的排烟量", "Score": -1.0},
                ],
            },
            "JianChanQingKuang": {
                "Headline": "消防监督检查情况",
                "SourceItems": [
                    {"Details": "疏散通道、安全出口和消防通道保持畅通", "Score": -2.0},
                    {"Details": "电气线路定期检查", "Score": -5.0},
                    {"Details": "燃气管路定期检测", "Score": -5.0},
                    {"Details": "消防设施符合技术标准", "Score": -6.0},
                ],
            },
            "JiuYuanNengLi": {
                "Headline": "灭火救援能力",
                "SourceItems": [
                    {"Details": "员工参加初起火灾扑救操作培训", "Score": -7.0},
                    {"Details": "定期组织疏散演练", "Score": -8.0},
                    {"Details": "建立应急疏散预案", "Score": -8.0},
                    {"Details": "对员工进行消防器材使用培训", "Score": -2.0},
                ],
            },
            "XiaoFangGuanLi": {
                "Headline": "消防管理",
                "SourceItems": [
                    {"Details": "定期进行消防安全教育和培训", "Score": -10.0},
                    {"Details": "建立防火档案", "Score": -3.0},
                    {"Details": "建立消防设施操作与故障记录", "Score": -2.0},
                    {"Details": "定期开展防火检查与巡查", "Score": -2.0},
                ],
            },
        }
    elif companyID == "CPY3101120003":
        data = {
            "RecommendedNames": run(get_priorRect(companyID)),
            "WeiHuBaoYang": {
                "Headline": "设施维护保养",
                "SourceItems": [
                    {"Details": "维修时间", "Score": -8.0},
                    {"Details": "维修成功率", "Score": -8.0},
                ],
            },
            "YunXingZhuangTai": {
                "Headline": "消防设施运行状态",
                "SourceItems": [
                    {"Details": "火灾探测器完好率", "Score": -2.0},
                    {"Details": "火灾报警次数", "Score": -2.0},
                    {"Details": "控制器完好率", "Score": -5.0},
                    {"Details": "应急照明备用电源供电时间", "Score": -3.0},
                    {"Details": "机械排烟系统的排烟量", "Score": -3.0},
                ],
            },
            "JianChanQingKuang": {
                "Headline": "消防监督检查情况",
                "SourceItems": [
                    {"Details": "疏散通道、安全出口和消防通道保持畅通", "Score": -4.0},
                    {"Details": "电气线路定期检查", "Score": -10.0},
                    {"Details": "燃气管路定期检测", "Score": -10.0},
                    {"Details": "消防设施符合技术标准", "Score": -2.0},
                ],
            },
            "JiuYuanNengLi": {
                "Headline": "灭火救援能力",
                "SourceItems": [
                    {"Details": "员工参加初起火灾扑救操作培训", "Score": -2.0},
                    {"Details": "定期组织疏散演练", "Score": -2.0},
                    {"Details": "建立应急疏散预案", "Score": -2.0},
                    {"Details": "对员工进行消防器材使用培训", "Score": -4.0},
                ],
            },
            "XiaoFangGuanLi": {
                "Headline": "消防管理",
                "SourceItems": [
                    {"Details": "定期进行消防安全教育和培训", "Score": -7.0},
                    {"Details": "建立防火档案", "Score": -6.0},
                    {"Details": "建立消防设施操作与故障记录", "Score": -3.0},
                    {"Details": "定期开展防火检查与巡查", "Score": -3.0},
                ],
            },
        }
    return schema.ScoreDetail(**data)  # type: ignore


def getDeviceIntactInfo(wellRateType: List[List[float]]) -> List[Dict[str, object]]:
    res = []
    for info in wellRateType:
        nm = PARTTYPE2NAME[int(info[0])]
        temp = {"DeviceType": nm, "IconName": nm, "IntactRate": info[1] / 100}
        res.append(temp)
    return res


def getDeviceAccess(companyID: str) -> schema.DeviceAccess:
    data = {"CompanyName": "",
            "DeviceIntactInfo": getDeviceIntactInfo(run(get_wellRateType(companyID)))}
    if companyID == "CPY3101120001":
        data = {
            "CompanyName": "复兴馆",
            "DeviceIntactInfo": getDeviceIntactInfo(run(get_wellRateType(companyID))),
        }
    elif companyID == "CPY3101120002":
        data = {
            "CompanyName": "花栖馆",
            "DeviceIntactInfo": getDeviceIntactInfo(run(get_wellRateType(companyID))),
        }
    elif companyID == "CPY3101120003":
        data = {
            "CompanyName": "竹藤馆",
            "DeviceIntactInfo": getDeviceIntactInfo(run(get_wellRateType(companyID))),
        }
    return schema.DeviceAccess(**data)  # type: ignore


def getRectification(companyID: str) -> schema.Rectification:
    data = {
        "CompanyName": "",
        "Numbers": 0,
        "Rate": 0,
        "MTTR": 0,
        "MTBF": 0,
        "FireSystems": [
            {"Categories": "室外消火栓", "Amount": 0},
            {"Categories": "室内消火栓", "Amount": 0},
            {"Categories": "喷淋系统", "Amount": 0},
            {"Categories": "其他", "Amount": 0},
        ],
    }
    if companyID == "CPY3101120001":
        data = {
            "CompanyName": "复兴馆",
            "Numbers": 117,
            "Rate": 62,
            "MTTR": get_avgRectTime(companyID),
            "MTBF": get_avgRepeatTime(companyID),
            "FireSystems": [
                {"Categories": "室外消火栓", "Amount": 28},
                {"Categories": "室内消火栓", "Amount": 32},
                {"Categories": "喷淋系统", "Amount": 27},
                {"Categories": "其他", "Amount": 13},
                {"Categories": "其他1", "Amount": 13},
            ],
        }
    elif companyID == "CPY3101120002":
        data = {
            "CompanyName": "花栖堂",
            "Numbers": 89,
            "Rate": 31,
            "MTTR": get_avgRectTime(companyID),
            "MTBF": get_avgRepeatTime(companyID),
            "FireSystems": [
                {"Categories": "室外消火栓", "Amount": 33},
                {"Categories": "室内消火栓", "Amount": 20},
                {"Categories": "喷淋系统", "Amount": 11},
                {"Categories": "其他", "Amount": 20},
                {"Categories": "其他1", "Amount": 20},
            ],
        }
    elif companyID == "CPY3101120003":
        data = {
            "CompanyName": "竹藤馆",
            "Numbers": 117,
            "Rate": 44,
            "MTTR": get_avgRectTime(companyID),
            "MTBF": get_avgRepeatTime(companyID),
            "FireSystems": [
                {"Categories": "室外消火栓", "Amount": 35},
                {"Categories": "室内消火栓", "Amount": 53},
                {"Categories": "喷淋系统", "Amount": 19},
                {"Categories": "其他", "Amount": 29},
                {"Categories": "其他1", "Amount": 29},
            ],
        }
    return schema.Rectification(**data)  # type: ignore


def getAlarmRecordsDay(companyID: str) -> schema.AlarmRecordsDay:
    data = {
        "CompanyName": "",
        "MaxAlarmsCount": 0,
        "DeviceInfos": [{"DeviceName": "", "AlarmsCount": 0}],
    }
    numList = run(get_fireRankNum(companyID))
    if companyID == "CPY3101120001":
        infoList = []
        for i in range(10):
            infoList.append(
                {
                    "DeviceName": PARTTYPE2NAME[run(get_fireRankType(companyID))[i]],
                    "AlarmsCount": numList[i],
                }
            )
        data = {
            "CompanyName": "复兴馆",
            "MaxAlarmsCount": max(numList),
            "DeviceInfos": infoList,
        }
    if companyID == "CPY3101120002":
        infoList = []
        for i in range(10):
            infoList.append(
                {
                    "DeviceName": PARTTYPE2NAME[run(get_fireRankType(companyID))[i]],
                    "AlarmsCount": numList[i],
                }
            )
        data = {
            "CompanyName": "复兴馆",
            "MaxAlarmsCount": max(numList),
            "DeviceInfos": infoList,
        }
    if companyID == "CPY3101120003":
        infoList = []
        for i in range(10):
            infoList.append(
                {
                    "DeviceName": PARTTYPE2NAME[run(get_fireRankType(companyID))[i]],
                    "AlarmsCount": numList[i],
                }
            )
        data = {
            "CompanyName": "复兴馆",
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


# TODO: get REAL data from DB
def getData(groupName: str, methodName: str) -> str:
    if methodName not in METHODNAME_2_METHOD.keys():
        raise ValueError()
    res = METHODNAME_2_METHOD[methodName](groupName)
    if isinstance(res, BaseModel):
        return res.json(ensure_ascii=False)
    return f"[{','.join([item.json(ensure_ascii=False) for item in res])}]"


if __name__ == "__main__":
    for k, v in METHODNAME_2_METHOD.items():
        res = getData("", k)
        if k == "fireDataStatistics":
            print(res)
