# 九九のリストを作成する
list_x = [[(x * y) for y in range(1,10)] for x in range(1,10)]

# 九九の表を表示する
#for v in range(1, 10):
#    for h in range(1, 10):
#        print(f"{(v * h):3d}", end="")
#    
#    print("")

for i in list_x:
    for h in i:
        print(f"{(h):3d}", end="")
        
    print("")
