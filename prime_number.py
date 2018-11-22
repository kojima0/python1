#エラトステネスのふるい
#素数を表示する
for i in range(1,100):
    if i == 1:
        continue
    if i != 2 and i % 2 == 0:
        continue
    if i != 3 and i % 3 == 0:
        continue
    if i != 5 and i % 5 == 0:
        continue
    if i != 7 and i % 7 == 0:
        continue
    print(i)
