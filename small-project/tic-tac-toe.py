import numpy as np


class tic_tac_toe:
    def __init__(self):
        self.header = ['1', '2', '3']
        self.board = [['-' for i in range(3)] for j in range(3)]
        self.array = np.array([0, 1] * 5)

        self.answer_list = \
            [
                [[0, 0], [1, 1], [2, 2]],
                [[0, 2], [1, 1], [2, 0]],

                [[0, 0], [0, 1], [0, 2]],
                [[1, 0], [1, 1], [1, 2]],
                [[2, 0], [2, 1], [2, 2]],

                [[0, 0], [0, 1], [0, 2]],
                [[1, 0], [1, 1], [1, 2]],
                [[2, 0], [2, 1], [2, 2]]
            ]

        self.main()

    def display(self):
        print('  ' + ' '.join(self.header))
        for i in range(len(self.board)):
            print(str(i + 1) + ' ' + ' '.join(self.board[i]))

    def _change_board(self, array, player):
        if player == 0:
            try:
                if array[0] and array[1] < len(self.board) + 1:
                    if self.board[array[0] - 1][array[1] - 1] == '-':
                        self.board[array[0] - 1][array[1] - 1] = 'O'
                        self.display()
                        return True
                    else:
                        return False
                else:
                    return False
            except IndexError:
                return False
        else:
            try:
                if array[0] and array[1] < len(self.board) + 1:
                    if self.board[array[0] - 1][array[1] - 1] == '-':
                        self.board[array[0] - 1][array[1] - 1] = 'X'
                        self.display()
                        return True
                    else:
                        return False
                else:
                    return False
            except IndexError:
                return False

    def _input_answer(self, num):
        x = [int(y) for y in input('input number: ').split()]
        if self._change_board(x, num):
            return True
        else:
            print('Input Again')
            self._input_answer(num)

    def _player_action(self, num):
        if num == 0:
            print('Player 1')
            self._input_answer(num)
            return True
        else:
            print('Player 2')
            self._input_answer(num)
            return True

    def _answer(self, num):
        if num == 0:
            for i in self.answer_list:
                a = 0
                for j in i:
                    if self.board[j[0]][j[1]] == 'O':
                        a += 1
                        if a == 3:
                            break
                    if a == 3:
                        break
                if a == 3:
                    print('Win Player 1')
                    return True
        else:
            pass

    def main(self):
        z = 0
        self.display()

        while True:
            if self._player_action(self.array[z]):
                if self._answer(self.array[z]):
                    break
                z += 1
                if z == len(self.array):
                    break
            else:
                pass


if __name__ == '__main__':
    main = tic_tac_toe()
