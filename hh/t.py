import random

def guess_the_number():
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字，你能猜到它是什么吗？")

    # 随机生成一个1到100之间的数字
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # 用户输入猜测
            guess = int(input("请输入你的猜测（1-100）："))
            attempts += 1

            if guess < 1 or guess > 100:
                print("请输入1到100之间的数字！")
                continue

            if guess < secret_number:
                print("太小了，再试试！")
            elif guess > secret_number:
                print("太大了，再试试！")
            else:
                print(f"恭喜你，猜对了！答案是 {secret_number}。你一共猜了 {attempts} 次。")
                break
        except ValueError:
            print("无效输入，请输入一个整数！")

# 运行游戏
if __name__ == "__main__":
    guess_the_number()