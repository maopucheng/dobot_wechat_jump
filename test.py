import math


dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
dType.SetPTPCoordinateParams(api,200,200,200,200)
dType.SetPTPJumpParams(api, 10, 200)
dType.SetPTPCommonParams(api, 100, 100)
moveX=0;moveY=0;moveZ=10;moveFlag=-1
pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]
while(True):
    moveFlag *= -1
    for i in range(5):
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z+moveZ, rHead, 1)
        moveX += 10 * moveFlag
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z+moveZ, rHead, 1)
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+moveX, y+moveY, z, rHead, 1)
