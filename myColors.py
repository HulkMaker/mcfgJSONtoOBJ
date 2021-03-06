def getEarthColor():
    i=1
    kd=[0.26, 0.53, 0.19]
    ks=[0.02, 0.05, 0.02]
    ka=[0.04, 0.04, 0.04]
    tf=[0.0, 0.0, 0.0]
    ns=.001
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni

def getRoadColor():
    i=1
    kd=[0.46, 0.53, 0.49]
    ks=[0.2, 0.2, 0.2]
    ka=[0.4, 0.4, 0.4]
    tf=[1.0, 1.0, 1.0]
    ns=20
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni
def getCityTowerColor():
    '''
    city walls color
    '''
    i=1
    kd=[0.46, 0.3, 0.6]
    ks=[0.1, 0.1, 0.1]
    ka=[0.09, 0.9, 0.09]
    tf=[1.0, 1.0, 1.0]
    ns=0.01
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni

def getCityWallColor():
    '''
    city walls color
    '''
    i=1
    kd=[0.46, 0.463, 0.469]
    ks=[0.03, 0.01, 0.02]
    ka=[0.02, 0.01, 0.01]
    tf=[1.0, 1.0, 1.0]
    ns=10
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni
def getWallbColor():
    '''
    building walls color
    '''
    i=1
    kd=[0.46, 0.03, 0.09]
    ks=[0.3, 0.01, 0.02]
    ka=[0.2, 0.01, 0.01]
    tf=[1.0, 1.0, 1.0]
    ns=30
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni
def getRoofColor():
    '''
    Building roof color
    '''
    i=1
    kd=[0.33, 0.35, 0.38]
    ks=[0.23, 0.25, 0.28]
    ka=[1, 1, 1]
    tf=[1.0, 1.0, 1.0]
    ns=40
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni
def getFieldColor():
    i=1
    kd=[0.96, 0.77, 0.60]
    ks=[0.3, 0.15, 0.05]
    ka=[0, 0, 0]
    tf=[1.0, 1.0, 1.0]
    ns=0
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni
def getSquareColor():
    i=4
    kd=[0.45, 0.30, 0.25]
    ks=[0.93, 0.85, 0.68]
    ka=[1, 0.8, 0.6]
    tf=[1.0, 1.0, 1.0]
    ns=10
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni
def getPrismsColor():
    i=4
    kd=[0.5, 0.5, 0.5]
    ks=[0.93, 0.85, 0.68]
    ka=[1, 0.8, 0.6]
    tf=[1.0, 1.0, 1.0]
    ns=40
    ni=1.0
    return i, kd, ks, ka, tf, ns, ni
def getRiversColor():
    i=4
    kd=[0.2, 0.2, 0.5]
    ks=[0.2, 0.05, 0.68]
    ka=[0, 0, 0]
    tf=[1.0, 1.0, 1.0]
    ns=60
    ni=1.3
    return i, kd, ks, ka, tf, ns, ni
def getPlanksColor():
    i=2
    kd=[0.2, 0.2, 0.5]
    ks=[0.2, 0.05, 0.68]
    ka=[0, 0, 0]
    tf=[1.0, 1.0, 1.0]
    ns=60
    ni=1.3
    return i, kd, ks, ka, tf, ns, ni