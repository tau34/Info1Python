question = ["英単語 dilation の意味は？", "4次方程式の解の公式の名前は？", "ハイゼンベルクの不確定性原理に関して、正しい表現はどれか？"]
options = [["拡張", "構文", "慣性"], ["カルダノの公式", "ガロアの公式", "フェラーリの公式"], ["任意の2つの物理量について成り立つ", "非可換な物理量についてのみ成り立つ", "位置と運動量についてのみ成り立つ"]]
answers = [0, 2, 1]
message = ["残念。0点でした。頑張りましょう。", "あなたの点数は1点でした。", "あなたの点数は2点でした。", "素晴らしい!3点満点です!"]
selected = [0, 0, 0]

print(question[0])
print("1: " + options[0][0])
print("2: " + options[0][1])
print("3: " + options[0][2])
ans = int(input("答えを選んでください: "))
selected[0] = ans - 1

print(question[1])
print("1: " + options[1][0])
print("2: " + options[1][1])
print("3: " + options[1][2])
ans = int(input("答えを選んでください: "))
selected[1] = ans - 1

print(question[2])
print("1: " + options[2][0])
print("2: " + options[2][1])
print("3: " + options[2][2])
ans = int(input("答えを選んでください: "))
selected[2] = ans - 1

print(message[sum(selected[i] == answers[i] for i in range(len(question)))])
