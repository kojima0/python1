ex_tax = int(input("税抜価格を入力してください：")) #税抜価格
in_tax = int(ex_tax * 1.08) #税込価格

if ex_tax >= 2000 :
    print("送料は無料です")
    total_price = in_tax
else :
    print("送料として350円かかります")
    total_price = in_tax + 350

print("送料込みの価格は",total_price,"円です。")
