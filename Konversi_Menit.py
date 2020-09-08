import math

def konversiMenit(sec):
    menit=math.floor(sec/60)
    if sec%60 == 0:
        sec = '00'
    elif sec%60 <10:
        sec = '0%s' % str(sec%60)
    else:
        sec = sec%60

    return '%s:%s' % (menit,sec)

print(konversiMenit(21))
