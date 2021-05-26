from typing import List

from pydantic.main import BaseModel


# fireDataStatistics
class DoubleVector2(BaseModel):
    X: float
    Y: float


class Category(BaseModel):
    Name: str
    Points: List[DoubleVector2]


class ChartData(BaseModel):
    VSize: float
    Categories: List[Category]


class FireDataStatistics(BaseModel):
    Month: ChartData
    Week: ChartData
    Day: ChartData


class SheetData(BaseModel):
    Year: ChartData
    Month: ChartData
    Day: ChartData


# safetyScore安全评分
class SafetyScore(BaseModel):
    CompanyName: str
    PercentageOfIoT: int
    SafetyRating: int
    ImageUrl: str
    SceneName: str
    FireStatistics: int
    WarningStatistics: int
    FailureStatistics: int
    AbnormalStatistics: int
    HiddenDangerStatistics: int
    AdjacentUnits: List[str]


# realTimeAlarm实时警情
class RealTimeAlarm(BaseModel):
    CompanyName: str
    CompanyAddress: str


# giveAlarmRecord报警记录详情
class Equipment(BaseModel):
    Name: str
    Interval: float
    Hour: int
    Minute: int
    Second: int
    HistoryEvent: str


class GiveAlarmRecord(BaseModel):
    Date: str
    Details: str
    Types: str  # FIXME: should be int
    Result: str
    EquipmentList: List[Equipment]


# buildingInfo建筑信息
class BuildingInfo(BaseModel):
    CompanyName: str
    CompanyAddress: str
    ContactPerson: str
    ContactPhone: str
    FireLevel: int
    BuildingHeight: float
    BuildingArea: float
    FireLift: int
    SecurityExit: int


class AlarmInfo(BaseModel):
    DailyAlarm: int
    MonthlyAlarm: int
    PendingTasks: int


# scoreDetail评分详情
class SourceItem(BaseModel):
    Details: str
    # Score: float


class ProjectSource(BaseModel):
    Headline: str
    HeadlineScore: str
    SourceItems: List[SourceItem]


class ScoreDetail(BaseModel):
    RecommendedNames: List[str]
    WeiHuBaoYang: ProjectSource
    YunXingZhuangTai: ProjectSource
    JianChanQingKuang: ProjectSource
    JiuYuanNengLi: ProjectSource
    XiaoFangGuanLi: ProjectSource


# deviceAccess设备完好情况
class DeviceIntactInfo(BaseModel):
    DeviceType: str
    IconName: str
    IntactRate: float


class DeviceAccess(BaseModel):
    CompanyName: str
    DeviceIntactInfo: List[DeviceIntactInfo]


# rectification整改情况
class FireSystem(BaseModel):
    Categories: str
    Amount: float


class Rectification(BaseModel):
    CompanyName: str
    Numbers: int
    Rate: float
    MTTR: int
    MTBF: int
    FireSystems: List[FireSystem]


# alarmRecordsDay当日报警记录图表
class AlarmDevice(BaseModel):
    DeviceName: str
    AlarmsCount: int


class AlarmRecordsDay(BaseModel):
    CompanyName: str
    MaxAlarmsCount: float
    DeviceInfos: List[AlarmDevice]
