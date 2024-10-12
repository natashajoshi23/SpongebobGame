def main():
    import pygame, sys
    pygame.init()


    screenW = 800
    screenH = 500


    screen = pygame.display.set_mode((screenW, screenH))
    pygame.display.set_caption('Space Invaders')


    bg = pygame.image.load('beach background.png')
    bg = pygame.transform.scale(bg, (800, 500))
    xpos = 0
    ypos = 0

    ship = pygame.image.load('spongebob.png')
    ship = pygame.transform.scale(ship, (120, 120))
    sx = 350
    sSpeed = 0

    bullet = pygame.image.load('burger bullet.png')
    bullet = pygame.transform.scale(bullet, (23, 23))
    by = -200
    bx = -300
    bSpeed = .8

    alienList = []
    xPos = []
    yPos = []
    num = 0
    aspeed = .9

    # sounds
    bg_music = pygame.mixer.Sound("Spongebob Squarepants - Ending.mp3")
    alien_sound = pygame.mixer.Sound("other sound.wav")
    bullet_sound = pygame.mixer.Sound("sound2.wav")


    for i in range(5):
        for j in range(11):
            if i == 0 or i == 1:
                alienList.append(pygame.image.load('patrick.png').convert_alpha())
                alienList[num] = pygame.transform.scale(alienList[num], (40, 60))
                xPos.append(j * 50 + 5)
                yPos.append(i * 57 + 4)
                num += 1
            if i == 2 or i == 3:
                alienList.append(pygame.image.load('gary.webp').convert_alpha())
                alienList[num] = pygame.transform.scale(alienList[num], (40, 50))
                xPos.append(j * 50 + 5)
                yPos.append(i * 57 + 4)
                num += 1
            if i == 4:
                alienList.append(pygame.image.load('mr krabs.png').convert_alpha())
                alienList[num] = pygame.transform.scale(alienList[num], (60, 80))
                xPos.append(j * 50 + 5)
                yPos.append(i * 54 + 4)
                num += 1
    # scores
    score = 0

    # define the score board function
    def display_scores():
       font = pygame.font.SysFont('comic sans', bold = True, size=25)
       text = font.render(f"Score: {score}", True, (70,130,180))
       text_rect = text.get_rect(center=(68,20))
       screen.blit(text, text_rect)


    # winner
    def game_over():
     if yPos[i] > 600:
         pygame.mixer.Sound.play(bg_music)
         screen.fill((0, 0, 0))
         font3 = pygame.font.SysFont('comic sans', 50)
         text3 = font3.render(f"GAME OVER!!", True, (255, 255, 255), None)
         text3_rect = text3.get_rect(center=(screenW / 2, 200))
         screen.blit(text3, text3_rect)
         font4 = pygame.font.SysFont('comic sans', 30)
         text4 = font4.render(f"You lost :(", True, (255, 255, 255), None)
         text4_rect = text4.get_rect(center=(screenW / 2, 370))
         screen.blit(text4, text4_rect)

     if score == 55:
         pygame.mixer.Sound.play(bg_music)
         screen.fill((0, 0, 0))
         font3 = pygame.font.SysFont('comic sans', 50)
         text3 = font3.render(f"GAME OVER!!", True, (255, 255, 255), None)
         text3_rect = text3.get_rect(center=(screenW / 2, 200))
         screen.blit(text3, text3_rect)
         font5 = pygame.font.SysFont('comic sans', 30)
         text5 = font5.render(f"You win! :)", True, (255, 255, 255), None)
         text5_rect = text5.get_rect(center=(screenW / 2, 370))
         screen.blit(text5, text5_rect)

    # set the start screen flag
    start_screen = True

    # start screen loop
    while start_screen:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               start_screen = False
               game_over = True
           if event.type == pygame.KEYDOWN:
               start_screen = False

       # draw the start screen
       screen.fill((0, 0, 0))
       font = pygame.font.SysFont('comic sans', size=50)
       font2 = pygame.font.SysFont('comic sans', size=35)
       font3 = pygame.font.SysFont('comic sans', size=15)
       title = font.render("Space Invaders", True, (255, 255, 255))
       message = font2.render("Press any key to start", True, (255, 255, 255))
       name = font3.render("Created by Natasha", True, (255, 255, 255))
       start_text_rect = title.get_rect(center=(screenW / 2, 200))
       screen.blit(title, start_text_rect)
       start_text_rect2 = title.get_rect(center=(screenW / 2, 300))
       screen.blit(message, start_text_rect2)
       start_text_rect3 = name.get_rect(center=(715, 480))
       screen.blit(name, start_text_rect3)
       pygame.display.update()


    gameOn = True


    while gameOn:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    sSpeed += 2
                if e.key == pygame.K_LEFT:
                    sSpeed -= 2
                if e.key == pygame.K_SPACE and by < 0:
                    pygame.mixer.Sound.play(bullet_sound)
                    bx = sx + 40
                    by = 460 - 100
                    bSpeed = -2
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    sSpeed -= 2
                if e.key == pygame.K_LEFT:
                    sSpeed += 2

        # logic
        sx += sSpeed
        if sx > 685:
            sx = 685
        if sx < 0:
            sx = 0

        by += bSpeed
        changeD = False
        for i in range(55):
            xPos[i] += aspeed
            if xPos[i] > screenW - 25 or xPos[i] < 0:
                changeD = True

        if changeD:
            changeD = False
            aspeed *= -1
            for i in range(55):
                yPos[i] += 20

        for i in range(55):
            if pygame.rect.Rect(bx, by, bullet.get_width(), bullet.get_height()).colliderect(pygame.rect.Rect(xPos[i], yPos[i], alienList[i].get_width(), alienList[i].get_height())):
                pygame.mixer.Sound.play(alien_sound)
                score += 1
                yPos[i] -= 3000
                by -= 500
                pygame.rect.Rect(bx, by, bullet.get_width(), bullet.get_height())
    #display
        screen.fill((0,0,0))
        screen.blit(bg, (xpos,ypos))
        screen.blit(ship, (sx, 370))
        screen.blit(bullet, (bx, by))
        for i in range(55):
            screen.blit(alienList[i], (xPos[i], (yPos[i])))
        display_scores()
        game_over()
        pygame.display.update()

main()