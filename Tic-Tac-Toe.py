import pygame
import sys
pygame.init()
#Variables
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("Tic-Tac-Toe")
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
A = []
for i in range(3):
    B = []
    for j in range(1):
        B = [0] * 3
    A.append(B)
current_player = 1
game_started = False
player1_score = 0
player2_score = 0
#defs
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
def check_draw():
    for row in A:
        if 0 in row:
            return False
    return True
def draw_start_button():
    font = pygame.font.Font(None, 36)
    start_text = font.render("Start", True, black)
    start_button = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, "cyan", start_button, 2)
    screen.blit(start_text, start_button)
def start_game():
    global game_started
    game_started = True
def reset_game():
    global A, current_player
    A = []
    for i in range(3):
        B=[]
        for j in range(3):
            B=[0]*3
        A.append(B)
    current_player = 1
def draw_scores():
    font = pygame.font.Font(None, 22)
    magic = "black"
    magic2 = "black"
    if player1_score > player2_score:
        magic = "red"
        magic2 = "black"
    if player1_score < player2_score:
        magic2 = "red"
        magic = "black"
    player1_text = font.render(f"Player 1: {player1_score}", True, magic)
    player2_text = font.render(f"Player 2: {player2_score}", True, magic2)
    screen.blit(player1_text, (20, HEIGHT + 20))
    screen.blit(player2_text, (WIDTH - 100, HEIGHT + 20))
#The main ring
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_started and event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                start_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)
                if start_button_rect.collidepoint(x, y):
                    start_game()
        if game_started and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // (HEIGHT // 3), x // (WIDTH // 3)
            if A[row][col] == 0:
                A[row][col] = current_player
                current_player = 3 - current_player
                winner = check_winner()
                if winner != 0:
                    if winner == 1:
                        player1_score += 1
                    else:
                        player2_score += 1
                    reset_game()
    winner = check_winner()
    if winner != 0:
        print(f"Player {winner} wins!")
    if check_draw():
        print("Draw!")
        reset_game()
    screen.fill("Cyan")
    if not game_started:
        draw_start_button()
    else:
        for row in range(3):
            for col in range(3):
                if A[row][col] == 1:
                    pygame.draw.line(screen, black, (col * WIDTH // 3, row * HEIGHT // 3),
                                     ((col + 1) * WIDTH // 3, (row + 1) * HEIGHT // 3), 2)
                    pygame.draw.line(screen, black, ((col + 1) * WIDTH // 3, row * HEIGHT // 3),
                                     (col * WIDTH // 3, (row + 1) * HEIGHT // 3), 2)
                elif A[row][col] == 2:
                    pygame.draw.circle(screen, white, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6),
                                       WIDTH // 6, 10)
        for i in range(1, 3):
            pygame.draw.line(screen, "darkblue", (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), 5)
            pygame.draw.line(screen, "darkblue", (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), 5)
        draw_scores()
    pygame.display.update()
