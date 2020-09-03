


def Cafe_Visitation(name='',age=0,money=0):
    if type(name) is not str or type(age) is not int or type(money) is not int or name == '':
        return "Kamu tidak boleh masuk"
    elif age<17:
        if money >= 50000:
            return "Anda bisa pesan minum, sisa uang anda %s" % (money-50000)
        else:
            return "Uang tidak cukup, anda harus pulang"
    elif age>17:
        if money >=300000:
            return "Anda bisa pesan minum, sisa uang anda %s" % (money-300000)
        else:
            return "Uang tidak cukup, anda harus pulang"
    else:
        return "Ada kesalahan pada kode"
print(Cafe_Visitation("obo",2,51000))
print(Cafe_Visitation("obo",2,5000))
print(Cafe_Visitation("",2,51000))
print(Cafe_Visitation("obo",21,51000))
print(Cafe_Visitation("obo",22,3001000))