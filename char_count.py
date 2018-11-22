words = [] #リスト
az = list("abcdefghijklmnopqrstuvwxyz")
char_count = dict.fromkeys(az,0) #辞書

while True:
    word = input("英単語を入力してください：")
    if word == "":
        break
    #英単語wordをリストwordsにいれる
    words.append(word)
    
words.sort() #ABC順
print("入力した英単語：" ,words)

for a in words:
    for b in a:
        char_count[b] += 1
        
#1文字以上の文字、「○が△個ありました」を表示
for c, d in char_count.items():
    if d >= 1:
        print(f"{c}が{d}個ありました")
