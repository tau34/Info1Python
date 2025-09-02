f = open(input("ファイル名を入力：") + ".txt", "w", encoding = "utf-8")
f.write(input("メッセージを入力："))

f.close()
