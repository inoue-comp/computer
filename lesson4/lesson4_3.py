import random
secret =random.randint(1,10)
guess = 0
tries = 0

while guess != secret:
    guess = int(input("1〜10の数字を当てて！: "))
    tries += 1
    if guess == secret:
        print("正解！", tries, "回目で当たりました！")
    elif guess > secret:
        print("大きいかも")
    elif guess < secret:
        print("小さいかも")


