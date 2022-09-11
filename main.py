from random import randint

from cc_module.Chinese_checkers import *
import settings

# プレイヤーの種類
players = settings.players
num = len(players)

# 盤面の初期化
cc = Chinese_checkers(num, players)

# gameloop 用の変数
n = randint(1, num)
while not cc.main_board.gameset(n):
    cc.display(n)
    cc.play(n)
    n = (n % num) +1
print("winner is {}".format(n))