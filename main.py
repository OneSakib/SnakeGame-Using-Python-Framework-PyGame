import random

import pygame


def gameloop():
    x = pygame.init()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 500
    GAMEWINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    EXIT_GAME = False
    GAME_OVER = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    SCORE = 0
    FONT = pygame.font.SysFont(None, 55)

    def text_screen(text, color, x, y):
        GAMEWINDOW.fill(WHITE)
        screen_text = FONT.render(text, True, color)
        GAMEWINDOW.blit(screen_text, (x, y))
        pygame.display.update()

    # Food
    FOOD_X = random.randint(30, SCREEN_WIDTH / 2)
    FOOD_Y = random.randint(30, SCREEN_HEIGHT / 2)
    FOOD_SIZE = 20
    # Snake Size
    SNAKE_X = 45
    SNAKE_Y = 55
    SNAKE_SIZE = 20
    VELOCITY_X = 0
    VELOCITY_Y = 0
    CLOCK = pygame.time.Clock()
    fps = 30
    SNAKE_LIST = []
    SNAKE_LENGTH = 1

    def plot_snake(GAMEWINDOW, COLOR, SNAKE_LIST, SNAKE_SIZE):
        for SNAKE_X, SNAKE_Y in SNAKE_LIST:
            pygame.draw.rect(GAMEWINDOW, COLOR, [SNAKE_X, SNAKE_Y, SNAKE_SIZE, SNAKE_SIZE])

    while not EXIT_GAME:
        if GAME_OVER:
            GAMEWINDOW.fill(WHITE)
            text_screen("Game Over ! Press Enter to Continue", RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    EXIT_GAME = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    EXIT_GAME = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        VELOCITY_X = 5
                        VELOCITY_Y = 0
                    elif event.key == pygame.K_LEFT:
                        VELOCITY_X = -5
                        VELOCITY_Y = 0

                    elif event.key == pygame.K_DOWN:
                        VELOCITY_Y = 5
                        VELOCITY_X = 0

                    elif event.key == pygame.K_UP:
                        VELOCITY_Y = -5
                        VELOCITY_X = 0
            if abs(SNAKE_X - FOOD_X) < 10 and abs(SNAKE_Y - FOOD_Y) < 10:
                SCORE += 1
                SNAKE_LENGTH += 1
                FOOD_X = random.randint(30, SCREEN_WIDTH / 2)
                FOOD_Y = random.randint(30, SCREEN_HEIGHT / 2)

            SNAKE_X += VELOCITY_X
            SNAKE_Y += VELOCITY_Y
            GAMEWINDOW.fill(WHITE)
            text_screen("SCORE: " + str(SCORE), RED, 5, 5)
            pygame.draw.rect(GAMEWINDOW, RED, [FOOD_X, FOOD_Y, FOOD_SIZE, FOOD_SIZE])

            HEAD = []
            HEAD.append(SNAKE_X)
            HEAD.append(SNAKE_Y)
            SNAKE_LIST.append(HEAD)
            if len(SNAKE_LIST) > SNAKE_LENGTH:
                del SNAKE_LIST[0]

            if SNAKE_X < 0 or SNAKE_X > SCREEN_WIDTH or SNAKE_Y < 0 or SNAKE_Y > SCREEN_HEIGHT:
                GAME_OVER = True
            plot_snake(GAMEWINDOW, BLACK, SNAKE_LIST, SNAKE_SIZE)
            # pygame.draw.rect(GAMEWINDOW, BLACK, [SNAKE_X, SNAKE_Y, SNAKE_SIZE, SNAKE_SIZE])
        pygame.display.update()
        CLOCK.tick(fps)
    pygame.quit()
    quit()


gameloop()
