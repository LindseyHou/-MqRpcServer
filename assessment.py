#  type: ignore
import os
import time
from typing import List

import numpy as np
import pandas as pd


# assessment for running status of IoT facilities
def AssessmentWithIoTData(IotData, IotDataName, B, N):
    # IotData: a matrix or table file that the data is obtained from IoT in the last 5min
    lengthOfIoTData = IotData.shape[0]
    numberOfType = B.shape[0]

    fireNumberFacility = np.zeros(numberOfType, dtype=int)  # counter for fire
    errorNumberFacility = np.zeros(numberOfType, dtype=int)  # counter for error

    tempFireFacilityNameList = []
    tempErrorFacilityNameList = []
    tempFireFacilityNumList = []
    tempErrorFacilityNumList = []

    flag = 0  # whether liandong happens
    for i in range(0, lengthOfIoTData):  # for each facility
        if IotData[i, 2] == 100:  # fire
            facilityType = IotData[i, 1]
            typeIndex = FindIndex(B, facilityType)
            # print("typeindex:",typeIndex)
            facilityName = IotDataName[i]
            # print("Facility", facilityName, "has a fire alarm.")
            # print("facilityName:",facilityName)
            counter, facility_index = FindListElement(
                tempFireFacilityNameList, facilityName
            )
            if counter == 0:
                fireNumberFacility[typeIndex] = fireNumberFacility[typeIndex] + 1
                tempFireFacilityNameList.append(facilityName)
                tempFireFacilityNumList.append(1)
            elif counter > 0:
                tempFireFacilityNumList[facility_index] = (
                    tempFireFacilityNumList[facility_index] + 1
                )

        else:  # error
            facilityType = IotData[i, 1]
            typeIndex = FindIndex(B, facilityType)
            # print("typeindex:", typeIndex)
            facilityName = IotDataName[i]
            # print("Facility", facilityName, "has an error alarm.")
            # print("facilityName:", facilityName)
            counter, facility_index = FindListElement(
                tempErrorFacilityNameList, facilityName
            )
            if counter == 0:
                errorNumberFacility[typeIndex] = errorNumberFacility[typeIndex] + 1
                tempErrorFacilityNameList.append(facilityName)
                tempErrorFacilityNumList.append(1)
            elif counter > 0:
                tempErrorFacilityNumList[facility_index] = (
                    tempErrorFacilityNumList[facility_index] + 1
                )

    # print("FireFacilityNameList:",tempFireFacilityNameList)
    # print("FireFacilityNumList:", tempFireFacilityNumList)
    # print("ErrorFacilityNameList:",tempErrorFacilityNameList)
    # print("ErrorFacilityNumList:", tempErrorFacilityNumList)
    # print(fireNumberFacility)
    # print(errorNumberFacility)

    score_IoTDataVec = np.zeros(numberOfType)
    for i in range(0, numberOfType):
        score_IoTDataVec[i] = (N[i] - errorNumberFacility[i]) / N[i] * 100
        if fireNumberFacility[i] > 0:  # if fire alarm happens
            flag = flag + 1
            score_IoTDataVec[i] = score_IoTDataVec[i] * 0.4  # if i type has fire alarm

    # print(score_IoTDataVec)
    # score_IoTData = np.dot(score_IoTDataVec,w)
    # if flag > 1: #liandong happens
    #     score_IoTData = score_IoTData*0.4
    # print("fireNumberType:",fireNumberFacility)
    # print("errorNumberType:",errorNumberFacility)
    return (
        tempFireFacilityNameList,
        tempFireFacilityNumList,
        tempErrorFacilityNameList,
        tempErrorFacilityNumList,
        fireNumberFacility,
        errorNumberFacility,
        score_IoTDataVec,
        flag,
    )


