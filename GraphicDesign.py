import time

import pygame
import tictactoe

width = 500
height = 500
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("TicTacToe")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 100

user = 'None'
pygame.init()

def main():
    board = tictactoe.initial_state()
    x_offset = 80
    square_space = 15
    y_offset = 30
    square_size = 100
    square = []
    font = pygame.font.Font('freesansbold.ttf', 40)
    fontsmall = pygame.font.Font('freesansbold.ttf', 28)

    """
        Game Loop
    """
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        """
            Draw the game board
        """
        WIN.fill(BLACK)
        for i in range(3):
            row = []
            for j in range(3):
                x = x_offset + (square_size + square_space) * i
                y = y_offset + (square_size + square_space) * j
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(WIN, WHITE, rect, 3)
                row.append(rect)
                if board[i][j] != tictactoe.EMPTY:
                    text = font.render(board[i][j], True, WHITE)
                    textRect = text.get_rect()
                    textRect.center = rect.center
                    WIN.blit(text, textRect)
            square.append(row)

        # check if game finished
        if tictactoe.terminal(board):
            winner = tictactoe.winner(board)
            s = f"{winner} Wins" if winner else "Tie"
            rect1 = pygame.Rect(width // 2 - square_size, 440, 2 * square_size, square_size / 2)
            text = font.render("Play again", True, WHITE)
            textRect = text.get_rect()
            textRect.center = rect1.center
            pygame.draw.rect(WIN, WHITE, rect1, 3)
            WIN.blit(text, textRect)
        else :
            user = tictactoe.player(board)
            s = "Wait... " if user == tictactoe.O else "Your Turn"
        rect = pygame.Rect(width // 2 - square_size // 2, 380, square_size, square_size / 2)
        text = font.render(s, True, WHITE)
        textRect = text.get_rect()
        textRect.center = rect.center
        WIN.blit(text, textRect)
        pygame.display.update()
        if tictactoe.terminal(board):  # check if game finished
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if rect1.collidepoint(x, y):
                    board = tictactoe.initial_state()
        else: # Game not finish
            if user == tictactoe.O: # Computer Turn
                time.sleep(1)
                i, j = tictactoe.minimax(board)
                tictactoe.result(board, (i, j))
            elif user == tictactoe.X:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == tictactoe.EMPTY and square[i][j].collidepoint(x, y):
                                tictactoe.result(board, (i, j))

    pygame.quit()


if __name__ == "__main__":
    main()
