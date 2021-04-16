from random import randint
from typing import Any, Callable, Dict, List, Type, Union

from pydantic.main import BaseModel

import schema


def getRandPoints(Vsize: int, type: str) -> List[Dict[str, int]]:
    res: List[Dict[str, int]] = []
    if type == "Day":
        for i in range(11):
            x = 3 * i - 2
            y = randint(0, Vsize)
            res += [{"X": x, "Y": y}]
        return res
    if type == "Month":
        for i in range(1, 13):
            x = i
            y = randint(0, Vsize)
            res += [{"X": x, "Y": y}]
        return res
    if type == "Year":
        for i in range(2011, 2021):
            x = i
            y = randint(0, Vsize)
            res += [{"X": x, "Y": y}]
        return res
    return res


def getFireDataStatistics(companyID: str) -> schema.FireDataStatistics:
    Vsize_1 = 29
    Vsize_2 = 586
    Vsize_3 = 4556
    data = {
        "Day": {
            "VSize": Vsize_1,
            "Categories": [
                {"Name": "电气故障", "Points": getRandPoints(Vsize_1, "Day")},
                {"Name": "用火不慎", "Points": getRandPoints(Vsize_1, "Day")},
                {"Name": "违章作业", "Points": getRandPoints(Vsize_1, "Day")},
                {"Name": "违规吸烟", "Points": getRandPoints(Vsize_1, "Day")},
                {"Name": "其他", "Points": getRandPoints(Vsize_1, "Day")},
            ],
        },
        "Month": {
            "VSize": Vsize_2,
            "Categories": [
                {"Name": "电气故障", "Points": getRandPoints(Vsize_2, "Month")},
                {"Name": "用火不慎", "Points": getRandPoints(Vsize_2, "Month")},
                {"Name": "违章作业", "Points": getRandPoints(Vsize_2, "Month")},
                {"Name": "违规吸烟", "Points": getRandPoints(Vsize_2, "Month")},
                {"Name": "其他", "Points": getRandPoints(Vsize_2, "Month")},
            ],
        },
        "Year": {
            "VSize": 4556,
            "Categories": [
                {"Name": "电气故障", "Points": getRandPoints(Vsize_3, "Year")},
                {"Name": "用火不慎", "Points": getRandPoints(Vsize_3, "Year")},
                {"Name": "违章作业", "Points": getRandPoints(Vsize_3, "Year")},
                {"Name": "违规吸烟", "Points": getRandPoints(Vsize_3, "Year")},
                {"Name": "其他", "Points": getRandPoints(Vsize_3, "Year")},
            ],
        },
    }
    return schema.FireDataStatistics(**data)  # type: ignore


def getSafetyScore(companyID: str) -> List[schema.SafetyScore]:
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
                    },
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
    if companyID == "CPY3101120001":
        data = {"DailyAlarm": 1, "MonthlyAlarm": 20, "PendingTasks": 11}
    elif companyID == "CPY3101120002":
        data = {"DailyAlarm": 2, "MonthlyAlarm": 15, "PendingTasks": 8}
    elif companyID == "CPY3101120003":
        data = {"DailyAlarm": 5, "MonthlyAlarm": 25, "PendingTasks": 17}
    return schema.AlarmInfo(**data)


def getScoreDetail(companyID: str) -> schema.ScoreDetail:
    if companyID == "CPY310112001":
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
    elif companyID == "CPY310112002":
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
    elif companyID == "CPY310112003":
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


def getDeviceAccess(companyID: str) -> schema.DeviceAccess:
    if companyID == "CPY3101120001":
        data = {
            "CompanyName": "复兴馆",
            "DeviceIntactInfo": [
                {"DeviceType": "消防栓", "IconName": "消防栓", "IntactRate": 0.75},
                {"DeviceType": "消防水池", "IconName": "消防水池", "IntactRate": 0.85},
            ],
        }
    elif companyID == "CPY3101120002":
        data = {
            "CompanyName": "花栖馆",
            "DeviceIntactInfo": [
                {"DeviceType": "消防栓", "IconName": "消防栓", "IntactRate": 0.50},
                {"DeviceType": "消防水池", "IconName": "消防水池", "IntactRate": 0.35},
            ],
        }
    elif companyID == "CPY3101120003":
        data = {
            "CompanyName": "竹藤馆",
            "DeviceIntactInfo": [
                {"DeviceType": "消防栓", "IconName": "消防栓", "IntactRate": 0.55},
                {"DeviceType": "消防水池", "IconName": "消防水池", "IntactRate": 0.65},
            ],
        }
    return schema.DeviceAccess(**data)  # type: ignore


def getRectification(companyID: str) -> List[schema.Rectification]:
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
        {
            "CompanyName": "花栖堂",
            "Numbers": 89,
            "Rate": 31,
            "MTTR": 8,
            "MTBF": 7,
            "FireSystems": [
                {"Categories": "室外消火栓", "Amount": 33},
                {"Categories": "室内消火栓", "Amount": 20},
                {"Categories": "喷淋系统", "Amount": 11},
                {"Categories": "其他", "Amount": 20},
            ],
        },{
            "CompanyName": "竹藤馆",
            "Numbers": 117,
            "Rate": 44,
            "MTTR": 6,
            "MTBF": 5,
            "FireSystems": [
                {"Categories": "室外消火栓", "Amount": 35},
                {"Categories": "室内消火栓", "Amount": 53},
                {"Categories": "喷淋系统", "Amount": 19},
                {"Categories": "其他", "Amount": 29},
            ],
        },
        
    ]

    return [schema.Rectification(**data) for data in datas]  # type: ignore


def getAlarmRecordsDay(companyID: str) -> schema.AlarmRecordsDay:
    if companyID == "CPY3101120001":
        data = {
            "CompanyName": "复兴馆",
            "MaxAlarmsCount": 124,
            "DeviceInfos": [
                {"DeviceName": "消防栓", "AlarmsCount": 12},
                {"DeviceName": "消防水池", "AlarmsCount": 124},
            ],
        }
    if companyID == "CPY3101120002":
        data = {
            "CompanyName": "花栖堂",
            "MaxAlarmsCount": 119,
            "DeviceInfos": [
                {"DeviceName": "消防栓", "AlarmsCount": 7},
                {"DeviceName": "消防水池", "AlarmsCount": 119},
            ],
        }
    if companyID == "CPY3101120003":
        data = {
            "CompanyName": "竹藤馆",
            "MaxAlarmsCount": 113,
            "DeviceInfos": [
                {"DeviceName": "消防栓", "AlarmsCount": 18},
                {"DeviceName": "消防水池", "AlarmsCount": 113},
            ],
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
        res = getData("CPY3102300001", k)
        if k == "fireDataStatistics":
            print(res)
