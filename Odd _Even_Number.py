angka1 = 1
while angka1 < 101:
    if angka1 % 2 == 0:
        print('%s - genap' % angka1)
        angka1 = angka1+3
    else:
        print('%s - ganjil' % angka1)
        angka1 = angka1+3

angka2 = 50
while angka2 < 201:
    if angka2 % 3 == 0:
        print('%s - faktor 3' % angka2)
        angka2 = angka2 + 5
    else:
        print('%s - tidak bisa dibagi 3' % angka2)
        angka2 = angka2 + 5

angka3 = 100
while angka3 < 201:
    if angka3 % 8 == 0:
        print(angka3)
        angka3 = angka3 + 1
    else:
        angka3 = angka3 + 1