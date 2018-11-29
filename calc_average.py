total_points = 0
total_people = 0


while True:
    point = int(input("点数を入力してください："))

    if point == -1:
        break

    total_points = total_points + point
    total_people += 1

average = total_points / total_people
print(str(total_people),"人のテストの平均点は",str(average),"点です")
print("test")
