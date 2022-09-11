from cc_module.base.board import Board
from cc_module.play import *
from cc_module.data.data2 import *
from cc_module.data.data3 import *
from cc_module.data.data6 import *

class Chinese_checkers():
    def __init__(self, num, players):
        self.num = num
        self.players = players
        self.inf = 10**10
        if self.num == 2:
            self.start = start2
            self.set = set2
            self.goal = goal2
            self.top = top2
            self.ph = ph2
        elif self.num == 3:
            self.start = start3
            self.set = set3
            self.goal = goal3
            self.top = top3
            self.ph = ph3
        elif self.num == 6:
            self.start = start6
            self.set = set6
            self.goal = goal6
            self.top = top6
            self.ph = ph6
        else:
            print("Error")
            return
        
        self.main_board = Play(self.num, self.start, self.set)
        return

    def play(self, n):
        #print(self.num, self.players)
        agent = self.players[n-1]
        if agent == "alphabeta":
            mb, ma = self.main_board.alphabeta(n)
            self.main_board.move(mb[0], mb[1], ma[0], ma[1], n)
            
        elif agent == "selfplay":
            mb, ma = self.main_board.selfplay(n)
            self.main_board.move(mb[0], mb[1], ma[0], ma[1], n)
            
        elif agent == "mcts":
            bb, bp = self.main_board.mcts_action(n)
            self.main_board.board = copy.deepcopy(bb)
            self.main_board.position = copy.deepcopy(bp)
            self.main_board.sort_position(n)
        
    def gameset(self, n):
        for j in range(6):
            if self.main_board.position[n-1][j][0] != self.goal[n-1][j][0]:
                if self.main_board.position[n-1][j][1] != self.goal[n-1][j][1]:
                    return False
        return True

    def display(self, n):
        dic = {-1:'\\', 0:'-', 1:'o', 2:'x', 3:'+', 4:'●', 5:'@', 6:'▼'}
        
        def sc(l):
            ret = []
            for a in l:
                ret.append(dic[a])

            return ret

        print('---------------------------------------------------------')
        print('player is {} ({}, {})'.format(n, dic[n], self.players[n-1]))
        print(' 0   2   4   6   8   10  12')
        print('0 {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[0])))
        print('1  {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[1])))
        print('2   {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[2])))
        print('3    {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[3])))
        print('4     {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[4])))
        print('5      {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[5])))
        print('6       {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[6])))
        print('7        {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[7])))
        print('8         {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[8])))
        print('9          {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[9])))
        print('10          {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[10])))
        print('11           {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[11])))
        print('12            {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(*sc(self.main_board.board[12])))
        print('                   0   2   4   6   8   10  12')
        # for i in range(self.main_board.num):
        #     print('player {} positions: {}'.format(i+1, self.main_board.position[i]))
        return
    