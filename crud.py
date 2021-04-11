from typing import Any, Callable, Dict, List, Type, Union

from pydantic.main import BaseModel

import schema


def getFireDataStatistics() -> schema.FireDataStatistics:
    data = {
        "Day": {
            "VSize": 29,
            "Categories": [
                {
                    "Name": "电气故障",
                    "Points": [
                        {"X": 1, "Y": 22},
                        {"X": 4, "Y": 5},
                        {"X": 7, "Y": 19},
                        {"X": 10, "Y": 12},
                        {"X": 13, "Y": 15},
                        {"X": 16, "Y": 7},
                        {"X": 19, "Y": 26},
                        {"X": 22, "Y": 4},
                        {"X": 25, "Y": 16},
                        {"X": 28, "Y": 20},
                        {"X": 31, "Y": 14},
                    ],
                },
                {
                    "Name": "用火不慎",
                    "Points": [
                        {"X": 1, "Y": 19},
                        {"X": 4, "Y": 3},
                        {"X": 7, "Y": 26},
                        {"X": 10, "Y": 1},
                        {"X": 13, "Y": 11},
                        {"X": 16, "Y": 10},
                        {"X": 19, "Y": 5},
                        {"X": 22, "Y": 23},
                        {"X": 25, "Y": 13},
                        {"X": 28, "Y": 26},
                        {"X": 31, "Y": 23},
                    ],
                },
                {
                    "Name": "违章作业",
                    "Points": [
                        {"X": 1, "Y": 2},
                        {"X": 4, "Y": 23},
                        {"X": 7, "Y": 8},
                        {"X": 10, "Y": 28},
                        {"X": 13, "Y": 8},
                        {"X": 16, "Y": 2},
                        {"X": 19, "Y": 4},
                        {"X": 22, "Y": 15},
                        {"X": 25, "Y": 28},
                        {"X": 28, "Y": 21},
                        {"X": 31, "Y": 19},
                    ],
                },
                {
                    "Name": "违规吸烟",
                    "Points": [
                        {"X": 1, "Y": 14},
                        {"X": 4, "Y": 9},
                        {"X": 7, "Y": 27},
                        {"X": 10, "Y": 15},
                        {"X": 13, "Y": 10},
                        {"X": 16, "Y": 11},
                        {"X": 19, "Y": 22},
                        {"X": 22, "Y": 2},
                        {"X": 25, "Y": 5},
                        {"X": 28, "Y": 13},
                        {"X": 31, "Y": 20},
                    ],
                },
                {
                    "Name": "其他",
                    "Points": [
                        {"X": 1, "Y": 19},
                        {"X": 4, "Y": 7},
                        {"X": 7, "Y": 15},
                        {"X": 10, "Y": 17},
                        {"X": 13, "Y": 1},
                        {"X": 16, "Y": 23},
                        {"X": 19, "Y": 18},
                        {"X": 22, "Y": 18},
                        {"X": 25, "Y": 19},
                        {"X": 28, "Y": 15},
                        {"X": 31, "Y": 3},
                    ],
                },
            ],
        },
        "Month": {
            "VSize": 586,
            "Categories": [
                {
                    "Name": "电气故障",
                    "Points": [
                        {"X": 1, "Y": 160},
                        {"X": 2, "Y": 522},
                        {"X": 3, "Y": 174},
                        {"X": 4, "Y": 357},
                        {"X": 5, "Y": 567},
                        {"X": 6, "Y": 516},
                        {"X": 7, "Y": 106},
                        {"X": 8, "Y": 130},
                        {"X": 9, "Y": 456},
                        {"X": 10, "Y": 457},
                        {"X": 11, "Y": 100},
                        {"X": 12, "Y": 397},
                    ],
                },
                {
                    "Name": "用火不慎",
                    "Points": [
                        {"X": 1, "Y": 385},
                        {"X": 2, "Y": 135},
                        {"X": 3, "Y": 520},
                        {"X": 4, "Y": 102},
                        {"X": 5, "Y": 476},
                        {"X": 6, "Y": 116},
                        {"X": 7, "Y": 290},
                        {"X": 8, "Y": 464},
                        {"X": 9, "Y": 285},
                        {"X": 10, "Y": 271},
                        {"X": 11, "Y": 152},
                        {"X": 12, "Y": 110},
                    ],
                },
                {
                    "Name": "违章作业",
                    "Points": [
                        {"X": 1, "Y": 329},
                        {"X": 2, "Y": 430},
                        {"X": 3, "Y": 116},
                        {"X": 4, "Y": 246},
                        {"X": 5, "Y": 527},
                        {"X": 6, "Y": 270},
                        {"X": 7, "Y": 138},
                        {"X": 8, "Y": 166},
                        {"X": 9, "Y": 296},
                        {"X": 10, "Y": 271},
                        {"X": 11, "Y": 497},
                        {"X": 12, "Y": 406},
                    ],
                },
                {
                    "Name": "违规吸烟",
                    "Points": [
                        {"X": 1, "Y": 187},
                        {"X": 2, "Y": 512},
                        {"X": 3, "Y": 495},
                        {"X": 4, "Y": 190},
                        {"X": 5, "Y": 169},
                        {"X": 6, "Y": 280},
                        {"X": 7, "Y": 563},
                        {"X": 8, "Y": 557},
                        {"X": 9, "Y": 211},
                        {"X": 10, "Y": 542},
                        {"X": 11, "Y": 107},
                        {"X": 12, "Y": 552},
                    ],
                },
                {
                    "Name": "其他",
                    "Points": [
                        {"X": 1, "Y": 562},
                        {"X": 2, "Y": 400},
                        {"X": 3, "Y": 507},
                        {"X": 4, "Y": 404},
                        {"X": 5, "Y": 163},
                        {"X": 6, "Y": 262},
                        {"X": 7, "Y": 378},
                        {"X": 8, "Y": 474},
                        {"X": 9, "Y": 469},
                        {"X": 10, "Y": 163},
                        {"X": 11, "Y": 128},
                        {"X": 12, "Y": 237},
                    ],
                },
            ],
        },
        "Year": {
            "VSize": 4556,
            "Categories": [
                {
                    "Name": "电气故障",
                    "Points": [
                        {"X": 2011, "Y": 3536},
                        {"X": 2012, "Y": 1648},
                        {"X": 2013, "Y": 2358},
                        {"X": 2014, "Y": 3333},
                        {"X": 2015, "Y": 4068},
                        {"X": 2016, "Y": 1739},
                        {"X": 2017, "Y": 1839},
                        {"X": 2018, "Y": 1908},
                        {"X": 2019, "Y": 1833},
                        {"X": 2020, "Y": 3936},
                    ],
                },
                {
                    "Name": "用火不慎",
                    "Points": [
                        {"X": 2011, "Y": 4296},
                        {"X": 2012, "Y": 1783},
                        {"X": 2013, "Y": 1732},
                        {"X": 2014, "Y": 3154},
                        {"X": 2015, "Y": 1035},
                        {"X": 2016, "Y": 2423},
                        {"X": 2017, "Y": 1589},
                        {"X": 2018, "Y": 3820},
                        {"X": 2019, "Y": 2992},
                        {"X": 2020, "Y": 3361},
                    ],
                },
                {
                    "Name": "违章作业",
                    "Points": [
                        {"X": 2011, "Y": 1367},
                        {"X": 2012, "Y": 2239},
                        {"X": 2013, "Y": 1934},
                        {"X": 2014, "Y": 2821},
                        {"X": 2015, "Y": 2611},
                        {"X": 2016, "Y": 1021},
                        {"X": 2017, "Y": 1249},
                        {"X": 2018, "Y": 3769},
                        {"X": 2019, "Y": 1166},
                        {"X": 2020, "Y": 4092},
                    ],
                },
                {
                    "Name": "违规吸烟",
                    "Points": [
                        {"X": 2011, "Y": 1174},
                        {"X": 2012, "Y": 3807},
                        {"X": 2013, "Y": 2886},
                        {"X": 2014, "Y": 2291},
                        {"X": 2015, "Y": 2531},
                        {"X": 2016, "Y": 1674},
                        {"X": 2017, "Y": 3030},
                        {"X": 2018, "Y": 2016},
                        {"X": 2019, "Y": 2300},
                        {"X": 2020, "Y": 3501},
                    ],
                },
                {
                    "Name": "其他",
                    "Points": [
                        {"X": 2011, "Y": 3772},
                        {"X": 2012, "Y": 3403},
                        {"X": 2013, "Y": 3553},
                        {"X": 2014, "Y": 3815},
                        {"X": 2015, "Y": 4244},
                        {"X": 2016, "Y": 2443},
                        {"X": 2017, "Y": 4291},
                        {"X": 2018, "Y": 3589},
                        {"X": 2019, "Y": 3001},
                        {"X": 2020, "Y": 2315},
                    ],
                },
            ],
        },
    }
    return schema.FireDataStatistics(**data)  # type: ignore


