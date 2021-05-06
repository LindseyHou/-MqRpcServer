from random import randint
from typing import List


def random_list(start: float, stop: float, length: int) -> List[int]:
    if length >= 0:
        length = int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(randint(start, stop))
    return random_list


waterRiskDay = random_list(1, 50, 10)
smokeRiskDay = random_list(1, 50, 10)
evacuRiskDay = random_list(1, 50, 10)
alarmRiskDay = random_list(1, 50, 10)
otherRiskDay = random_list(1, 50, 10)
riskDay = [waterRiskDay, smokeRiskDay, evacuRiskDay, alarmRiskDay, otherRiskDay]
waterRiskWeek = random_list(1, 200, 10)
smokeRiskWeek = random_list(1, 200, 10)
evacuRiskWeek = random_list(1, 200, 10)
alarmRiskWeek = random_list(1, 200, 10)
otherRiskWeek = random_list(1, 200, 10)
riskWeek = [waterRiskWeek, smokeRiskWeek, evacuRiskWeek, alarmRiskWeek, otherRiskWeek]
waterRiskMonth = random_list(1, 500, 10)
smokeRiskMonth = random_list(1, 500, 10)
evacuRiskMonth = random_list(1, 500, 10)
alarmRiskMonth = random_list(1, 500, 10)
otherRiskMonth = random_list(1, 500, 10)
riskMonth = [
    waterRiskMonth,
    smokeRiskMonth,
    evacuRiskMonth,
    alarmRiskMonth,
    otherRiskMonth,
]

wellRateWhole = 70.86  # FIXME
wellRateType = [
    [23, 100.0],
    [24, 78.6],
    [31, 100.0],
    [42, 100.0],
    [91, 62.4],
    [95, 50.0],
    [102, 100.0],
    [103, 100.0],
    [104, 100.0],
    [16, 92.3],
]
safetyScore = 45.2  # FIXME
priorRect = ["火灾自动报警系统", "自动喷水灭火系统", "防烟排烟系统", "电气火灾监控系统"]
firePartCode = ["37XF19000020400022", "37XF19000020400030"]
errorPartCode = [
    "37XF19000020400004",
    "37XF19000020400026",
    "37XF19000020400025",
    "37XF19000020400005",
    "37XF19000020400022",
    "37XF19000020400002",
    "37XF19000020400023",
    "37XF19000020400015",
    "37XF19000020400028",
]
errorPartCodeMonth = [
    "37XF19000020400004",
    "37XF19000020400026",
    "37XF19000020400025",
    "37XF19000020400005",
    "37XF19000020400022",
    "37XF19000020400002",
    "37XF19000020400023",
    "37XF19000020400015",
    "37XF19000020400028",
    "37XF19000020400009",
    "37XF19000020400007",
    "37XF19000020400031",
    "37XF19000020400027",
    "37XF19000020400034",
    "37XF19000020400020",
    "37XF19000020400012",
    "37XF19000020400003",
    "37XF19000020400013",
    "37XF19000020400001",
    "37XF19000020400035",
]
detailScore = [58.5, 95.6, 42.3]
errorRankType = [23, 24, 31, 42, 91]
errorRankNum = random_list(1, 60, 5)
avgRectTime = 15.7  # FIXME
avgRepeatTime = 3.3  # FIXME
fireDay = 23
fireMonth = 1045
riskNum = 17
fireRankType = [23, 24, 31, 42, 91, 95, 102, 103, 104, 16]
fireRankNum = random_list(1, 1000, 10)