# assessment for maintenance of IoT facilities in one month
def AssessmentWithIoTMaintenance(IotMaintenanceData, IotMaintenanceDataName, B, N):

    # IotMaintenance: a matrix or table file that the data obtained from IoT in the last one month
    lengthOfIoTData = IotMaintenanceData.shape[0]
    numberOfType = B.shape[0]

    errorNumberFacilityMaintenance = np.zeros(
        numberOfType, dtype=int
    )  # counter for error

    tempErrorFacilityMaintenanceNameList = []
    tempErrorFacilityMaintenanceNumList = []
    tempNeededMaintenanceList = np.zeros(B.shape[0], dtype=int)

    flag = 0  # whether liandong happens
    for i in range(0, lengthOfIoTData):  # for each facility
        if IotMaintenanceData[i, 2] == 200:  # error

            facilityType = IotMaintenanceData[i, 1]
            typeIndex = FindIndex(B, facilityType)
            # print("typeindex:", typeIndex)
            facilityName = IotMaintenanceDataName[i]
            # print("Facility", facilityName, "has an error alarm.")
            # print("facilityName:", facilityName)
            counter, facility_index = FindListElement(
                tempErrorFacilityMaintenanceNameList, facilityName
            )
            if counter == 0:
                errorNumberFacilityMaintenance[typeIndex] = (
                    errorNumberFacilityMaintenance[typeIndex] + 1
                )
                tempErrorFacilityMaintenanceNameList.append(facilityName)
                tempErrorFacilityMaintenanceNumList.append(1)
            elif counter > 0:
                tempErrorFacilityMaintenanceNumList[facility_index] = (
                    tempErrorFacilityMaintenanceNumList[facility_index] + 1
                )

            if (
                tempErrorFacilityMaintenanceNumList[facility_index] > 2
            ):  # if a facility seng more than 2 false alarm in a month
                tempNeededMaintenanceList[typeIndex] = 1  # should be redunced the score

    # print("ErrorFacilityNumList:", tempErrorFacilityMaintenanceNumList)
    # print("tempNeededMaintenanceList",tempNeededMaintenanceList)

    score_IoTMaintenanceDataVec = np.zeros(numberOfType)
    for i in range(0, numberOfType):
        # if errorNumberFacilityMaintenance[i] > 3:
        if (
            tempNeededMaintenanceList[i] > 0
        ):  # the type of the facilities that have more than 3 false alarm in one month
            score_IoTMaintenanceDataVec[i] = (
                (N[i] - errorNumberFacilityMaintenance[i]) / N[i] * 100
            )
        else:
            score_IoTMaintenanceDataVec[i] = 100

    # print(score_IoTMaintenanceDataVec)
    # score_IoTMaintenance = np.dot(score_IoTMaintenanceDataVec, w)

    # print("error", errorNumberFacilityMaintenance)
    # weibao, facilities to be rectified, their corrsponding number for type
    return (
        score_IoTMaintenanceDataVec,
        tempErrorFacilityMaintenanceNameList,
        errorNumberFacilityMaintenance,
    )


def AssessmentForRectification(
    IotMaintenanceDataOld,
    IotMaintenanceDataOldName,
    IotMaintenanceData,
    IotMaintenanceDataName,
    B: np.ndarray,
    N: np.ndarray,
):
    # calculate the rectification score

    stillBeRectedNumber = np.zeros(B.shape[0], dtype=int)

    _, rectOld, neededRect = AssessmentWithIoTMaintenance(
        IotMaintenanceDataOld, IotMaintenanceDataOldName, B, N
    )
    # print("Last Month errorFacilityNumber of each Type:", neededRect)
    _, rect, _ = AssessmentWithIoTMaintenance(
        IotMaintenanceData, IotMaintenanceDataName, B, N
    )

    # print(len(rectOld))
    # exit()
    for i in range(0, len(rect)):
        counter, index = FindAllListElement(IotMaintenanceDataOldName, rect[i])
        size = np.where(IotMaintenanceDataOld[index, 2] == 200)[0].shape[0]
        if counter > 0 and size > 0:
            tempIndex = index[np.where(IotMaintenanceDataOld[index, 2] == 200)[0][0]]

            facilityType = IotMaintenanceDataOld[tempIndex, 1]
            typeIndex = FindIndex(B, facilityType)

            stillBeRectedNumber[typeIndex] = stillBeRectedNumber[typeIndex] + 1

    #    print("stillBeRectedNumber:",stillBeRectedNumber)#already been rectified

    numberNotRect = 0
    score_rect_memory = np.zeros(B.shape[0], dtype=int)
    for i in range(0, B.shape[0]):
        if neededRect[i] > 0:
            score_rect_memory[i] = (
                (neededRect[i] - stillBeRectedNumber[i]) / neededRect[i] * 100
            )
            if score_rect_memory[i] < 0:
                score_rect_memory[i] = 0
        else:
            score_rect_memory[i] = 0  # do not need to rectify
            numberNotRect = numberNotRect + 1

    # print("Rate of rectification of each type:", score_rect_memory)

    score_rect = np.sum(score_rect_memory) / (B.shape[0] - numberNotRect)

    return stillBeRectedNumber, score_rect


