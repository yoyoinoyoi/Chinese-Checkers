from cc_module.base.board import Board

class Alphabeta(Board):
    def __init__(self, board, position):
        super().__init__(self, board, position)
        return
    
    def alpha_beta(n):#コンピュータが駒を動かすまでの流れ

        class AB:
            def __init__(self, a = 1): #評価関数の係数の決定
                self.a = a

            def move_n(self, depth, BOARD, limit, n):#番号nの人の指し手を考える.実装はα-β法
                if depth == 0:
                    return self.value_func(BOARD.board, BOARD.position, n), [], []

                value = -self.inf
                m_b, m_a = [], []
                for posi, posj in BOARD.position[n-1]:
                    next = BOARD.can_move(posi, posj)
                    for posx, posy in next:
                        # b を動かすコード
                        new_board = Board(BOARD.board, BOARD.position)
                        new_board.move(posi, posj, posx, posy, n)

                        if new_board.Gameset((n % self.self.num) +1): #動かしたとき、ゲームセット
                            v = self.value_func(new_board.board, new_board.position, n)
                        else:
                            v, _1, _2 = self.move_not_n(depth -1, new_board, value, n, (n % self.num) +1)
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

                value = self.inf
                m_b, m_a = [], []
                for posi, posj in BOARD.position[k-1]:
                    next = BOARD.can_move(posi, posj)
                    for posx, posy in next:
                        # b を動かすコード
                        new_board = Board(BOARD.board, BOARD.position)
                        new_board.move(posi, posj, posx, posy, k)

                        if new_board.Gameset((k % self.num) +1): #動かしたとき、ゲームセット
                            v = self.value_func(new_board.board, new_board.position, k)
                        elif ((k % self.num) + 1) == n: #動かした後、n番目の人に戻る
                            v, _1, _2 = self.move_n(depth -1, new_board, value, n)
                        else: #動かした後、n番目以外の人になる
                            v, _1, _2 = self.move_not_n(depth -1, new_board, limit, n, (k % self.num) +1)
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
                pos_score = [0 for _ in range(self.num)]

                for i in range(self.num):
                    for k in range(6):
                        if ((i + 1) % 3 == 0) and (self.num == 6):
                            pos_score[i] += abs(self.top[i][0] - l[i][k][0]) + abs(self.top[i][1] - l[i][k][1])
                        elif (i == 1) and (self.num == 3):
                            pos_score[i] += abs(self.top[i][0] - l[i][k][0]) + abs(self.top[i][1] - l[i][k][1])
                        else:
                            pos_score[i] += max(abs(self.top[i][0] - l[i][k][0]), abs(self.top[i][1] - l[i][k][1]))

                #pos_score[i] が盤面的な距離になっている(この距離が小さいほど良い)
                v = -self.num * pos_score[n-1] + self.a * sum(pos_score)
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
