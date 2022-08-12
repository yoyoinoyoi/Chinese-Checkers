from cc_module.base.board import *

class Selfplay(Board):
    
    def selfplay(self, n):#一人が駒を動かすまでの流れ
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
                
            if (self.board[i][j] != n):
                print('Error. No.{} piece do not exist there.'.format(n))
                continue

            print('You can move these coodinates.')
            for l in self.can_move(i, j):
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
                
            if (self.board[i][j] != n):
                print('Error. No.{} piece do not exist there.'.format(n))
                continue
                
            if not ((0 <= x < 13) or (0 <= y < 13)):
                print('Error. You cannot move outside board.')
                continue
                
            if (self.board[x][y] != 0):
                print('Error. Some piece has already existed there.')
                continue

            if [x, y] not in self.can_move(i, j):
                print('Error. You cannot get there.')
                continue

            flag = 0

        # self.move(i, j, x, y, n)
        print('ok. ({}, {}) -> ({}, {})'.format(i, j, x, y))
        #self.Map()
        return [i, j], [x, y]
