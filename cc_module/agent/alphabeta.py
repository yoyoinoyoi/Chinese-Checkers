from cc_module.base.board import *


from cc_module.data.data2 import *
from cc_module.data.data3 import *
from cc_module.data.data6 import *

class AB:
    
    def __init__(self, func): #評価関数の係数の決定
        self.func = func
        self.inf = 10**10

    def move_n(self, depth, BOARD, limit, n):#番号nの人の指し手を考える.実装はα-β法
        if depth == 0:
            return self.value_func(BOARD, n), [], []

        value = -self.inf
        m_b, m_a = [], []
        for posi, posj in BOARD.position[n-1]:
            next = BOARD.can_move(posi, posj)
            for posx, posy in next:
                # b を動かすコード
                new_board = Board(BOARD.num, BOARD.board, BOARD.position)
                new_board.move(posi, posj, posx, posy, n)

                if new_board.gameset(n): #動かしたとき、ゲームセット
                    v = self.value_func(new_board, n)
                else:
                    v, _1, _2 = self.move_not_n(depth -1, new_board, value, n, (n % new_board.num) +1)
            # Minmax法 : 先手は大きな値を選ぶ
                if value < v:
                    value = v
                    m_b = [posi, posj]
                    m_a = [posx, posy]
            # alpha-beta法
                if value >= limit:
                    break
        return value, m_b, m_a

    def move_not_n(self, depth, BOARD, limit, n, k):#番号n以外の人の差し手を考える.番号はk番目の人
        if depth == 0:
            return self.value_func(BOARD, n), [], []

        value = self.inf
        m_b, m_a = [], []
        for posi, posj in BOARD.position[k-1]:
            next = BOARD.can_move(posi, posj)
            for posx, posy in next:
                # b を動かすコード
                new_board = Board(BOARD.num, BOARD.board, BOARD.position)
                new_board.move(posi, posj, posx, posy, k)

                if new_board.gameset(k): #動かしたとき、ゲームセット
                    v = self.value_func(new_board, n)
                elif ((k % new_board.num) + 1) == n: #動かした後、n番目の人に戻る
                    v, _1, _2 = self.move_n(depth -1, new_board, value, n)
                else: #動かした後、n番目以外の人になる
                    v, _1, _2 = self.move_not_n(depth -1, new_board, limit, n, (k % new_board.num) +1)
            # Minmax法 : 後手は小さな値を選ぶ
                if value > v:
                    value = v
                    m_b = [posi, posj]
                    m_a = [posx, posy]
            #alpha-beta法
                if value <= limit:
                    break
        return value, m_b, m_a

    #評価関数のセット

    def value_func(self, b, n):#agent 別に評価関数を割り振る
        if self.func == "func1":
            return self.val_func1(b, n)
        
        return self.val_func1(b, n)

    def val_func1(self, b, n):#評価関数1

        v = 0
        pos_score = [0 for _ in range(b.num)]
        
        if b.num == 2:
            top = top2
        elif b.num == 3:
            top = top3
        else:
            top = top6

        for i in range(b.num):
            for k in range(6):
                if ((i + 1) % 3 == 0) and (b.num == 6):
                    pos_score[i] += abs(top[i][0] - b.position[i][k][0]) + abs(top[i][1] - b.position[i][k][1])
                elif (i == 1) and (b.num == 3):
                    pos_score[i] += abs(top[i][0] - b.position[i][k][0]) + abs(top[i][1] - b.position[i][k][1])
                else:
                    pos_score[i] += max(abs(top[i][0] - b.position[i][k][0]), abs(top[i][1] - b.position[i][k][1]))

        #pos_score[i] が盤面的な距離になっている(この距離が小さいほど良い)
        v = -b.num * pos_score[n-1] + sum(pos_score)
        return v

class Alphabeta(Board):
    
    def alphabeta(self, n, config):#コンピュータが駒を動かすまでの流れ
        depth = config[0]
        func = config[1]
        ab = AB(func)
        ab_board = Board(self.num, self.board, self.position)
        _, mb, ma = ab.move_n(depth, ab_board, self.inf, n) ##depthは決めてあげる
        return mb, ma
