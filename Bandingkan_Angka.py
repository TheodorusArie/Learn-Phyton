
def bandingAngka(a,b):
    if b > a:
        return False
    elif a > b:
        return True
    else:
        return -1

print(bandingAngka(3,2))