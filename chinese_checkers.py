from collections import deque
import math
import random
import copy
import time
import sys
sys.setrecursionlimit(10000000)

#初期盤面, dataset

b_start  = [[-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1, 0, 0,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

b_start2 = [[-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1, 1, 1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1, 1, 1, 1,-1,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1,-1,-1, 2, 2, 2,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 2, 2,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

b_start3 = [[-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1, 1, 1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1, 1, 1, 1,-1,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1,-1, 3, 0, 0, 0, 0, 0, 0, 2,-1,-1,-1],
            [-1, 3, 3, 0, 0, 0, 0, 0, 2, 2,-1,-1,-1],
            [ 3, 3, 3, 0, 0, 0, 0, 2, 2, 2,-1,-1,-1],
            [-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

b_start6 = [[-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1, 1, 1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1, 1, 1, 1,-1,-1,-1],
            [-1,-1,-1, 6, 6, 6, 0, 0, 0, 0, 2, 2, 2],
            [-1,-1,-1, 6, 6, 0, 0, 0, 0, 0, 2, 2,-1],
            [-1,-1,-1, 6, 0, 0, 0, 0, 0, 0, 2,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1,-1, 5, 0, 0, 0, 0, 0, 0, 3,-1,-1,-1],
            [-1, 5, 5, 0, 0, 0, 0, 0, 3, 3,-1,-1,-1],
            [ 5, 5, 5, 0, 0, 0, 0, 3, 3, 3,-1,-1,-1],
            [-1,-1,-1, 4, 4, 4,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 4, 4,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1, 4,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

set2 = [[[ 0, 9], [ 1, 8], [ 1, 9], [ 2, 7], [ 2, 8], [ 2, 9]],
        [[10, 3], [10, 4], [10, 5], [11, 3], [11, 4], [12, 3]]]
set3 = [[[ 0, 9], [ 1, 8], [ 1, 9], [ 2, 7], [ 2, 8], [ 2, 9]],
        [[ 7, 9], [ 8, 8], [ 8, 9], [ 9, 7], [ 9, 8], [ 9, 9]],
        [[ 7, 2], [ 8, 1], [ 8, 2], [ 9, 0], [ 9, 1], [ 9, 2]]]
set6 = [[[ 0, 9], [ 1, 8], [ 1, 9], [ 2, 7], [ 2, 8], [ 2, 9]],
        [[ 3,10], [ 3,11], [ 3,12], [ 4,10], [ 4,11], [ 5,10]],
        [[ 7, 9], [ 8, 8], [ 8, 9], [ 9, 7], [ 9, 8], [ 9, 9]],
        [[10, 3], [10, 4], [10, 5], [11, 3], [11, 4], [12, 3]],
        [[ 7, 2], [ 8, 1], [ 8, 2], [ 9, 0], [ 9, 1], [ 9, 2]],
        [[ 3, 3], [ 3, 4], [ 3, 5], [ 4, 3], [ 4, 4], [ 5, 3]]]

goal2 = [[[10, 3], [10, 4], [10, 5], [11, 3], [11, 4], [12, 3]],
         [[ 0, 9], [ 1, 8], [ 1, 9], [ 2, 7], [ 2, 8], [ 2, 9]]]
goal3 = [[[10, 3], [10, 4], [10, 5], [11, 3], [11, 4], [12, 3]],
         [[ 3, 3], [ 3, 4], [ 3, 5], [ 4, 3], [ 4, 4], [ 5, 3]],
         [[ 3,10], [ 3,11], [ 3,12], [ 4,10], [ 4,11], [ 5,10]]]
goal6 = [[[10, 3], [10, 4], [10, 5], [11, 3], [11, 4], [12, 3]],
         [[ 7, 2], [ 8, 1], [ 8, 2], [ 9, 0], [ 9, 1], [ 9, 2]],
         [[ 3, 3], [ 3, 4], [ 3, 5], [ 4, 3], [ 4, 4], [ 5, 3]],
         [[ 0, 9], [ 1, 8], [ 1, 9], [ 2, 7], [ 2, 8], [ 2, 9]],
         [[ 3,10], [ 3,11], [ 3,12], [ 4,10], [ 4,11], [ 5,10]],
         [[ 7, 9], [ 8, 8], [ 8, 9], [ 9, 7], [ 9, 8], [ 9, 9]]]

top2 = [[12, 3], [ 0, 9]]
top3 = [[12, 3], [ 3, 3], [ 3,12]]
top6 = [[12, 3], [ 9, 0], [ 3, 3], [ 0, 9], [ 3,12], [ 9, 9]]

ph2 =  [[[ 1, 8], [ 1, 9], [ 2, 7], [ 2, 9]],
        [[10, 3], [10, 5], [11, 3], [11, 4]]]
ph3 =  [[[ 1, 8], [ 1, 9], [ 2, 7], [ 2, 9]],
        [[ 7, 9], [ 8, 9], [ 9, 7], [ 9, 8]],
        [[ 7, 2], [ 8, 1], [ 9, 1], [ 9, 2]]]
ph6 =  [[[ 1, 8], [ 1, 9], [ 2, 7], [ 2, 9]],
        [[ 3,10], [ 3,11], [ 4,11], [ 5,10]],
        [[ 7, 9], [ 8, 9], [ 9, 7], [ 9, 8]],
        [[10, 3], [10, 5], [11, 3], [11, 4]],
        [[ 7, 2], [ 8, 1], [ 9, 1], [ 9, 2]],
        [[ 3, 4], [ 3, 5], [ 4, 3], [ 5, 3]]]

class Board():
    def __init__(self, b, pos):#盤面の生成。この地点では駒は一つも置かれていない
        self.board = copy.deepcopy(b)
        self.position = copy.deepcopy(pos)
        return

    def can_move(self, i, j):#(i,j)から動かせるマスを出力する関数
        vec = [[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,-1]] #駒を動かせる方向
        opt = [[i,j]] #駒を動かすことのできる位置の候補

        visited = deque([[i,j]]) #ループ防止のため
        while visited:#飛び越し処理
            si,sj = visited.popleft ()
            for vx,vy in vec:
                if (0 <= si + 2*vx < 13) and  (0 <= sj + 2*vy < 13):#飛び越し先がマップ内かどうか
                    if self.board[si + 2*vx][sj + 2*vy] == 0:            #飛び越し先が0,つまり駒がないかどうか
                        if self.board[si + vx][sj + vy] != 0:            #隣接しているかどうか
                            if [si+2*vx, sj+2*vy] not in opt:   #ループ防止のため、すでにシミュレートしているならそこをとらない
                                visited.append([si+2*vx, sj+2*vy])
                                opt.append([si+2*vx, sj+2*vy])

        for vx,vy in vec:#周囲6マスの処理
                if (0 <= i + vx < 13) and  (0 <= j + vy < 13):
                    if self.board[i + vx][j + vy] == 0:
                        if [i+vx, j+vy] not in opt:
                                visited.append([i+vx, j+vy])
                                opt.append([i+vx, j+vy])

        #self.prohibit()
        return opt[1:]

    def move(self, i, j, x ,y, n):#(i,j)から(x,y)へ動かす。間違っていても関数は動くので注意
        self.board[i][j] = 0
        self.board[x][y] = n
        for np in range(6): #position のほうも更新を行う
            if (self.position[n-1][np][0] == i) and (self.position[n-1][np][1] == j):
                self.position[n-1][np] = [x, y]
                self.sort_position()
                return

    def sort_position(self):#2つの要素のみを持った配列を配列する
        self.position.sort(key = lambda x:x[1])
        self.position.sort(key = lambda x:x[0])
        return

    def Gameset(self, n):#nは勝利したか
        for j in range(6):
            if self.position[n-1][j][0] != goal[n-1][j][0]:
                if self.position[n-1][j][1] != goal[n-1][j][1]:
                    return 0
        return n

    def prohibit(self):#禁止状態の検出
        for i in range(num):
            Max = 10**12
            Min = -10**12
            for j in range(4):
                Max = min(Max, self.board[ ph[i][j][0] ][ ph[i][j][1] ])
                Min = max(Min, self.board[ ph[i][j][0] ][ ph[i][j][1] ])
            if (Max == Min) and (Max == (i +1)):
                return True

        return False

#alpha-betaにかかわる関数

def alpha_beta(n):#コンピュータが駒を動かすまでの流れ

    class AB:
        def __init__(self, a = 1): #評価関数の係数の決定
            self.a = a

        def move_n(self, depth, BOARD, limit, n):#番号nの人の指し手を考える.実装はα-β法
            if depth == 0:
                return self.value_func(BOARD.board, BOARD.position, n), [], []

            value = -inf
            m_b, m_a = [], []
            for posi, posj in BOARD.position[n-1]:
                next = BOARD.can_move(posi, posj)
                for posx, posy in next:
                    # b を動かすコード
                    new_board = Board(BOARD.board, BOARD.position)
                    new_board.move(posi, posj, posx, posy, n)

                    if new_board.Gameset((n % num) +1): #動かしたとき、ゲームセット
                        v = self.value_func(new_board.board, new_board.position, n)
                    else:
                        v, _1, _2 = self.move_not_n(depth -1, new_board, value, n, (n % num) +1)
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
                return self.value_func(BOARD.board, BOARD.position, n), [], []

            value = inf
            m_b, m_a = [], []
            for posi, posj in BOARD.position[k-1]:
                next = BOARD.can_move(posi, posj)
                for posx, posy in next:
                    # b を動かすコード
                    new_board = Board(BOARD.board, BOARD.position)
                    new_board.move(posi, posj, posx, posy, k)

                    if new_board.Gameset((k % num) +1): #動かしたとき、ゲームセット
                        v = self.value_func(new_board.board, new_board.position, k)
                    elif ((k % num) + 1) == n: #動かした後、n番目の人に戻る
                        v, _1, _2 = self.move_n(depth -1, new_board, value, n)
                    else: #動かした後、n番目以外の人になる
                        v, _1, _2 = self.move_not_n(depth -1, new_board, limit, n, (k % num) +1)
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

        def value_func(self, b, l, n):#agent 別に評価関数を割り振る
            return self.val_func1(b, l, n)

        def val_func1(self, b, l, n):#評価関数1

            v = 0
            pos_score = [0 for _ in range(num)]

            for i in range(num):
                for k in range(6):
                    if ((i + 1) % 3 == 0) and (num == 6):
                        pos_score[i] += abs(top[i][0] - l[i][k][0]) + abs(top[i][1] - l[i][k][1])
                    elif (i == 1) and (num == 3):
                        pos_score[i] += abs(top[i][0] - l[i][k][0]) + abs(top[i][1] - l[i][k][1])
                    else:
                        pos_score[i] += max(abs(top[i][0] - l[i][k][0]), abs(top[i][1] - l[i][k][1]))

            #pos_score[i] が盤面的な距離になっている(この距離が小さいほど良い)
            v = -num * pos_score[n-1] + self.a * sum(pos_score)
            return v

    ab_board = Board(board.board, board.position)
    ab = AB(a_list[n-1])
    _, mb, ma = ab.move_n(depth_list[n-1], ab_board, inf, n) ##depthは決めてあげる
    posi, posj = mb[0], mb[1]
    posx, posy = ma[0], ma[1]
    ab_board.move(posi, posj, posx, posy, n)
    board.board = copy.deepcopy(ab_board.board)
    board.position = copy.deepcopy(ab_board.position)
    return

    # モンテカルロ木探索のノードの定義
# モンテカルロ木探索の行動選択
# n番目のプレイヤーに対しての行動選択
def mcts_action(N):# 一番有効な手を返す(i, j) -> (x, y)の[i, j, x, y]

    class Node:
        # ノードの初期化 state = board　とみてよい
        def __init__(self, state, position):
            self.n_board = Board(state, position)
            self.w = 0 # 累計価値
            self.n = 0 # 試行回数
            self.child_nodes = None  # 子ノード群

        # 局面の価値の計算
        def evaluate(self, N, k):
            # ゲーム終了時
            #test print("state", state)
            result = self.n_board.Gameset(k)
            if result > 0: #決着がついたとき
                # 勝敗結果で価値を取得
                if result == N: #勝ったとき
                    value = 1
                else:
                    value = -1 #負けた時

            # 累計価値と試行回数の更新
                self.w += value
                self.n += 1
                return value

            # 子ノードが存在しない時
            if not self.child_nodes:
                # プレイアウトで価値を取得

                #確認用
                #print("state")
                #for l in self.state:
                #    print(*l)

                sim = Node(self.n_board.board, self.n_board.position)
                value = sim.playout(N, k)

                # 累計価値と試行回数の更新
                self.w += value
                self.n += 1

                # 子ノードの展開
                if self.n == 10:  #閾値の設定
                    self.expand(N, (k % num) +1)
                return value

            # 子ノードが存在する時
            else:
                # UCB1が最大の子ノードの評価で価値を取得
                value = self.next_child_node(N, k).evaluate(N, (k % num) +1)

                # 累計価値と試行回数の更新
                self.w += value
                self.n += 1
                return value

        # 子ノードの展開
        def expand(self, N, k):# k番目が動かすノード
            cur_pos = self.n_board.position[k-1]
            self.child_nodes = []
            for i in range(6):
                posi = cur_pos[i][0]
                posj = cur_pos[i][1]
                cand = self.n_board.can_move(posi, posj)
                for j in range(len(cand)):
                    if self.enter(posi, posj, cand[j][0], cand[j][1], k) > 0:
                        #盤面的距離が小さくなればそれをcandidateに追加する
                        new_n_board = Board(self.n_board.board, self.n_board.position)
                        new_n_board.move(posi, posj, cand[j][0], cand[j][1], k)
                        self.child_nodes.append(Node(new_n_board.board, new_n_board.position))

            return

        # UCB1が最大の子ノードの取得
        def next_child_node(self, N, k):
            # 試行回数が0の子ノードを返す
            for child_node in self.child_nodes:
                if child_node.n == 0:
                    return child_node

            # UCB1の計算
            t = 0
            for c in self.child_nodes:
                t += c.n
            ucb1_values = []
            for child_node in self.child_nodes:
                ucb1_values.append(self.val(child_node.w, child_node.n, t))

            # UCB1が最大の子ノードを返す
            if N == k:
                ucb1_max = -100000
                index_list = []
                for s in range(len(ucb1_values)):
                    if ucb1_values[s] == ucb1_max:
                        index_list.append(s)
                    if ucb1_values[s] > ucb1_max:
                        ucb1_max = ucb1_values[s]
                        index_list = [s]
                
                return self.child_nodes[random.choice(index_list)]
            # UCB1が最小の子ノードを返す   
            else:
                ucb1_min = 100000
                index_list = []
                for s in range(len(ucb1_values)):
                    if ucb1_values[s] == ucb1_min:
                        index_list.append(s)
                    if ucb1_values[s] < ucb1_min:
                        ucb1_min = ucb1_values[s]
                        index_list = [s]
                
                return self.child_nodes[random.choice(index_list)]

        def val(self, w, n, N):
            C = 1
            return w/n + C*(2*math.log(N)/n)**0.5

        def playout(self, n, k, depth = 1000):# プレイアウト を行う。nが勝った場合には1,負けた場合には0を返す
            # 負けは状態価値0
            if depth == 0: #詰み状況によるループの防止
                return -1
            
            # 次の状態の状態価値

            r_val = random.randint(0, 100)
            if r_val < 5: # 5 は決める(ε-greedy)
                self.random_action(k)
            else:
                self.greedy_action(k)#error

            result = self.n_board.Gameset(k)
            if result > 0:
                if n == result:
                    return 1
                else:
                    return -1

            return self.playout(n, (k % num) + 1, depth-1)

        def random_action(self, k):#ランダムで手を選び実行する
            cur_pos = self.n_board.position[k-1]
            candidate = []
            for i in range(6):
                posi = cur_pos[i][0]
                posj = cur_pos[i][1]
                cand = self.n_board.can_move(posi, posj)
                for j in range(len(cand)):
                    candidate.append([posi, posj, cand[j][0], cand[j][1]])

            Cho = random.choice(candidate)
            self.n_board.move(Cho[0], Cho[1], Cho[2], Cho[3], k)
            return

        def greedy_action(self, k):#ランダムで手を選び実行するが、手が多すぎるので、少なくとも前進する一手を選ぶように改良する
            cur_pos = self.n_board.position[k-1]
            candidate = []
            max_prog = 0 #縮んだ(進んだ)距離
            for i in range(6):
                posi = cur_pos[i][0]
                posj = cur_pos[i][1]
                cand = self.n_board.can_move(posi, posj)
                for j in range(len(cand)):
                    #盤面的距離が小さくなればそれをcandidateに追加する
                    prog = self.enter(posi, posj, cand[j][0], cand[j][1], k)
                    #盤面的距離が一番小さくなるような一手を選択する
                    if prog >= max_prog:
                        if prog > max_prog:
                            max_prog = prog
                            candidate = [ [posi, posj, cand[j][0], cand[j][1]] ]

                        else:
                            candidate.append([posi, posj, cand[j][0], cand[j][1]])

            if candidate == []:
                return self.random_action(k)

            Cho = random.choice(candidate)
            self.n_board.move(Cho[0], Cho[1], Cho[2], Cho[3], k)
            return

        def enter(self, posi, posj, posx, posy, k): #(posx, posy) -> (posi, posj)#盤面的距離が小さくなるようならそれを採用する
            if num == 2:
                top = top2
            if num == 3:
                top = top3
            if num == 6:
                top = top6

            if (k % 3 == 0) and (num == 6):
                dist1 = abs(top[k-1][0] - posi) + abs(top[k-1][1] - posj)
                dist2 = abs(top[k-1][0] - posx) + abs(top[k-1][1] - posy)
            elif (k == 2) and (num == 3):
                dist1 = abs(top[k-1][0] - posi) + abs(top[k-1][1] - posj)
                dist2 = abs(top[k-1][0] - posx) + abs(top[k-1][1] - posy)
            else:
                dist1 = max(abs(top[k-1][0] - posi), abs(top[k-1][1] - posj))
                dist2 = max(abs(top[k-1][0] - posx), abs(top[k-1][1] - posy))
                
            return dist1 - dist2 #縮んだ距離

    # 現在の局面のノードの作成
    root_node = Node(board.board, board.position)
    root_node.expand(N, N)

    # 1000回のシミュレーションを実行
    if __name__ == '__main__':#時間を計測する
        mcts_thinking = time.time()

    cal = 0
    #for _ in range(simulation_list[N-1]):
    while (time.time() - mcts_thinking < 9.99):
        root_node.evaluate(N, N)
        cal+=1

    # 試行回数の最大値を持つ行動を返す
    n_list = []
    legal_state = []
    legal_pos = []

    for c in root_node.child_nodes: #c: 盤面
        n_list.append(c.n)
        legal_pos.append(c.n_board.position)
        legal_state.append(c.n_board.board)

    #決定した手で実際に動かす
    n_value = -100000
    index_list = []
    for nl in range(len(n_list)):
        if n_list[nl] == n_value:
            index_list.append(nl)
        if n_list[nl] > n_value:
            n_value = n_list[nl]
            index_list = [nl]

    bb = copy.deepcopy(legal_state[random.choice(index_list)])   
    bp = copy.deepcopy(legal_pos[random.choice(index_list)] )
    board = Board(bb, bp)
    print("calculate: {}".format(cal))

    return

def hybrid(n):
    if play < 8:
        alpha_beta(n)
    else:
        mcts_action(n)
    return

def turn(n):#一人が駒を動かすまでの流れ
    dec = input('Simulate...Enter Move...Any string:')
    while dec == '':
        l = list(map(int,input('Which piece do you want to move? (i, j)').split()))#入力がa b
        if len(l) != 2:
            print('Error. Input is 2 variables.')
            continue

        i, j = l[0], l[1]
        if not ((0 <= i < 13) or (0 <= j < 13)):
            print('Error. There is outside board.')
            continue
            
        if (board.board[i][j] != n):
            print('Error. No.{} piece do not exist there.'.format(n))
            continue

        print('You can move these coodinates.')
        for l in board.can_move(board.board, i, j):
            print(*l)

        dec = input('Simulate...Enter Move...Any string:')
            
    flag = 1
    while flag:
        l = list(map(int,input('Move:(i, j) -> (x, y) ').split()))
        if len(l) != 4:
            print('Error. Input is 4 variables.')
            continue
            
        i, j, x, y = l[0], l[1], l[2], l[3]
        if not ((0 <= i < 13) or (0 <= j < 13)):
            print('Error. There is outside board.')
            continue
            
        if (board.board[i][j] != n):
            print('Error. No.{} piece do not exist there.'.format(n))
            continue
            
        if not ((0 <= x < 13) or (0 <= y < 13)):
            print('Error. You cannot move outside board.')
            continue
            
        if (board.board[x][y] != 0):
            print('Error. Some piece has already existed there.')
            continue

        if [x, y] not in board.can_move(board.board, i, j):
            print('Error. You cannot get there.')
            continue

        flag = 0

    board.move(board.board, i, j, x, y, n)
    print('ok. ({}, {}) -> ({}, {})'.format(i, j, x, y))
    board.Map()
    return

def com_turn(n, p):
    if computer_list[p][n-1] == 'a-b':
        func = alpha_beta
    elif computer_list[p][n-1] == 'mcts':
        func = mcts_action
    elif computer_list[p][n-1] == 'hyb':
        func = hybrid
    elif computer_list[p][n-1] == 'self':
        func = turn
    else:
        pass

    func(n)
    return

def sc(l):#数字の情報から駒を表示
    #dic = {-1:'\\', 0:'-', 1:'o', 2:'x', 3:'▲', 4:'●', 5:'+', 6:'▼'}
    dic = {-1:' ', 0:'o', 1:'●', 2:'▲', 3:'■', 4:'●', 5:'+', 6:'▼'}
    ret = []
    for a in l:
        ret.append(dic[a])

    return ret


#ゲームの流れ
#num = int(input('the number of player:(2 or 3 or 6)'))
#定数

inf = 100000
num = 3
if num == 2:
    s = set2
    goal = goal2
    ph = ph2
    top = top2
if num == 3:
    s = set3
    goal = goal3
    ph = ph3
    top = top3
if num == 6:
    s = set6
    goal = goal6
    ph = ph6
    top = top6

#mcts
simulation_list = [1500, 1500, 1000, 1000, 1000, 1000] #シミュレーション回数
shreshold_list = [10, 10, 10, 4, 5, 6] #木の拡大する閾値
#alpha-beta
depth_list = [4, 4, 4] #各エージェントの深さを決定
a_list = [1, 1, 1] # 評価関数の定数a が大きくなれば周りの影響を受けやすい

computer_list = [['a-b', 'mcts'],[]]

#dic = {-1:'\\', 0:'-', 1:'o', 2:'x', 3:'▲', 4:'●', 5:'+', 6:'▼'}
dic = {-1:' ', 0:'o', 1:'●', 2:'▲', 3:'■', 4:'●', 5:'+', 6:'▼'}
for gameplay in range(1):  
    n = 1
    play = 0
    cnt = 0
    board = Board(b_start3, s)
    print("game {}".format(gameplay+1))
    print('---------------------------------------------------------')
    print('player is {} ({}, {})'.format(n, dic[n], computer_list[gameplay][n-1]))
    print(' 0   2   4   6   8   10  12')
    print('0 {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[0])))
    print('1  {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[1])))
    print('2   {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[2])))
    print('3    {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[3])))
    print('4     {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[4])))
    print('5      {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[5])))
    print('6       {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[6])))
    print('7        {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[7])))
    print('8         {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[8])))
    print('9          {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[9])))
    print('10          {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[10])))
    print('11           {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[11])))
    print('12            {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[12])))
    print('                   0   2   4   6   8   10  12')
    while not board.Gameset(n):
        if cnt > 80*num:
            print("quit game")
            break

        start = time.time()

        com_turn(n, gameplay)

        elapsed_time = time.time() - start

        print('---------------------------------------------------------')
        print('player is {} ({}, {})'.format(n, dic[n], computer_list[gameplay][n-1]))
        print(' 0   2   4   6   8   10  12')
        print('0 {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[0])))
        print('1  {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[1])))
        print('2   {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[2])))
        print('3    {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[3])))
        print('4     {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[4])))
        print('5      {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[5])))
        print('6       {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[6])))
        print('7        {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[7])))
        print('8         {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[8])))
        print('9          {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[9])))
        print('10          {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[10])))
        print('11           {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[11])))
        print('12            {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(board.board[12])))
        print('                   0   2   4   6   8   10  12')
        print("thinking time:{0}".format(elapsed_time) + "[sec]")
            
        n = (n % num) + 1
        cnt += 1
        play += 1
