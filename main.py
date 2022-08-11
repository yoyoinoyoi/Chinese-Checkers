from random import randint

from cc_module.Chinese_checkers import *

num = 2

# プレイヤーの種類
players = ["alphabeta", "alphabeta"]

# 盤面の初期化
cc = Chinese_checkers(num, players)

# gameloop 曜の変数
n = randint(1, num)
while not cc.gameset(n):
    cc.display(n)
    cc.play(n)
    n = (n % num) +1
print("winner is {}".format(n))