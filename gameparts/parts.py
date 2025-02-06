class Board:
    def __init__(self):
        self.field_size = 3
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.field_size + 2))

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or
                    all([self.board[j][i] == player for j in range(self.field_size)])):
                return True
        if (
                self.board[0][0] == self.board[1][1] == self.board[2][2] == player
                or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False
