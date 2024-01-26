from Square import Square
from Piece import Piece

class Board:
    def __init__(self):
        self.board = [[Square(i, j, 50, 50) for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    self.board[i][j].color = (255,255,255)  # white square
                else:
                    self.board[i][j].color = (125,125,125)  # black square
                if j == 1:
                    self.board[i][j].piece = Piece('B', 'Pawn')
                elif j == 6:
                    self.board[i][j].piece = Piece('W', 'Pawn')
                elif j == 0:
                    if i in [0, 7]:
                        self.board[i][j].piece = Piece('B', 'Rook')
                    elif i in [1, 6]:
                        self.board[i][j].piece = Piece('B', 'Knight')
                    elif i in [2, 5]:
                        self.board[i][j].piece = Piece('B', 'Bishop')
                    elif i == 3:
                        self.board[i][j].piece = Piece('B', 'Queen')
                    elif i == 4:
                        self.board[i][j].piece = Piece('B', 'King')
                elif j == 7:
                    if i in [0, 7]:
                        self.board[i][j].piece = Piece('W', 'Rook')
                    elif i in [1, 6]:
                        self.board[i][j].piece = Piece('W', 'Knight')
                    elif i in [2, 5]:
                        self.board[i][j].piece = Piece('W', 'Bishop')
                    elif i == 3:
                        self.board[i][j].piece = Piece('W', 'Queen')
                    elif i == 4:
                        self.board[i][j].piece = Piece('W', 'King')

    def draw(self, screen):
        for row in self.board:
            for square in row:
                square.draw(screen)