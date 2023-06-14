import random as rm

#ランダムな3桁の数字を生成
def generate_random_bumber():
    return rm.randint(100,999)

#数字を回答する
ans_number = int(input("解答を入力してください : "))

#正解と不正解の出力
def check_answer(answer, guess):
    if answer == guess:
        print("大正解!!")
        return True
    else:
        print("不正解です。")
        return False

#ゲームの中身
def game():
    answer = generate_random_bumber()
    attempts = 0

    while attempts < 3:
        guess = input("3桁の数字を回答してください : ")

        attempts += 1
        if check_answer(answer, int(guess)):
            break

    if attempts == 3:
        print("Game Over")

game()








