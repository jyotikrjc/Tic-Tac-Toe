import string


class TicTacToc:

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.steps = {'X': 0, 'O': 0}
        self.player = 'X'

    def play(self):
        print(self.__str__())
        while not self.is_finished():
            self.move()

    def move(self):
        print("Enter the coordinates: ", end="")
        coordinate = input().split(" ")
        if len(coordinate) != 2:
            print("You should enter numbers!")
            self.move()
        elif coordinate[0] not in string.digits or coordinate[1] not in string.digits:
            print("You should enter numbers!")
            self.move()
        else:
            x = 3 - int(coordinate[1])
            y = int(coordinate[0]) - 1
            if x not in range(0, 3) or y not in range(0, 3):
                print("Coordinates should be from 1 to 3!")
                self.move()
            elif self.board[x][y] != ' ':
                print("This cell is occupied! Choose another one!")
                self.move()
            else:
                self.board[x][y] = self.player
                self.steps[self.player] += 1
                self.player = 'X' if self.player == 'O' else 'O'
                print(self.__str__())

    def is_finished(self):
        if self.is_win('X'):
            print("X wins")
            return True
        elif self.is_win('O'):
            print("O wins")
            return True
        elif sum(self.steps.values()) == 9:
            print("Draw")
            return True
        else:
            return False

    def is_win(self, player):
        for i in range(3):
            if all(x == player for x in self.board[i]) \
                    or all(x == player for x in [self.board[j][i] for j in range(3)]):
                return True
        if all(x == player for x in [self.board[i][i] for i in range(3)]) \
                or all(x == player for x in [self.board[i][2 - i] for i in range(3)]):
            return True
        return False

    def __str__(self):
        return "-" * 9 + "\n" + "\n".join(" ".join(["|", *self.board[i], "|"]) for i in range(3)) + "\n" + "-" * 9


game = TicTacToc()
game.play()
