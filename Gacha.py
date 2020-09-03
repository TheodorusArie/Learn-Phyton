import math
from random import random
from random import seed

def Gacha(number):
    switch={
        1:"Coba lagi ya",
        2:"Dapat kupon 5",
        3:"Dapat Kupon 15",
        4:"Dapat kupon 20",
        5:"Dapat Jackpot"
    }
    return switch.get(number,"invalid")

print(Gacha(math.ceil(random()*10/2)))