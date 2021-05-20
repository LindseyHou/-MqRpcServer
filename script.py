import os

companyID_ints = [
    107747,
    107748,
    116584,
    130584,
    130588,
    130589,
    130591,
    130592,
    130595,
    130596,
    135588,
    137584,
    139586,
    144588,
    145584,
    149584,
    153586,
    168585,
]

for id in companyID_ints:
    companyID = "CPYTEMP" + str(id)
    os.system("python3 real_var.py " + companyID + ">" + companyID + ".log")
    print("Finish writing " + companyID + ".log")
