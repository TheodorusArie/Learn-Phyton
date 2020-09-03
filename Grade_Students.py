

def Grade_Students(name='',score=''):
    if name == '' or score == '' or type(name) is int or type(score) is str:
        return "Name dan Score harus di isi"
    elif score > 100 or score < 0:
        return "Nilai Invalid"
    elif score>=80:
        return "%s dapet grade A" % name
    elif score >= 65:
        return "%s dapet grade B" % name
    elif score >=50:
        return "%s dapet grade C" % name
    elif score >=35:
        return "%s dapet grade D" % name
    else:
        return "%s dapet grade E" % name


print(Grade_Students())
print(Grade_Students('bobo',70))
print(Grade_Students('bibi',0))
print(Grade_Students('baba',101))
print(Grade_Students('bebe',55))
print(Grade_Students(0,'asdasd'))

