import pygame
from Piece import Piece

class Square:
    def __init__(self, i, j, width, height):
        self.i = i
        self.j = j
        self.width = width
        self.height = height
        self.color = (255,255,255) if (i+j)%2 == 0 else (125,125,125)
        self.piece = None
        self.selected = False
        self.abs_x = i * width
        self.abs_y = j * height
        self.rect = pygame.Rect(self.abs_x, self.abs_y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.selected:
            pygame.draw.rect(screen, (255,0,0), self.rect, 5)
        if self.piece is not None:
            self.piece.draw(screen, self.abs_x, self.abs_y)

    def select(self):
        self.selected = True