# -*- coding: utf-8 -*-
import random

# GOALまでのマスの数と名前を決める(Decide to goals and your name)
goal = 10
name1 = input("名前を入力してください:")

# サイコロを振る処理とゴールまでの処理(Throw dice and to Goal)
while goal > 0:
    print(name1 + "さん、サイコロを振ってください")
    throw = input("Enterkeyを押すとサイコロを振ります")
    dice = [1, 2, 3, 4, 5, 6]
    number = (random.choice(dice))
    print(number)
    print(str(number) + "マス進みました")
    goal -= number
    if goal <= 0:
        print("ゴールしました！")
    else:
        print("ゴールまで残り" + str(goal) + "マスです")
        print("-----------------------------------------------")
