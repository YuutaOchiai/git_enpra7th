import random as rm

#ランダムな3桁の数字を生成
random_number =rm.randint(100,999)
print(random_number)

#数字を回答する
ans_number = int(input("解答を入力してください : "))

#正解と不正解の出力
if random_number == ans_number:
    print("大正解!!")
else:
    print("不正解です。")

print("以下にヒントを示します。次に表示される数字が解答の中に含まれます。")

#ヒントを出力する
def random_digit():
    digit = rm.choice(str(random_number))
    return digit
random_digit()


