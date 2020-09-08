
def XOcounter(kata):
    x=0
    o=0
    for i,a in enumerate(kata):
        if kata[i] == 'x':
            x = x+1
        else:
            o=o+1
    if x == o:
        return True
    else:
        return False

print(XOcounter('xxxooo'))