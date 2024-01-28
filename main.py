import pygame
import sys
sys.path.insert(1, 'data/classes')

from data.classes.Board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    board = Board()

    selected_piece = None
    selected_square = None
    valid_moves = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Selecting a piece and moving it. Reselecting a piece should deselect the previous piece. If same piece is selected, deselect it.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i, j = x // 50, y // 50  # Assuming each square is 50x50 pixels
                if selected_piece is None:
                    selected_square = board.board[i][j]
                    selected_piece = selected_square.piece
                    if selected_piece is not None:
                        selected_square.selected = True
                        # Calculate valid moves for the selected piece
                        valid_moves = [(x, y) for x in range(8) for y in range(8) if selected_piece.is_valid_move((selected_square.i, selected_square.j), (x, y), board.board)]
                else:
                    target_square = board.board[i][j]
                    if (i, j) in valid_moves:
                        target_square.piece = selected_piece
                        selected_square.piece = None
                        selected_square.selected = False
                        selected_piece = None
                        selected_square = None
                        valid_moves = []
                    elif target_square.piece is not None and target_square.piece.color == selected_piece.color:
                        # Reselect the piece
                        selected_square.selected = False
                        selected_square = target_square
                        selected_square.selected = True
                        selected_piece = selected_square.piece
                        valid_moves = [(x, y) for x in range(8) for y in range(8) if selected_piece.is_valid_move((selected_square.i, selected_square.j), (x, y), board.board)]
                    else:
                        # Invalid move, show an error message or something
                        pass

        screen.fill((0, 0, 0))
        board.draw(screen)

        # Highlight valid moves
        for (i, j) in valid_moves:
            pygame.draw.rect(screen, (0, 255, 0), board.board[i][j].rect, 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()