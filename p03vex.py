question = ["英単語 dilation の意味は？", "4次方程式の解の公式の名前は？", "ハイゼンベルクの不確定性原理に関して、正しい表現はどれか？"]
options = [["拡張", "構文", "慣性"], ["カルダノの公式", "ガロアの公式", "フェラーリの公式"], ["任意の2つの物理量について成り立つ", "非可換な物理量についてのみ成り立つ", "位置と運動量についてのみ成り立つ"]]
answers = [0, 2, 1]
message = ["残念。0点でした。頑張りましょう。", "あなたの点数は1点でした。", "あなたの点数は2点でした。", "素晴らしい!3点満点です!"]
selected = [0, 0, 0]

for i in range(len(question)):
    print(question[i])
    for j in range(len(options[i])):
        print(str(j + 1) + ": " + options[i][j])
    ans = int(input("答えを選んでください: "))
    selected[i] = ans - 1

print(message[sum(selected[i] == answers[i] for i in range(len(question)))])
