kata = 'Javascript'

new_string =''
for i,a in enumerate(kata):
    new_string = new_string + kata[(len(kata)-1)-i]
print(new_string)