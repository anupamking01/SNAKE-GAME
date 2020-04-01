import pygame
import random
import os
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Anupam's Game")
bgimg = pygame.image.load("snake-2.jpg")
pygame.display.update()

#color specific
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#resolution
width = 600
length = 900
pygame.mixer.music.load('Snake Song.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def score_display(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def snake_modify(gameWindow, color, set_limits, snake_len):
    for x, y in set_limits:
        pygame.draw.rect(gameWindow, color, [x, y, snake_len, snake_len])


def Welcome():
    exit_game = False

    while not exit_game:
        gameWindow.fill(white)
        bgimg1 = pygame.image.load("cover.jpg")
        gameWindow.blit(bgimg1,(0,0))
        pygame.display.update()


        score_display("WELCOME TO SNAKE-VILLA", black, 150, 50)
        score_display("PRESS SPC TO CONTINUE", black, 190, 290)
      #  score_display("----------^-----------", black, 210, 330)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    game_loop()
        pygame.display.update()
        clock.tick(60)


# Game Loop
def game_loop():
    exit_game = False
    game_over = False

    # co-ordinates
    snake_x = 50
    snake_y = 50
    # food_co-ordinates
    food_x = 300
    food_y = 450
    # food_size=
    food_l = 10

    # length
    snake_l = 1
    # velocity
    vel_x = 0
    vel_y = 0
    # frame per second
    fps = 60
    score = 0

    # snake_cordinats list
    snk_list = []
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

        # Creating a game loop
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            bgimg2 = pygame.image.load("game_end.jpg")
            gameWindow.blit(bgimg2, (0, 0))
            score_display("Press spc to continue", red, 230, 450)
            #pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    print("keydown")
                    if event.key == pygame.K_RIGHT:
                        vel_x = 3
                        vel_y = 0
                        print("RIGHT")
                    if event.key == pygame.K_LEFT:
                        vel_x = -3
                        vel_y = 0

                    if event.key == pygame.K_UP:
                        vel_x = 0
                        vel_y = -3

                    if event.key == pygame.K_DOWN:
                        vel_x = 0
                        vel_y = 3

            # changing x
            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                snake_l += 5
                pygame.mixer.music.load('chew.mp3')
                pygame.mixer.music.play()
                food_x = random.randint(30, 600)
                food_y = random.randint(50, 500)
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            score_display("Score: " + str(score) + "  Hiscore: "+str(hiscore), red, 5, 5)

            #  pygame.draw.rect(gameWindow, black, [ snake_x, snake_y, snake_l, snake_l ])

            pygame.draw.rect(gameWindow, red, [food_x, food_y, 20, 20])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snake_l:
                del snk_list[0]

            if snake_x >= 900 or snake_y >= 600 or snake_x <= 0 or snake_y <= 0:
                game_over = True
                pygame.mixer.music.load('game_start.mp3')
                pygame.mixer.music.play()

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('game_start.mp3')
                pygame.mixer.music.play()

            snake_modify(gameWindow, blue, snk_list, 20)
        pygame.display.update()
        clock.tick(fps)

        # with open("Score.txt", "w") as f:
       #     f.write(str(hiscore))

#        score_display("SCORE:" + str(score * 10) + "   HIGHSCORE: " + str(hiscore), white, 5, 5)





    pygame.quit()
    quit()

Welcome()



