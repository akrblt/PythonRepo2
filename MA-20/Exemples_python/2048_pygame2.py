import pygame
import random
import time

# Initialize pygame
pygame.init()

# Define colors
colors = {
    0: (238, 228, 218),
    2: (240, 240, 100),
    4: (242, 196, 92),
    8: (242, 145, 55),
    16: (245, 124, 32),
    32: (245, 93, 34),
    64: (245, 56, 23),
    128: (245, 247, 75),
    256: (124, 217, 62),
    512: (0, 204, 0),
    1024: (0, 128, 255),
    2048: (0, 0, 255),
    4096: (155, 155, 255),
    8192: (255, 182, 193)
}

# Define the game grid (initial state)
game = [
    [2, 1024, 4, 8],
    [16, 4, 32, 64],
    [2, 128, 256, 512],
    [8, 0, 32, 0]
]
score = 0  # Initial score
won = False  # Flag to check if the player has won
font = pygame.font.SysFont("Arial", 32)

# Pygame window setup
WIDTH, HEIGHT = 800, 480
CELL_SIZE, MARGIN = 100, 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Timer variables
start_time = time.time()

def update_time():
    time_passed = int(time.time() - start_time)
    timer_text = font.render(f"Time: {time_passed}s", True, (0, 0, 0))
    screen.fill((187, 173, 160), (WIDTH - 150, 20, 150, 50))
    screen.blit(timer_text, (WIDTH - 150, 20))

def display_message(message):
    message_screen = pygame.Surface((300, 150))
    message_screen.fill((255, 223, 0) if message == "You Win!" else (255, 0, 0))
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(150, 75))
    message_screen.blit(text, text_rect)
    screen.blit(message_screen, (WIDTH//2 - 150, HEIGHT//2 - 75))
    pygame.display.update()
    pygame.time.delay(2000)

def display():
    screen.fill((187, 173, 160))
    for row in range(4):
        for col in range(4):
            value = game[row][col]
            color = colors.get(value, (187, 173, 160))
            pygame.draw.rect(screen, color, (
                col * (CELL_SIZE + MARGIN) + MARGIN,
                row * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE),
                border_radius=10)
            if value > 0:
                text = font.render(str(value), True, (255, 255, 255))
                text_rect = text.get_rect(center=(col * (CELL_SIZE + MARGIN) + MARGIN + CELL_SIZE // 2,
                                                  row * (CELL_SIZE + MARGIN) + MARGIN + CELL_SIZE // 2))
                screen.blit(text, text_rect)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (470, 20))
    pygame.display.update()

def add_random_tile():
    empty_cells = [(r, c) for r in range(4) for c in range(4) if game[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        game[r][c] = 2 if random.random() < 0.7 else 4

def pack4(a, b, c, d):
    global score
    nums = [x for x in [a, b, c, d] if x]
    while len(nums) < 4:
        nums.append(0)
    for i in range(3):
        if nums[i] == nums[i + 1] and nums[i] != 0:
            nums[i] *= 2
            score += nums[i]
            nums.pop(i + 1)
            nums.append(0)
    return nums

def move(direction):
    global game
    moved = False
    if direction == "up":
        for c in range(4):
            col = [game[r][c] for r in range(4)]
            new_col = pack4(*col)
            for r in range(4):
                if game[r][c] != new_col[r]:
                    moved = True
                game[r][c] = new_col[r]
    elif direction == "down":
        for c in range(4):
            col = [game[r][c] for r in range(4)][::-1]
            new_col = pack4(*col)[::-1]
            for r in range(4):
                if game[r][c] != new_col[r]:
                    moved = True
                game[r][c] = new_col[r]
    elif direction == "left":
        for r in range(4):
            row = game[r]
            new_row = pack4(*row)
            if game[r] != new_row:
                moved = True
            game[r] = new_row
    elif direction == "right":
        for r in range(4):
            row = game[r][::-1]
            new_row = pack4(*row)[::-1]
            if game[r] != new_row:
                moved = True
            game[r] = new_row
    return moved

def is_lost():
    for r in range(4):
        for c in range(4):
            if game[r][c] == 0:
                return False
            if c < 3 and game[r][c] == game[r][c + 1]:
                return False
            if r < 3 and game[r][c] == game[r + 1][c]:
                return False
    return True

def check_win():
    return (2048 in row for row in game)

def handle_keys():
    global won
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            moved = False
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                moved = move("right")
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                moved = move("left")
            elif event.key in (pygame.K_UP, pygame.K_w):
                moved = move("up")
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                moved = move("down")
            if moved:
                add_random_tile()
                display()
                if check_win() and not won:
                    won = True
                    display_message("You Win!")
                if is_lost():
                    display_message("Game Over!")
                    print(f"Game Over! Total time: {int(time.time() - start_time)}s")
                    #pygame.quit()
                    exit()

# Start the game
add_random_tile()
display()
while True:
    handle_keys()
    update_time()
    pygame.display.update()
    pygame.time.Clock().tick(30)
