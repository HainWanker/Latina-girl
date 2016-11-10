import pygame

pygame.init()

screen = pygame.display.set_mode([300, 500])

lind_y = 250
kiirus_y = 0

toru_x = 300

mäng_alustas = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mäng_alustas = True
                kiirus_y = -30
    screen.fill([169, 0, 200])

    if mäng_alustas:

        lind = pygame.Rect([150, lind_y, 40, 40])
        pygame.draw.rect(screen, [134, 190, 13], lind)

        toru_x -= 5

        toru = pygame.Rect([toru_x, 350, 60, 150])
        pygame.draw.rect(screen, [30, 127, 11], toru)

        toru_üleval = pygame.Rect([toru_x, 0, 60, 150])
        pygame.draw.rect(screen, [30, 127, 11], toru_üleval)

        kiirus_y += 5
        lind_y += kiirus_y

        if toru_x < -60:
            toru_x = 300

        if lind.colliderect(toru):
            lind_y = 250
            toru_x = 300
            mäng_alustas = False

        if lind.colliderect(toru_üleval):
            lind_y = 250
            toru_x = 300
            mäng_alustas = False
      
    pygame.display.flip()

    pygame.time.wait(50)
