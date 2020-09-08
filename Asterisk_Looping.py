

for i in range(5):
    rows = ''
    for idx in range(5):
        rows = rows + '*'
    print(rows)


for i in range(5):
    rows=""
    for idx in range(i+1):
        rows = rows + '*'
    print(rows)

for i in range(5):
    rows = ""
    for idx in range(5-i):
        rows = rows + '*'
    print(rows)