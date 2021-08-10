from collections import deque
import random
import copy
import time

#初期盤面

b_start  = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0,-1,-1,-1,-1],
            [-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
            [-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1],
            [-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
            [-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
            [-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
            [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
            [-1,-1,-1,-1, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]


class Board():
    def __init__(self, b):#盤面の生成。この地点では駒は一つも置かれていない
        self.board = b[:]

    def can_move(self, b, i, j):#(i,j)から動かせるマスを出力する関数
        vec = [[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,-1]] #駒を動かせる方向
        opt = [[i,j]] #駒を動かすことのできる位置の候補

        visited = deque([[i,j]]) #ループ防止のため
        while visited:#飛び越し処理
            si,sj = visited.popleft ()
            for vx,vy in vec:
                if (0 <= si + 2*vx < 17) and  (0 <= sj + 2*vy < 17):#飛び越し先がマップ内かどうか
                    if b[si + 2*vx][sj + 2*vy] == 0:            #飛び越し先が0,つまり駒がないかどうか
                        if b[si + vx][sj + vy] != 0:            #隣接しているかどうか
                            if [si+2*vx, sj+2*vy] not in opt:   #ループ防止のため、すでにシミュレートしているならそこをとらない
                                visited.append([si+2*vx, sj+2*vy])
                                opt.append([si+2*vx, sj+2*vy])

        for vx,vy in vec:#周囲6マスの処理
                if (0 <= i + vx < 17) and  (0 <= j + vy < 17):
                    if b[i + vx][j + vy] == 0:
                        if [i+vx, j+vy] not in opt:
                                visited.append([i+vx, j+vy])
                                opt.append([i+vx, j+vy])

        return opt[1:]

    def move(self, b, i, j, x ,y, n):#(i,j)から(x,y)へ動かす。間違っていても関数は動くので注意
        b[i][j] = 0
        b[x][y] = n
        return

    def sc(self, l):#数字の情報から駒を表示
        dic = {-1:'\\', 0:'-', 1:'o', 2:'x', 3:'▲', 4:'●', 5:'+', 6:'▼'}
        ret = []
        for a in l:
            ret.append(dic[a])

        return ret

    def Map(self):#現在の状態を表示する
        print(' 0   2   4   6   8   10  12  14  16 ')
        print('0 {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[0])))
        print('1  {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[1])))
        print('2   {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[2])))
        print('3    {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[3])))
        print('4     {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[4])))
        print('5      {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[5])))
        print('6       {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[6])))
        print('7        {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[7])))
        print('8         {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[8])))
        print('9          {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[9])))
        print('10          {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[10])))
        print('11           {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[11])))
        print('12            {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[12])))
        print('13             {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[13])))
        print('14              {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[14])))
        print('15               {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[15])))
        print('16                {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*self.sc(self.board[16])))
        print('                   0   2   4   6   8   10  12  14  16 ')
        return

    def turn(self, n):#一人が駒を動かすまでの流れ
        dec = input('Simulate...Enter Move...Any string:')
        while dec == '':
            l = list(map(int,input('Which piece do you want to move? (i, j)').split()))#入力がa b
            if len(l) != 2:
                print('Error. Input is 2 variables.')
                continue

            i, j = l[0], l[1]
            if not ((0 <= i < 17) or (0 <= j < 17)):
                print('Error. There is outside board.')
                continue
            
            if (self.board[i][j] != n):
                print('Error. No.{} piece do not exist there.'.format(n))
                continue

            print('You can move these coodinates.')
            for l in self.can_move(self.board, i, j):
                print(*l)

            dec = input('Simulate...Enter Move...Any string:')
            
        flag = 1
        while flag:
            l = list(map(int,input('Move:(i, j) -> (x, y) ').split()))
            if len(l) != 4:
                print('Error. Input is 4 variables.')
                continue
            
            i, j, x, y = l[0], l[1], l[2], l[3]
            if not ((0 <= i < 17) or (0 <= j < 17)):
                print('Error. There is outside board.')
                continue
            
            if (self.board[i][j] != n):
                print('Error. No.{} piece do not exist there.'.format(n))
                continue
            
            if not ((0 <= x < 17) or (0 <= y < 17)):
                print('Error. You cannot move outside board.')
                continue
            
            if (self.board[x][y] != 0):
                print('Error. Some piece has already existed there.')
                continue

            if [x, y] not in self.can_move(self.board, i, j):
                print('Error. You cannot get there.')
                continue

            flag = 0

        self.move(self.board, i, j, x, y, n)
        print('ok. ({}, {}) -> ({}, {})'.format(i, j, x, y))
        self.Map()
        return

    def setup(self, num):#盤面にコマを置く

        set2 = [[[2,12], [2,11], [2,10], [1,12], [1,11], [0,12]],
                [[14,4], [14,5], [14,6], [15,4], [15,5], [16,4]]]
        set3 = [[[2,12], [2,11], [2,10], [1,12], [1,11], [0,12]],
                [[10,12], [11,11], [11,12], [12,10], [12,11], [12,12]],
                [[10,2], [11,1], [11,2], [12,0], [12,1], [12,2]]]
        set6 = [[[2,12], [2,11], [2,10], [1,12], [1,11], [0,12]],
                [[4,14], [4,15], [4,16], [5,14], [5,15], [6,14]],
                [[10,12], [11,11], [11,12], [12,10], [12,11], [12,12]],
                [[14,4], [14,5], [14,6], [15,4], [15,5], [16,4]],
                [[10,2], [11,1], [11,2], [12,0], [12,1], [12,2]],
                [[4,4], [4,5], [4,6], [5,4], [5,5], [6,4]]]

        if num == 2:
            s = set2
        if num == 3:
            s = set3
        if num == 6:
            s = set6

        for i in range(num):
            for j in range(6):
                self.board[s[i][j][0]][s[i][j][1]] = i+1
        return

    def Gameset(self, b):#誰かが勝利したとき、終了する
        goal2 = [[[14,4], [14,5], [14,6], [15,4], [15,5], [16,4]],
                 [[2,12], [2,11], [2,10], [1,12], [1,11], [0,12]]]
        goal3 = [[[14,4], [14,5], [14,6], [15,4], [15,5], [16,4]],
                [[4,4], [4,5], [4,6], [5,4], [5,5], [6,4]],
                [[4,14], [4,15], [4,16], [5,14], [5,15], [6,14]]]
        goal6 = [[[14,4], [14,5], [14,6], [15,4], [15,5], [16,4]],
                [[10,2], [11,1], [11,2], [12,0], [12,1], [12,2]],
                [[4,4], [4,5], [4,6], [5,4], [5,5], [6,4]],
                [[2,12], [2,11], [2,10], [1,12], [1,11], [0,12]],
                [[4,14], [4,15], [4,16], [5,14], [5,15], [6,14]],
                [[10,12], [11,11], [11,12], [12,10], [12,11], [12,12]]]
                
        winner = False

        if num == 2:
            s = goal2
        if num == 3:
            s = goal3
        if num == 6:
            s = goal6

        for i in range(num):
            Max = 10**12
            Min = -10**12
            for j in range(6):
                Max = min(Max, b[ s[i][j][0] ][ s[i][j][1] ])
                Min = max(Min, b[ s[i][j][0] ][ s[i][j][1] ])
            if (Max == Min) and (Max == (i +1)):
                winner = i+1

        return winner

    def Position_n(self, b, n):#番号nの駒の位置を返す関数
        n_list = []
        for i in range(17):
            for j in range(17):
                if b[i][j] == n:
                    n_list.append([i,j])
        return n_list

    def com_turn(self,n):#コンピュータが駒を動かすまでの流れ
        _, mb, ma = self.move_n(depth_list[n-1], self.board, inf, n) ##depthは決めてあげる
        posi, posj = mb[0], mb[1]
        posx, posy = ma[0], ma[1]
        self.move(self.board, posi, posj, posx, posy, n)
        self.Map()
        print('ok. ({}, {}) -> ({}, {})'.format(posi, posj, posx, posy))
        return

    def move_n(self, depth, b, limit, n):#番号nの人の指し手を考える.実装はα-β法
        if depth == 0:
            return self.value_func(b, n), [], []

        value = -inf
        m_b, m_a = [], []
        n_list = self.Position_n(b, n)
        for posi, posj in n_list:
            next = self.can_move(b, posi, posj)
            for posx, posy in next:
                # b を動かすコード
                b_sim = copy.deepcopy(b)
                self.move(b_sim, posi, posj, posx, posy, n)

                if self.Gameset(b_sim): #動かしたとき、ゲームセット
                    v = self.value_func(b_sim, n)
                else:
                    v, _1, _2 = self.move_not_n(depth -1, b_sim, value, n, (n % num) +1)
            # Minmax法 : 先手は大きな値を選ぶ
                if value < v:
                    value = v
                    m_b = [posi, posj]
                    m_a = [posx, posy]
            # alpha-beta法
                if value >= limit:
                    break
        return value, m_b, m_a

    def move_not_n(self, depth, b, limit, n, k):#番号n以外の人の差し手を考える.番号はk番目の人
        if depth == 0:
            return self.value_func(b, n), [], []

        value = inf
        m_b, m_a = [], []
        n_list = self.Position_n(b, k)
        for posi, posj in n_list:
            next = self.can_move(b, posi, posj)
            for posx, posy in next:
                # b を動かすコード
                b_sim = copy.deepcopy(b)
                self.move(b_sim, posi, posj, posx, posy, k)

                if self.Gameset(b_sim): #動かしたとき、ゲームセット
                    v = self.value_func(b_sim, k)
                elif ((k % num) + 1) == n: #動かした後、n番目の人に戻る
                    v, _1, _2 = self.move_n(depth -1, b_sim, value, n)
                else: #動かした後、n番目以外の人になる
                    v, _1, _2 = self.move_not_n(depth -1, b_sim, limit, n, (k % num) +1)
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
        if agent_list[n-1] == 1:
            return self.val_func1(b, n)
        else:
            return self.val_func2(b, n)

    def val_func1(self, b, n):#評価関数1

        goal2 = [[16, 4], [0, 12]]
        goal3 = [[16, 4], [4, 4], [4, 16]]
        goal6 = [[16, 4], [12, 0], [4, 4], [0, 12], [4, 16], [12, 12]]

        v = 0
        pos_list = [[] for _ in range(num)]
        pos_score = [0 for _ in range(num)]
        for i in range(17):
            for j in range(17):
                if b[i][j] > 0:
                    pos_list[ b[i][j] -1].append([i,j])

        if num == 2:
            s = goal2
        if num == 3:
            s = goal3
        if num == 6:
            s = goal6

        for i in range(num):
            for k in range(6):
                if ((i + 1) % 3 == 0) and (num == 6):
                    pos_score[i] += abs(s[i][0] - pos_list[i][k][0]) + abs(s[i][1] - pos_list[i][k][1])
                elif (i == 1) and (num == 3):
                    pos_score[i] += abs(s[i][0] - pos_list[i][k][0]) + abs(s[i][1] - pos_list[i][k][1])
                else:
                    pos_score[i] += max(abs(s[i][0] - pos_list[i][k][0]), abs(s[i][1] - pos_list[i][k][1]))

        a = 1 #係数
        #pos_score[i] が盤面的な距離になっている(この距離が小さいほど良い)
        v = -num * pos_score[n-1] + a * sum(pos_score)
        return v

    def val_func2(self, b, n):#評価関数1

        goal2 = [[16, 4], [0, 12]]
        goal3 = [[16, 4], [4, 4], [4, 16]]
        goal6 = [[16, 4], [12, 0], [4, 4], [0, 12], [4, 16], [12, 12]]

        v = 0
        pos_list = [[] for _ in range(num)]
        pos_score = [0 for _ in range(num)]
        for i in range(17):
            for j in range(17):
                if b[i][j] > 0:
                    pos_list[ b[i][j] -1].append([i,j])

        if num == 2:
            s = goal2
        if num == 3:
            s = goal3
        if num == 6:
            s = goal6

        for i in range(num):
            for k in range(6):
                if ((i + 1) % 3 == 0) and (num == 6):
                    pos_score[i] += abs(s[i][0] - pos_list[i][k][0]) + abs(s[i][1] - pos_list[i][k][1])
                elif (i == 1) and (num == 3):
                    pos_score[i] += abs(s[i][0] - pos_list[i][k][0]) + abs(s[i][1] - pos_list[i][k][1])
                else:
                    pos_score[i] += max(abs(s[i][0] - pos_list[i][k][0]), abs(s[i][1] - pos_list[i][k][1]))

        a = 0.5 #係数
        #pos_score[i] が盤面的な距離になっている(この距離が小さいほど良い)
        v = -num * pos_score[n-1] + a * sum(pos_score)
        return v

#ゲームの流れ
num = int(input('the number of player:(2 or 3 or 6)'))

#変数

inf = 100000
player_list = [i+1 for i in range(num)]
computer_list = ['' for _ in range(num)]
agent_list = ['' for i in range(num)] #度のエージェントを用いるのかを決定
depth_list = [3 for i in range(num)] #各エージェントの深さを決定

for i in range(num):
    computer_list[i] = input('Is player{} human? Yes...Enter '.format(i+1))
    if computer_list[i] != '':
        agent_list[i] = input('What is No.{} agent type?(1, 2 or 3)'.format(i+1))
n = random.choice(player_list)#順番はランダムで時計回り

#ロードするかどうか
f1 = input('Load? Yes:1 No:Enter')
if f1 == '1':
    n = int(input('player number:'))
    L = [list(map(int,input('{} line'.format(i+1)).split())) for i in range(17)]
    board = Board(L)
else:
    board = Board(b_start)
    board.setup(num)

board.Map()
while not board.Gameset(board.board):
    dic = {-1:'\\', 0:'-', 1:'o', 2:'x', 3:'▲', 4:'●', 5:'+', 6:'▼'}
    print('---------------------------------------------------------')
    print('player is {} ({})'.format(n,dic[n]))
    if computer_list[n-1] == '':
        board.turn(n)
    else:
        if __name__ == '__main__':#時間を計測する
            start = time.time()

            board.com_turn(n)

            elapsed_time = time.time() - start
            print("thinking time:{0}".format(elapsed_time) + "[sec]")

    n %= num
    n += 1

print('winner is {}'.format(board.Gameset(board.board)))