def getSafetyScore() -> List[schema.SafetyScore]:
    datas = [
        {
            "CompanyName": "上海国际会议中心",
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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
            "PercentageOfIoT": 85,
            "SafetyRating": 83,
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


def getRealTimeAlarm() -> List[schema.RealTimeAlarm]:
    datas = [
        {"CompanyName": "上海国际会议中心", "CompanyAddress": "上海市浦东新区滨江大道2727号"},
        {"CompanyName": "复兴馆", "CompanyAddress": "上海市浦东新区金科路1800号"},
        {
            "CompanyName": "上海浦东新区百货有限公司天丽园宾馆",
            "CompanyAddress": "上海市浦东新区川沙新镇城厢社区新川路351号",
        },
    ]
    return [schema.RealTimeAlarm(**data) for data in datas]


def getGiveAlarmRecord() -> List[schema.GiveAlarmRecord]:
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
    return [schema.GiveAlarmRecord(**data) for data in datas]  # type: ignore


def getBuildingInfo() -> schema.BuildingInfo:
    data = {
        "CompanyName": "上海国际会议中心",
        "CompanyAddress": "上海市浦东新区滨江大道2727号",
        "ContactPerson": "刘总:18510550819",
        "ContactPhone": "1",
        "FireLevel": "1",
        "BuildingHeight": "1",
        "BuildingArea": "1",
        "FireLift": "1",
        "SecurityExit": "1",
    }
    return schema.BuildingInfo(**data)  # type: ignore


def getAlarmInfo() -> schema.AlarmInfo:
    data = {"DailyAlarm": 1, "MonthlyAlarm": 20, "PendingTasks": 11}
    return schema.AlarmInfo(**data)


def getScoreDetail() -> schema.ScoreDetail:
    data = {
        "RecommendedNames": [
            "火灾探测器完好率",
            "火灾报警次数",
            "定期进行消防安全教育和培训",
            "疏散通道、安全出口和消防通道保持畅通",
        ],
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
    return schema.ScoreDetail(**data)  # type: ignore


def getDeviceAccess() -> schema.DeviceAccess:
    data = {
        "CompanyName": "上海国际会议中心",
        "DeviceIntactInfo": [
            {"DeviceType": "消防栓", "IconName": "消防栓", "IntactRate": 0.75},
            {"DeviceType": "消防水池", "IconName": "消防水池", "IntactRate": 0.85},
        ],
    }
    return schema.DeviceAccess(**data)  # type: ignore


def getRectification() -> List[schema.Rectification]:
    datas = [
        {
            "CompanyName": "上海国际会议中心",
            "Numbers": 117,
            "Rate": 62,
            "MTTR": 7,
            "MTBF": 9,
            "FireSystems": [
                {"Categories": "室外消火栓", "Amount": 28},
                {"Categories": "室内消火栓", "Amount": 32},
                {"Categories": "喷淋系统", "Amount": 27},
                {"Categories": "其他", "Amount": 13},
            ],
        },
        {
            "CompanyName": "复兴馆",
            "Numbers": 117,
            "Rate": 62,
            "MTTR": 7,
            "MTBF": 9,
            "FireSystems": [
                {"Categories": "室外消火栓", "Amount": 28},
                {"Categories": "室内消火栓", "Amount": 32},
                {"Categories": "喷淋系统", "Amount": 27},
                {"Categories": "其他", "Amount": 13},
            ],
        },
    ]

    return [schema.Rectification(**data) for data in datas]  # type: ignore


def getAlarmRecordsDay() -> schema.AlarmRecordsDay:
    data = {
        "CompanyName": "上海国际会议中心",
        "MaxAlarmsCount": 124,
        "DeviceInfos": [
            {"DeviceName": "消防栓", "AlarmsCount": 12},
            {"DeviceName": "消防水池", "AlarmsCount": 124},
        ],
    }
    return schema.AlarmRecordsDay(**data)  # type: ignore


METHODNAME_2_METHOD: Dict[str, Callable[[], Any]] = {
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
def get_data(methodName: str) -> str:
    if methodName not in METHODNAME_2_METHOD.keys():
        raise ValueError()
    res = METHODNAME_2_METHOD[methodName]()
    if isinstance(res, BaseModel):
        return res.json(ensure_ascii=False)
    return f"[{','.join([item.json(ensure_ascii=False) for item in res])}]"


if __name__ == "__main__":
    for k, v in METHODNAME_2_METHOD.items():
        res = get_data(k)
        print(res)
