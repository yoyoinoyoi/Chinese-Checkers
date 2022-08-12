import copy
from collections import deque

from cc_module.data.data2 import *
from cc_module.data.data3 import *
from cc_module.data.data6 import *

class Board():
    """
    盤面操作の基本
    """
    def __init__(self, num, board, position):#盤面の生成。この地点では駒は一つも置かれていない
        self.board = copy.deepcopy(board)
        self.position = copy.deepcopy(position)
        self.num = num
        self.inf = 10**10
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
                #self.sort_position()
                self.position[n-1] = sorted(self.position[n-1], key = lambda x:x[1])
                self.position[n-1] = sorted(self.position[n-1], key = lambda x:x[0])
                return

    def sort_position(self):#2つの要素のみを持った配列を配列する
        self.position.sort(key = lambda x:x[1])
        self.position.sort(key = lambda x:x[0])
        return

    def prohibit(self):#禁止状態の検出
        if self.num == 2:
            ph = ph2
        elif self.num == 3:
            ph = ph3
        else:
            ph = ph6
        for i in range(self.num):
            Max = 10**12
            Min = -10**12
            
            for j in range(4):
                Max = min(Max, self.board[ ph[i][j][0] ][ ph[i][j][1] ])
                Min = max(Min, self.board[ ph[i][j][0] ][ ph[i][j][1] ])
            if (Max == Min) and (Max == (i +1)):
                return True

        return False
    
    def gameset(self, n):
        if self.num == 2:
            goal = goal2
        elif self.num == 3:
            goal = goal3
        else:
            goal = goal6
        for j in range(6):
            if self.position[n-1][j][0] != goal[n-1][j][0]:
                if self.position[n-1][j][1] != goal[n-1][j][1]:
                    return False
        return True
