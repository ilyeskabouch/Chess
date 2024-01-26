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
        if self.type == 'Pawn':
            if self.color == 'W':
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
            if abs(dx) != abs(dy):
                return False
            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1
            for x, y in zip(range(current_position[0] + step_x, target_position[0], step_x),
                             range(current_position[1] + step_y, target_position[1], step_y)):
                if board[x][y].piece is not None:
                    return False
        elif self.type == 'Queen':
            if dx == 0 or dy == 0 or abs(dx) == abs(dy):
                if dx != 0:
                    step = 1 if dx > 0 else -1
                    for x in range(current_position[0] + step, target_position[0], step):
                        if board[x][current_position[1]].piece is not None:
                            return False
                elif dy != 0:
                    step = 1 if dy > 0 else -1
                    for y in range(current_position[1] + step, target_position[1], step):
                        if board[current_position[0]][y].piece is not None:
                            return False
                else:
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