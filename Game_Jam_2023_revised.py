import pygame
import pygame_ex
pygame.init()

def main():
    # set up
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    title_name = "Crazy Clicker"

    TITLE = pygame.display.set_caption(title_name)
    ICON = pygame.image.load("img/cookie icon.jpg")
    START = pygame.image.load('img/start_sign.png')
    CONTINUE = pygame.image.load('img/continue_sign.png')
    COOKIE_STORE = pygame.image.load('img/cookie_store2.png')
    pygame.display.set_icon(ICON)

    basic_cookie_img = pygame.image.load('img/fix_basic_cookie.png')
    basic_cookie_width = basic_cookie_img.get_width()
    basic_cookie_height = basic_cookie_img.get_height()
    cool_cookie_img = pygame.image.load('img/fix_cool_cookie.png')
    cool_cookie_width = cool_cookie_img.get_width()
    cool_cookie_height = cool_cookie_img.get_height()
    grand_cookie_img = pygame.image.load('img/fix_grand_cookie.png')
    grand_cookie_width = grand_cookie_img.get_width()
    grand_cookie_height = grand_cookie_img.get_height()
    mighty_cookie_img = pygame.image.load('img/fix_mighty_cookie.png')
    mighty_cookie_width = mighty_cookie_img.get_width()
    mighty_cookie_height = mighty_cookie_img.get_height()

    start_x = SCREEN_WIDTH // 3
    start_y = SCREEN_HEIGHT // 4
    size_factor = 1.2

    cookie_display = basic_cookie_img
    cookie_width = basic_cookie_width
    cookie_height = basic_cookie_height

    # colors
    BLACK = (0, 0, 0)

    # font
    text_font1 = "THEBOLDFONT.ttf"

    # Clock (in sec)
    CLOCK = pygame.time.Clock()
    timer = 10
    millisecond = 1000

    # Costom events
    END_TIME = pygame.USEREVENT + 1
    pygame.time.set_timer(END_TIME, millisecond//10)

    GROW = pygame.USEREVENT + 2
    pygame.time.set_timer(GROW, millisecond//10)

    LEVEL_UP = pygame.USEREVENT + 3
    pygame.time.set_timer(LEVEL_UP, millisecond//10)

    BUTTON = pygame.USEREVENT + 4
    pygame.time.set_timer(BUTTON, millisecond//10)

    # game play varables
    growth_cap = 10
    click_count = 0
    adder = 1
    grow_ammount = 0

    level_cap1 = 3
    level_cap2 = 6
    level_cap3 = 9

    # text function
    score_text = pygame_ex.Text(text_font1, 33)
    time_text = pygame_ex.Text(text_font1, 33)
    end_text = pygame_ex.Text(text_font1, 33)
    title_text = pygame_ex.Text(text_font1, 33)
    highscore_text = pygame_ex.Text(text_font1, 33)

    # main menu loop
    start_button = pygame_ex.Button(SCREEN_WIDTH//2+250, SCREEN_HEIGHT//2+100, START)
    continue_button = pygame_ex.Button(SCREEN_WIDTH//2+250, SCREEN_HEIGHT//2+100, CONTINUE)

    run = True
    rune = True
    runz = True
    start_button.draw(screen)
    while rune:
        reset_ticks = pygame.time.get_ticks()
        screen.blit(COOKIE_STORE, (0, 0))
        title_text.draw(title_name, BLACK, SCREEN_WIDTH//3, 50, screen)
        with open("highscore.txt", 'r') as f:
            hi = f.read()
        highscore_text.draw("highscore " + hi, BLACK, 0, 0, screen)
        if start_button.draw(screen) == True:
            rune = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                rune = False
                run = False
                runz = False
        pygame.display.update()

    # game loop

    while run:
        tc = pygame.time.get_ticks() - reset_ticks
        # count down function
        TIME = timer
        count_down = (tc // millisecond)
        TIME = TIME - count_down

        # displays bg, cookie, score/timer.
        screen.blit(COOKIE_STORE, (0, 0))
        screen.blit(cookie_display, (start_x, start_y))

        # draws the text on the main game

        score_text.draw("clicks\t" + str(click_count), BLACK, 0, 0, screen)
        time_text.draw("time\t" + str(TIME), BLACK, SCREEN_WIDTH - SCREEN_HEIGHT//4, 0, screen)

        # event checker
        key = pygame.key.get_pressed()
        for event in pygame.event.get():

            # if x in window is clicked it exits the game
            if event.type == pygame.QUIT:
                run = False

            # will register input if spacebar is pressed then lifted
            if event.type == pygame.KEYUP and key[pygame.K_SPACE]:
                click_count += adder

            # costume event that is checked when the time == 0 and ends the game
            if event.type == END_TIME:
                if TIME == 0:
                    with open('highscore.txt', 'r') as fr:
                        data = fr.read()
                    if click_count > int(data):
                        with open('highscore.txt', 'w') as f:
                            f.write(str(click_count))
                    pygame.time.set_timer(END_TIME, 0)
                    print(str(TIME))
                    screen.blit(COOKIE_STORE, (0, 0))
                    with open('highscore.txt', 'r') as file:
                        hi = file.read()
                    end_text.draw("your score was " + str(click_count) + " highscore is " + str(hi),
                                  BLACK, SCREEN_WIDTH // 2 - round(SCREEN_WIDTH*0.3), SCREEN_HEIGHT // 2, screen)
                    pygame.display.update()

                    while runz:
                        if continue_button.draw(screen):
                            runz = False
                        for events in pygame.event.get():
                            if events.type == pygame.QUIT:
                                pygame.quit()
                        pygame.display.update()
                    run = False
                    main()

            # costume event that checks if growth cap is reached and if it is it increses the size of the cookie image
            if event.type == GROW:
                growth = click_count
                if growth > growth_cap:
                    cookie_display = pygame.transform.scale(cookie_display, (cookie_width * size_factor, cookie_height * size_factor))
                    cookie_width = cookie_width * size_factor
                    cookie_height = cookie_height * size_factor
                    growth_cap += 10
                    grow_ammount += 1

            # this event checks if the groth ammount is at a specific level cap and if it is then it changes the cookie storage varables and updates screen
            if event.type == LEVEL_UP:

                if grow_ammount == level_cap1:
                    cookie_display = cool_cookie_img
                    cookie_width = cool_cookie_width
                    cookie_height = cool_cookie_height

                elif grow_ammount == level_cap2:
                    cookie_display = grand_cookie_img
                    cookie_width = grand_cookie_width
                    cookie_height = grand_cookie_height

                elif grow_ammount == level_cap3:
                    cookie_display = mighty_cookie_img
                    cookie_width = mighty_cookie_width
                    cookie_height = mighty_cookie_height

        # updates graphics
        pygame.display.update()

    # quits out of game
    pygame.quit()

main()