def FindIndex(apArray: np.ndarray, value):
    index = -1
    for i in range(0, apArray.shape[0]):
        temp = apArray[i]
        if temp == value:
            index = i
            break

    # print("index", index)
    return index


def FindListElement(list, value):
    counter = 0
    first_index = -1
    for i in range(0, np.array(list).shape[0]):
        temp = list[i]
        if temp == value:
            counter = counter + 1
            first_index = i
            break

    # print("index", index)
    return counter, first_index


def FindAllListElement(list, value):
    counter = 0
    first_index = []
    for i in range(0, np.array(list).shape[0]):
        temp = list[i]
        if temp == value:
            counter = counter + 1
            first_index.append(i)
    if counter == 0:
        first_index.append(-1)
    # print("index", index)
    first_index = np.array(first_index)
    return counter, first_index


def coupling(B, WorkingStatus, MaintainStatus, RectiScore, LDflag):
    # RawData Pre-Processing
    # Projection from facilities to systems
    # Fixed Parameters
    FullWeight = np.array(
        [
            0.084166515,
            0.10452645,
            0.124068351,
            0.065442647,
            0.065442647,
            0.022723141,
            0.022723141,
            0.022723141,
            0.084166515,
            0.10452645,
            0.084166515,
            0.10843483,
            0.022723141,
            0.084166515,
        ]
    )
    # weights for 13 systems+维保, a fixed vector obtained from FAHP

    HuoZai = np.array(
        [
            1,
            10,
            11,
            12,
            13,
            21,
            22,
            23,
            25,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            40,
            41,
            42,
            43,
            44,
            50,
            51,
            52,
            53,
            61,
            62,
            69,
            74,
            78,
            79,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            121,
            132,
            134,
            136,
            137,
            138,
            139,
            140,
            141,
            142,
            144,
            147,
            155,
            156,
            161,
            162,
            163,
            164,
            165,
        ]
    )
    JiShui = np.array([24, 92, 135, 258, 302, 303, 305, 351, 401, 402])
    PenShui = np.array(
        [91, 95, 96, 97, 98, 99, 106, 145, 148, 167, 256, 257, 301, 304, 352]
    )
    PaiYan = np.array([103, 104, 111, 113, 114, 115, 116, 149, 150, 451, 452, 453])
    FangHuo = np.array([102, 117, 118, 151])
    QiTi = np.array([81, 101, 129, 131, 146])
    PaoMo = np.array([105])
    GanFen = np.array([0])
    DianTi = np.array([152])
    GuangBo = np.array([130])
    ZhaoMing = np.array([128, 153, 154])
    DianYuan = np.array([133, 157, 158, 159, 160])
    DianQi = np.array([16, 17, 18])
    SysList = [
        HuoZai,
        JiShui,
        PenShui,
        PaiYan,
        FangHuo,
        QiTi,
        PaoMo,
        GanFen,
        DianTi,
        GuangBo,
        ZhaoMing,
        DianYuan,
        DianQi,
    ]
    SysNameList = [
        "火灾自动报警系统",
        "消防给水与消火栓系统",
        "自动喷水灭火系统",
        "防烟排烟系统",
        "防火门及卷帘系统",
        "气体与细水雾灭火系统",
        "泡沫灭火系统",
        "干粉灭火系统",
        "消防电梯",
        "消防应急广播",
        "消防应急照明和疏散指示",
        "消防电源",
        "电气火灾监控系统",
    ]
    tempB = set(B)
    l = len(B)
    Bsys = B.copy()
    Sysind = []
    SysScore1 = []
    SysScore2 = []
    for i in range(0, len(SysList)):
        tempSys = set(SysList[i])

        ind_dict = {k: i for i, k in enumerate(B)}
        inter = tempB.intersection(tempSys)
        indices = [ind_dict[x] for x in inter]

        if len(indices) != 0:
            Bsys[indices] = i + 1
            Sysind.append(i)
            SysScore1.append(np.mean(WorkingStatus[indices]))
            SysScore2.append(np.mean(MaintainStatus[indices]))

            l = l - len(indices)
            if l == 0:
                break

        if LDflag > 1:
            SysScore1 = [i * 0.4 for i in SysScore1]

    s = np.append(np.append(SysScore1, SysScore2), RectiScore)
    w = FullWeight[Sysind]
    weight = np.append(np.append(w, w), FullWeight[-1])
    weight = weight / np.sum(weight)
    c = []
    e = []
    for j in range(0, len(Sysind)):
        c.append(j + len(Sysind))
        e.append(j)
    if len(np.argwhere(Sysind == 1) > 0) and len(np.argwhere(Sysind == 2) > 0):
        c.append(np.argwhere(Sysind == 1))
        e.append(np.argwhere(Sysind == 2))
    if len(np.argwhere(Sysind == 5) > 0) and len(np.argwhere(Sysind == 6) > 0):
        c.append(np.argwhere(Sysind == 6))
        e.append(np.argwhere(Sysind == 5))

    # Main Coupling Calculation after obtaining s(score),weight,c(cause),e(effect)
    sc = s[c]  # find the score of all cause factors
    se = s[e]  # find the score of all effect factors
    s_correct = s.copy()  # initiate corrected score
    coup = np.zeros(len(sc))  # initiate coupling coefficients

    for i in range(0, len(sc)):
        if sc[i] < se[i]:
            coup[i] = (sc[i] * se[i] / ((sc[i] + se[i]) / 2) ** 2) ** 5
            temp = s_correct[e[i]] * (
                np.exp(-coup[i] * np.sqrt((se[i] - sc[i] + 1) * se[i] / sc[i]) / 7)
            )
            if temp < s_correct[e[i]]:
                s_correct[e[i]] = temp  # corrected score calculation

    safetyScore = np.dot(s_correct, weight)
    return Bsys, Sysind, SysNameList, s, weight, s_correct, safetyScore


