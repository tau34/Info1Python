f = open("fruits.csv", encoding="utf-8")
print(f.readlines()[int(input("1~10の数字を入力：")) - 1])

f.close()
