f = open(input("ファイル名を入力：") + ".txt", "a", encoding = "utf-8")
f.write(input("メッセージを入力："))
f.close()