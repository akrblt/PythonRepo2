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
    [0, 2, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0]
]

score = 0  # Initial score
won = False  # Flag to check if the player has won
font = pygame.font.SysFont("Arial", 32)

# Pygame window setup
WIDTH = 800
HEIGHT = 480
GRID_SIZE = 4
CELL_SIZE = 100
MARGIN = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Timer variables
start_time = None
timer_running = False


# Function to update time
def update_time():
    if timer_running:
        time_passed = int(time.time() - start_time)
        timer_text = font.render(f"Time: {time_passed}s", True, (0, 0, 0))
        screen.fill((187, 173, 160), (WIDTH - 150, 20, 150, 50))  # clean dernier time
        screen.blit(timer_text, (WIDTH - 150, 20))  # write new time


def start_timer():
    global start_time, timer_running
    start_time = time.time()
    timer_running = True


def stop_timer():
    global timer_running
    timer_running = False


# Function to display the grid
def display():
    screen.fill((187, 173, 160))  # Background color

    # Draw the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = game[row][col]
            color = colors.get(value, (187, 173, 160))
            pygame.draw.rect(screen, color, (
            col * (CELL_SIZE + MARGIN) + MARGIN, row * (CELL_SIZE + MARGIN) + MARGIN, CELL_SIZE, CELL_SIZE),
                             border_radius=10)

            if value > 0:
                text = font.render(str(value), True, (255, 255, 255))
                text_rect = text.get_rect(center=(col * (CELL_SIZE + MARGIN) + MARGIN + CELL_SIZE // 2,
                                                  row * (CELL_SIZE + MARGIN) + MARGIN + CELL_SIZE // 2))
                screen.blit(text, text_rect)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (470, 20))

    # Update the display
    pygame.display.update()


# Add a random tile (2 or 4)
def add_random_tile():
    empty_cells = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if game[row][col] == 0:
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)
        game[row][col] = 2 if random.random() < 0.7 else 4


# Move and merge functions
def pack4(a, b, c, d):
    nm = 0

    if c == 0 and d > 0:
        c, d = d, 0
        nm += 1
    if b == 0 and c > 0:
        b, c, d = c, d, 0
        nm += 1
    if a == 0 and b > 0:
        a, b, c, d = b, c, d, 0
        nm += 1

    if a == b and a > 0:
        nm += 1
        a *= 2
        global score
        score += a
        b, c, d = c, d, 0
    if b == c and b > 0:
        nm += 1
        b *= 2
        score += b
        c, d = d, 0
    if c == d and d > 0:
        nm += 1
        c *= 2
        score += c
        d = 0

    return [a, b, c, d], nm


def move_up():
    tot_mov = 0
    for col in range(GRID_SIZE):
        new_values, nm = pack4(game[0][col], game[1][col], game[2][col], game[3][col])
        game[0][col], game[1][col], game[2][col], game[3][col] = new_values
        tot_mov += nm
    return tot_mov


def move_down():
    tot_mov = 0
    for col in range(GRID_SIZE):
        new_values, nm = pack4(game[3][col], game[2][col], game[1][col], game[0][col])
        game[3][col], game[2][col], game[1][col], game[0][col] = new_values
        tot_mov += nm
        tot_mov += nm
    return tot_mov


def move_left():
    tot_mov = 0
    for row in range(GRID_SIZE):
        new_values, nm = pack4(game[row][0], game[row][1], game[row][2], game[row][3])
        game[row][0], game[row][1], game[row][2], game[row][3] = new_values
        tot_mov += nm
        tot_mov += nm
    return tot_mov


def move_right():
    tot_mov = 0
    for row in range(GRID_SIZE):
        new_values, nm = pack4(game[row][3], game[row][2], game[row][1], game[row][0])
        game[row][3], game[row][2], game[row][1], game[row][0] = new_values
        tot_mov += nm
    return tot_mov


# Game over check
def lost():
    def nb_empty_tiles():
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if game[row][col] == 0:
                    return True
        return False

    def no_merge_possible():
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if col < 3 and game[row][col] == game[row][col + 1]:
                    return True
                if row < 3 and game[row][col] == game[row + 1][col]:
                    return True
        return False

    if not nb_empty_tiles() and not no_merge_possible():
        return True
    return False


# Check if the player wins
def check_win():
    global won
    for row in game:
        if 2048 in row:
            won = True
            stop_timer()
            return True
    return False


# Handle keypresses for moves
def handle_keys():
    global won
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            moved = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moved = move_right()
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moved = move_left()
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                moved = move_up()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moved = move_down()
            elif event.key == pygame.K_q:
                pygame.quit()

            if moved:
                add_random_tile()
                display()
                if lost():
                    stop_timer()
                    print("Game Over!")
                    pygame.quit()
                if check_win() and not won:
                    print("You Win!")
                    pygame.quit()
                    break


# Main game loop
start_timer()
add_random_tile()
display()

while True:
    handle_keys()
    update_time()
    pygame.display.update()
    pygame.time.Clock().tick(30)  # Frame rate
