"""用Python设计第一个游戏"""
import random

counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("猜一下心里想的数字")
    guess = int(temp)

    if guess == answer:
        print("你是小甲鱼心里的蝗虫嘛？")
        print("猜中了也没奖励")
        break
    else:
        if guess < answer:
            print("小啦")
        else:
            print("大啦")
    counts = counts - 1
print("游戏结束。")
print("答案是:",answer)
print(type(answer))
