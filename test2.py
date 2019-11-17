import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

def dobot_jump(time,x=200,y=0,z=0):

    #执行下降到位
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, x, y, z, 0, 1)[0]
    
    #暂停time
    lastIndex = dType.SetWAITCmd(api, time, 1)[0]

    #执行上升，Z轴比原先位置高10个坐标单位
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, x, y, z+10, 0, 1)[0]

    # #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)

    #Wait for Executing Last Command 
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)

    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)

#初始化dobot
def initDobot():
    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

    # #Async Home
    # dType.SetHOMECmd(api, temp = 0, isQueued = 1)

    # #Async PTP Motion
    lastIndex = dType.SetPTPJumpParams(api, 20, 150, isQueued = 1)[0]

    # #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)

    #Wait for Executing Last Command 
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)

    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):
    #初始化
    initDobot()

    #点击屏幕
    dobot_jump(0.001, 180, 0, 0)
    dobot_jump(0.001, 180, 0, 0)
    dobot_jump(0.001, 180, 0, 0)
    dobot_jump(0.2, 180, 0, 0)
    dobot_jump(0.2, 180, 0, 0)
    dobot_jump(0.2, 180, 0, 0)
    

#Disconnect Dobot
dType.DisconnectDobot(api)
