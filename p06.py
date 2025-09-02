f = open("hyaku.csv", encoding="utf-8")
i = input("1~100の数字を入力：")
print(i + ":" + f.readlines()[int(i)].split(",")[0])
f.close()