def DefaultScore(newMaintain, newRecti):
    MaintainStatus = newMaintain
    RectiScore = newRecti
    return MaintainStatus, RectiScore


def MainAssessment(
    B: np.ndarray,
    N: np.ndarray,
    IoTData: np.ndarray,
    IoTDataName: List[str],
    flag: int,
    IotMaintenanceData: np.ndarray,
    IotMaintenanceDataName: List[str],
    IotMaintenanceDataOld: np.ndarray,
    IotMaintenanceDataOldName: List[str],
):
    """
    B: 建筑单位所有设备的类型编码
    N: 建筑单位每类设备的数量，
    IoTData: 5分钟内报文，从报文中提取的“No.、partType、status、time”
    IoTDataName: 5分钟内报文，为每条报文所属设备的具体名称编码
    flag: 是否要进行每月一次维保整改计算的标识，若flag=1则需计算并更新维保整改结果
    IoTMaintenanceData: 本月报文
    IoTMaintenanceDataName: 本月报文
    IoTMaintenanceDataOld: 上一个月报文
    IoTMaintenanceDataOldName: 上一个月报文"""
    # t1 = time.process_time()
    (
        tempFireFacilityNameList,
        tempFireFacilityNumList,
        tempErrorFacilityNameList,
        tempErrorFacilityNumList,
        fireNumberFacility,
        errorNumberFacility,
        score_IoTData,
        LDflag,
    ) = AssessmentWithIoTData(IoTData, IoTDataName, B, N)
    # print("Working status time:",time.process_time()-t1)

    # print("5min Fire FacilityNameList:", tempFireFacilityNameList)
    # # 5min内发出火灾报警的设备名称编码
    # print("5min Fire FacilityNumList:", tempFireFacilityNumList)
    # # 5min内发出火灾报警的每个设备，发了多少次报警
    # print("5min Error FacilityNameList:", tempErrorFacilityNameList)
    # # 5min内发出故障报警的设备名称编码
    # print("5min Error FacilityNumList:", tempErrorFacilityNumList)
    # # 5min内发出故障报警的每个设备，发了多少次报警

    # print("5min fireFacilityNumber of each Type:", fireNumberFacility)
    # # 5min内每一类设备报火警的设备数量，把单个设备归类统计
    # print("5min errorFacilityNumber of each Type:", errorNumberFacility)
    # # 5min内每一类设备报故障的设备数量，把单个设备归类统计

    # print("working status assessment:", score_IoTData)
    # # 5min内每一类设备的运行状态得分

    # if LDflag > 1:
    #     print("Liandong happens for fire")
    # else:
    #     print("Liandong does not happen for fire")
    # print()

    WorkingStatus = score_IoTData

    if flag == 1:
        # t2 = time.process_time()
        (
            score_IoTMaintenanceData,
            errorFacilities,
            numberErrorType,
        ) = AssessmentWithIoTMaintenance(
            IotMaintenanceData, IotMaintenanceDataName, B, N
        )
        # # print("Maintain time:",time.process_time()-t2)
        # print("maintenance status assessment:", score_IoTMaintenanceData)
        # # 近一个月期间每一类设备的维保得分
        # print("This Month errorFacilitiesNameList:", errorFacilities)
        # # 近一个月期间，报了故障的设备的名称
        # print("This Month errorFacilityNumber of each Type:", numberErrorType)
        # # 近一个月期间每一类设备报故障的设备数量，把单个设备归类统计，如果一个设备报了多次故障，只算一个设备

        # print()
        # t3 = time.process_time()
        stillBeRectedNumber, score_rect = AssessmentForRectification(
            IotMaintenanceDataOld,
            IotMaintenanceDataOldName,
            IotMaintenanceData,
            IotMaintenanceDataName,
            B,
            N,
        )
        # # print("Rectification time:",time.process_time()-t3)
        # print(
        #     "Intersection of This and Last Month - stillBeRectedNumber:",
        #     stillBeRectedNumber,
        # )
        # # 没有维修好的每一类设备的故障设备数量，上一个月报了故障，近一个月还在报故障的设备对比
        # print("rectification assessment:", score_rect)
        # # 维保整改率，总分100
        avgRectTime = 30 * score_rect / 100
        # print("average rectified time:", avgRectTime)
        # # 平均整改时间，30*整改率（天）

        # data=open("MaintainReport.txt",'w+')
        # print("miantenance status assessment:", score_IoTMaintenanceData,file=data)
        # print("errorFacilities:",errorFacilities,file=data)
        # print("numberErrorType:",numberErrorType,file=data)
        # print("stillBeRectedNumber:",stillBeRectedNumber,file=data)#already been rectified
        # print("rectification assessment:", score_rect,file=data)
        # print("average rectified time:", 30*score_rect/100,file=data)
        # data.close()

        MaintainStatus = score_IoTMaintenanceData
        RectiScore = score_rect
        c = np.append(score_IoTMaintenanceData, score_rect)
        c = np.append(c, numberErrorType)
        np.savetxt("score.txt", c)  # 更新维保分数整改分数这两个变量
        # txt中存储的维保整改分数是否需要张泊明那边进行入库和更新
        f = open("info.txt", "w")
        f.write(str(errorFacilities))
        f.close()
    else:
        if os.path.exists("score.txt"):  # score.txt已存入历史计算结果，直接调用
            c = np.loadtxt("score.txt")
            RectiScore = c[score_IoTData.shape[0]]
            # print("rectification assessment:", RectiScore)
            MaintainStatus = c[0 : score_IoTData.shape[0]]
            # print("miantenance status assessment:", MaintainStatus)
            numberErrorType = c[score_IoTData.shape[0] + 1 :]
            f = open("info.txt", "r")
            errorFacilities = f.readlines()
            f.close()
            avgRectTime = 30 * RectiScore / 100
        else:  # 初始化ori.txt,errorFacilities,numberErrorType
            score_IoTMaintenanceData = 100 * np.ones(score_IoTData.shape)
            MaintainStatus = score_IoTMaintenanceData
            RectiScore = 100
            c = np.append(score_IoTMaintenanceData, RectiScore)
            np.savetxt("ori.txt", c)
            errorFacilities = []
            numberErrorType = []
            avgRectTime = 0

    # t4 = time.process_time()
    [Bsys, Sysind, SysNameList, s, weight, s_correct, safetyScore] = coupling(
        B, WorkingStatus, MaintainStatus, RectiScore, LDflag
    )
    # print("Coupling time:",time.process_time()-t4)
    # print("System indices of each Type in B:", Bsys)
    priorRectScore = []
    for i in range(0, len(Sysind)):
        # print("Working Status of", SysNameList[Sysind[i]], ":", s_correct[i])
        # print(
        #     "Maintain Status of",
        #     SysNameList[Sysind[i]],
        #     ":",
        #     s_correct[i + len(Sysind)],
        # )
        priorRectScore.append(s_correct[i] + s_correct[i + len(Sysind)])

    # print("Weight vector used:", weight)
    # print("Final Safety Score:", safetyScore)

    # 安信变量合集
    wellRateWhole = sum(score_IoTMaintenanceData) / len(score_IoTMaintenanceData)
    wellRateType = []
    for i in range(0, len(B)):
        wellRateType.append([B[i], score_IoTMaintenanceData[i]])

    tempind = np.argsort(priorRectScore)
    priorRect = []
    for i in range(0, len(tempind)):
        priorRect.append(SysNameList[tempind[i]])

    detailScore = []
    detailScore.append(sum(score_IoTData) / len(score_IoTData))
    detailScore.append(wellRateWhole)
    detailScore.append(RectiScore)

    if len(numberErrorType) > 0:
        tempind = np.argsort(numberErrorType)
        errorRankType = list(B[tempind[::-1]])
        errorRankNum = list(numberErrorType[tempind[::-1]])
    else:
        errorRankType = []
        errorRankNum = []

    # wellRateWhole      	miantenance status assessment均值         	float	建筑单位的整体完好率
    # wellRateType       	score_IoTMaintenanceData                 	list	建筑单位每类设备的完好率
    # safetyScore       	safety_score                            	float	消防安全评分
    # priorRect         	priorRect                                	list	优先整改推荐，评分最低前四系统
    # firePartCode      	tempFireFacilityNameList                	list	报火警的设备编码列表，长度不定
    # errorPartCode     	tempErrorFacilityNameList               	list	报故障的设备编码列表，长度不定
    # errorPartCodeMonth	errorFacilities                         	list	报故障的设备编码列表，长度不定
    # detailScore       	score_IoTData,score_IoTMaintenanceData均值	list	运行状态+维保+整改三项细分
    # errorRankType     	errorRankType                           	list	月度报故障前五名的设备类别
    # errorRankNum      	errorRankNum                            	list	对应的报故障数目
    # avgRectTime       	avgRectTime                             	float	平均整改时长

    return (
        wellRateWhole,
        wellRateType,
        safetyScore,
        priorRect,
        tempFireFacilityNameList,
        tempErrorFacilityNameList,
        errorFacilities,
        detailScore,
        errorRankType,
        errorRankNum,
        avgRectTime,
    )


