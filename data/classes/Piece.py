import pygame

class Piece:
    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.image = pygame.image.load(f'data/imgs/Chess{type}{color}.png')

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def is_valid_move(self, current_position, target_position, board):
        dx = target_position[0] - current_position[0]
        dy = target_position[1] - current_position[1]
        #Movement rules for Pieces. None of the pieces can move through other pieces. None of the pieces can move to a square occupied by a piece of the same color. None of the pieces can move to a square that is not on the board.
        if target_position[0] < 0 or target_position[0] > 7 or target_position[1] < 0 or target_position[1] > 7:
            # Can't move off the board
            return False
        if board[target_position[0]][target_position[1]].piece is not None and \
              board[target_position[0]][target_position[1]].piece.color == self.color:
            # Can't move to a square occupied by a piece of the same color
            return False
        if self.type == 'Pawn':
            # Pawns can only move forward one or two squares on their first move. After that, they can only move forward one square. They can also move diagonally one square to capture an opponent's piece. Pawns can never move backwards. Pawns can never move onto a square occupied by a piece of the same color. Pawns can never move through other pieces. Pawns can never move onto a square that is occupied by an opponent's piece unless they are capturing that piece. Pawns can never move diagonally unless they are capturing an opponent's piece.
            if self.color == 'W':
                # White pawns can only move up the board
                if dx == 0 and (dy == -1 or (dy == -2 and current_position[1] == 6)):
                    if dy == -1:
                        if board[current_position[0]][current_position[1] - 1].piece is not None:
                            return False
                    else:
                        if board[current_position[0]][current_position[1] - 1].piece is not None or \
                           board[current_position[0]][current_position[1] - 2].piece is not None:
                            return False
                elif abs(dx) == 1 and dy == -1:
                    if board[target_position[0]][target_position[1]].piece is None:
                        return False
                else:
                    return False
            else:
                if dx == 0 and (dy == 1 or (dy == 2 and current_position[1] == 1)):
                    if dy == 1:
                        if board[current_position[0]][current_position[1] + 1].piece is not None:
                            return False
                    else:
                        if board[current_position[0]][current_position[1] + 1].piece is not None or \
                           board[current_position[0]][current_position[1] + 2].piece is not None:
                            return False
                elif abs(dx) == 1 and dy == 1:
                    if board[target_position[0]][target_position[1]].piece is None:
                        return False
                else:
                    return False
        elif self.type == 'Rook':
            # Rooks cannot move to its current position
            if current_position == target_position:
                return False
            if dx != 0 and dy != 0:
                # Rooks can only move in straight lines
                return False
            if dx != 0:
                step = 1 if dx > 0 else -1
                for x in range(current_position[0] + step, target_position[0], step):
                    if board[x][current_position[1]].piece is not None:
                        # There's a piece in the way
                        return False
            else:
                step = 1 if dy > 0 else -1
                for y in range(current_position[1] + step, target_position[1], step):
                    if board[current_position[0]][y].piece is not None:
                        # There's a piece in the way
                        return False
        elif self.type == 'Knight':
            return abs(dx) == 2 and abs(dy) == 1 or abs(dx) == 1 and abs(dy) == 2
        elif self.type == 'Bishop':
            if current_position == target_position:
                return False
            if abs(dx) != abs(dy):
                return False
            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1
            for x, y in zip(range(current_position[0] + step_x, target_position[0], step_x),
                             range(current_position[1] + step_y, target_position[1], step_y)):
                if board[x][y].piece is not None:
                    return False
        elif self.type == 'Queen':
            # Queen has the combined movement of Rook and Bishop
            if current_position == target_position:
                return False
            if dx == 0 or dy == 0:
                # Rook movement
                if dx != 0:
                    step = 1 if dx > 0 else -1
                    for x in range(current_position[0] + step, target_position[0], step):
                        if board[x][current_position[1]].piece is not None:
                            # There's a piece in the way
                            return False
                else:
                    step = 1 if dy > 0 else -1
                    for y in range(current_position[1] + step, target_position[1], step):
                        if board[current_position[0]][y].piece is not None:
                            # There's a piece in the way
                            return False
            elif abs(dx) == abs(dy):
                # Bishop movement
                step_x = 1 if dx > 0 else -1
                step_y = 1 if dy > 0 else -1
                for x, y in zip(range(current_position[0] + step_x, target_position[0], step_x),
                                range(current_position[1] + step_y, target_position[1], step_y)):
                    if board[x][y].piece is not None:
                        return False
            else:
                return False
        elif self.type == 'King':
            if abs(dx) <= 1 and abs(dy) <= 1:
                target_piece = board[target_position[0]][target_position[1]].piece
                if target_piece is not None and target_piece.color == self.color:
                    # Can't move to a square occupied by a piece of the same color
                    return False
            else:
                return False
        return True