def waterState(f):
    if f <= 32:
        return "Solid"
    elif 32 < f > 212:
        return "Liquid"
    else:
        return "gas"
def isDozen (d):
    if d % 12 == 0:
        return True
    else:
        return False
def toGerman(a):
    if a == "yes":
        return "ja"
    else:
        return "nein"
def stopLight(c):
    if c == "green":
        return "go"
    elif c == "yellow":
        return "slow"
    else:
        return "stop"