if __name__ == "__main__":

    tablename = "iot-example3.xlsx"
    IoTData = pd.read_excel(tablename, sheet_name=0, header=None)
    IoTDataTemp = pd.read_excel(tablename, sheet_name=1, header=None)
    IotMaintenanceData = pd.read_excel(tablename, sheet_name=2, header=None)
    IotMaintenanceDataTemp = pd.read_excel(tablename, sheet_name=3, header=None)
    IotMaintenanceDataOld = pd.read_excel(tablename, sheet_name=4, header=None)
    IotMaintenanceDataOldTemp = pd.read_excel(tablename, sheet_name=5, header=None)
    excel6 = pd.read_excel(tablename, sheet_name=6)
    IoTData = IoTData.values
    IoTDataTemp = IoTDataTemp.values
    IotMaintenanceData = IotMaintenanceData.values
    IotMaintenanceDataTemp = IotMaintenanceDataTemp.values
    IotMaintenanceDataOld = IotMaintenanceDataOld.values
    IotMaintenanceDataOldTemp = IotMaintenanceDataOldTemp.values

    IoTDataName = []
    for i in range(0, IoTData.shape[0]):
        IoTDataName.append(IoTDataTemp[i][0])

    IotMaintenanceDataName = []
    for i in range(0, IotMaintenanceData.shape[0]):
        IotMaintenanceDataName.append(IotMaintenanceDataTemp[i][0])

    IotMaintenanceDataOldName = []
    for i in range(0, IotMaintenanceDataOld.shape[0]):
        IotMaintenanceDataOldName.append(IotMaintenanceDataOldTemp[i][0])

    # B =   # list vector of the type of the fire facilities
    # N =   # list vector of the number of the fire facilities
    # print("Type:", B)
    # print("TypeNumber:", N)
    # print("IoTData:", IoTData)
    # print("IoTDataName:", IoTDataName)
    # print()

    flag = 1  # only current status. If flag = 1:status+maintain+rectify
    # IotMaintenanceDataOld = IoTData[0:299,:] # Data for maintain+rectify, can be empty[] if flag = 0
    # IotMaintenanceDataOldName = IoTDataName[0:299]
    b = excel6.values[:, 0]
    n = excel6.values[:, 1]
    print("b", b)
    print("n", n)
    print("IoTData", IoTData)
    print("IoTDataName", IoTDataName)
    print("flag", flag)
    print("IotMaintenanceData", IotMaintenanceData)
    print("IotMaintenanceDataName", IotMaintenanceDataName)
    print("IotMaintenanceDataOld", IotMaintenanceDataOld)
    print("IotMaintenanceDataOldName", IotMaintenanceDataOldName)
    res = MainAssessment(
        b,
        n,
        IoTData,
        IoTDataName,
        flag,
        IotMaintenanceData,
        IotMaintenanceDataName,
        IotMaintenanceDataOld,
        IotMaintenanceDataOldName,
    )
    (
        wellRateWhole,
        wellRateType,
        safetyScore,
        priorRect,
        tempFireFacilityNameList,
        tempErrorFacilityNameList,
        errorFacilities,
        detailScore,
        errorRankType,
        errorRankNum,
        avgRectTime,
    ) = res
    print("wellRateWhole", wellRateWhole)
    print("wellRateType", wellRateType)
    print("safetyScore", safetyScore)
    print("priorRect", priorRect)
    print("tempFireFacilityNameList", tempFireFacilityNameList)
    print("tempErrorFacilityNameList", tempErrorFacilityNameList)
    print("errorFacilities", errorFacilities)
    print("detailScore", detailScore)
    print("errorRankType", errorRankType)
    print("errorRankNum", errorRankNum)
    print("avgRectTime", avgRectTime)
