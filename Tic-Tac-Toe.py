import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
A = [[0] * 3 for i in range(3) ]
current_player = 1
def check_winner():
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2] != 0:
            return A[i][0]
        if A[0][i] == A[1][i] == A[2][i] != 0:
            return A[0][i]
    if A[0][0] == A[1][1] == A[2][2] != 0:
        return A[0][0]
    if A[0][2] == A[1][1] == A[2][0] != 0:
        return A[0][2]
    return 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // (HEIGHT // 3), x // (WIDTH // 3)
            if A[row][col] == 0:
                A[row][col] = current_player
                current_player = 3 - current_player  
    winner = check_winner()
    if winner:
        print(f"Player {winner} wins!")
        pygame.quit()
        sys.exit()
    screen.fill("Cyan")
    for row in range(3):
        for col in range(3):
            if A[row][col] == 1:
                pygame.draw.line(screen, BLACK, (col * WIDTH // 3, row * HEIGHT // 3),
                                 ((col + 1) * WIDTH // 3, (row + 1) * HEIGHT // 3), 2)
                pygame.draw.line(screen, BLACK, ((col + 1) * WIDTH // 3, row * HEIGHT // 3),
                                 (col * WIDTH // 3, (row + 1) * HEIGHT // 3), 2)
            elif A[row][col] == 2:
                pygame.draw.circle(screen, WHITE, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), WIDTH // 6, 10)
    for i in range(1, 3):
        pygame.draw.line(screen, "darkblue", (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), 5)
        pygame.draw.line(screen, "darkblue", (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), 5)

    pygame.display.flip()
