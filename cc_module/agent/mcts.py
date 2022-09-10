import time
import random
import math

from cc_module.base.board import *

from cc_module.data.data2 import *
from cc_module.data.data3 import *
from cc_module.data.data6 import *


class Node:
    # ノードの初期化 state = board とみてよい
    def __init__(self, n, state, position):
        self.n_board = Board(n, state, position)
        self.w = 0 # 累計価値
        self.n = 0 # 試行回数
        self.child_nodes = None  # 子ノード群

    # 局面の価値の計算
    def evaluate(self, k):
        # ゲーム終了時
        #test print("state", state)
        
        # 勝ったとき
        if self.n_board.gameset(k): 
            # 勝敗結果で価値を取得
            value = 1
            # 累計価値と試行回数の更新
            self.w += value
            self.n += 1
            return value
        
        #負けた時
        for i in range(self.n_board.num):
            if self.n_board.gameset(i):
                value = -1 

            # 累計価値と試行回数の更新
                self.w += value
                self.n += 1
                return value

        # 子ノードが存在しない時
        if self.child_nodes == None:
            # プレイアウトで価値を取得

            #確認用
            #print("state")
            #for l in self.state:
            #    print(*l)

            sim = Node(self.n_board.num, self.n_board.board, self.n_board.position)
            value = sim.playout(k)

            # 累計価値と試行回数の更新
            self.w += value
            self.n += 1

            # 子ノードの展開
            if self.n == 10:  #閾値の設定
                self.expand((k % self.n_board.num) +1)
            return value

        # 子ノードが存在する時
        else:
            # UCB1が最大の子ノードの評価で価値を取得
            value = self.next_child_node(k).evaluate((k % self.n_board.num) +1)

            # 累計価値と試行回数の更新
            self.w += value
            self.n += 1
            return value

    # 子ノードの展開
    def expand(self, k):# k番目が動かすノード
        cur_pos = self.n_board.position[k-1]
        self.child_nodes = []
        for i in range(6):
            posi = cur_pos[i][0]
            posj = cur_pos[i][1]
            cand = self.n_board.can_move(posi, posj)
            for j in range(len(cand)):
                if self.enter(posi, posj, cand[j][0], cand[j][1], k) > 0:
                    #盤面的距離が小さくなればそれをcandidateに追加する
                    new_n_board = Board(self.n_board.num, self.n_board.board, self.n_board.position)
                    new_n_board.move(posi, posj, cand[j][0], cand[j][1], k)
                    self.child_nodes.append(Node(self.n_board.num, new_n_board.board, new_n_board.position))

        return

    # UCB1が最大の子ノードの取得
    def next_child_node(self, k):
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
            ucb1_values.append(self.UCB(child_node.w, child_node.n, t))

        # UCB1が最大の子ノードを返す
        if self.n_board.num == k:
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

    def UCB(self, w, n, N):
        C = 1
        return w/n + C*(2*math.log(N)/n)**0.5

    def playout(self, k, depth = 1000):# プレイアウト を行う。nが勝った場合には1,負けた場合には0を返す
        # 負けは状態価値0
        if depth == 0: #詰み状況によるループの防止
            return -1
        
        # 次の状態の状態価値

        r_val = random.randint(0, 100)
        if r_val < 5: # 5 は決める(ε-greedy)
            self.random_action(k)
        else:
            self.greedy_action(k)#error

        result = self.n_board.gameset(k)
        if result > 0:
            if self.n_board.num == result:
                return 1
            else:
                return -1

        return self.playout((k % self.n_board.num) + 1, depth-1)

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
        if self.n_board.num == 2:
            top = top2
        elif self.n_board.num == 3:
            top = top3
        else:
            top = top6

        if (k % 3 == 0) and (self.n_board.num == 6):
            dist1 = abs(top[k-1][0] - posi) + abs(top[k-1][1] - posj)
            dist2 = abs(top[k-1][0] - posx) + abs(top[k-1][1] - posy)
        elif (k == 2) and (self.n_board == 3):
            dist1 = abs(top[k-1][0] - posi) + abs(top[k-1][1] - posj)
            dist2 = abs(top[k-1][0] - posx) + abs(top[k-1][1] - posy)
        else:
            dist1 = max(abs(top[k-1][0] - posi), abs(top[k-1][1] - posj))
            dist2 = max(abs(top[k-1][0] - posx), abs(top[k-1][1] - posy))
                
        return dist1 - dist2 #縮んだ距離

class MCTS(Board):
    
    def mcts_action(self, n):# 一番有効な手を返す(i, j) -> (x, y)の[i, j, x, y]

        # 現在の局面のノードの作成
        root_node = Node(self.num, self.board, self.position)
        root_node.expand(n)

        # 1000回のシミュレーションを実行
        mcts_thinking = time.time()

        cal = 0
        #for _ in range(simulation_list[N-1]):
        while (time.time() - mcts_thinking < 9.99):
            root_node.evaluate(n)
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
        print("calculate: {}".format(cal))

        return [bb, bp]
