import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):

    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

    #Async Home
    # dType.SetHOMECmd(api, temp = 0, isQueued = 1)

    #Async PTP Motion
    dType.SetPTPJumpParams(api, 20, 150, isQueued = 1)

    x = 200
    y = 0
    z = 50
    r = 0
    print(str(x)+","+str(y)+","+str(z)+","+str(r))
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, x, y, z, r, isQueued = 1)[0]
   
    lastIndex = dType.SetWAITCmd(api, 5000, isQueued=1)[0]

    x = 200
    y = 0
    z = 50
    r = 0
    print(str(x)+","+str(y)+","+str(z)+","+str(r))
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, x, y, z, r, isQueued = 1)[0]
   
    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)

    #Wait for Executing Last Command 
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)

    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)

#Disconnect Dobot
dType.DisconnectDobot(api)
