f = open("fruits.csv", encoding="utf-8")
l = f.readlines()
a = ["","",""]
print("1~10の数字を3つ入力")
a[0] = l[int(input("1つめ：")) - 1]
a[1] = l[int(input("2つめ：")) - 1]
a[2] = l[int(input("3つめ：")) - 1]
print(a)

f.close()
