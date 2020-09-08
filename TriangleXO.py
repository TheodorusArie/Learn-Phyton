rows = 5


for i in range(rows):
    tampilan =''
    for idx in range(rows):
        if idx < (rows - i -1):
            tampilan = tampilan + ' '
        else:
            tampilan = tampilan + 'x'
            if idx != rows -1:
                tampilan = tampilan + 'o'
    print(tampilan)
