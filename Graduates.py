def Graduates(name,score,absen):
    if score > 70 and absen < 5 and absen >=0 and score <=100:
        return "%s Lulus" % name
    elif type(score) is not int or type(name) is not str or type(absen) is not int:
        return "Inputan data salah"
    else:
        return "%s Tidak Lulus" % name

print(Graduates('bobo',1,3))
    