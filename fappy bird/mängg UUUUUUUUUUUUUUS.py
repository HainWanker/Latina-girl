import pygame
import funktsioonid
import character


pygame.init()

screen = pygame.display.set_mode([300, 500])

bird = character.BirdObject(240, [253,222,21])

toru_x = 300

mäng_alustas = False

while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()

       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               mäng_alustas = True
               bird.jump(-40)

   screen.fill([208, 229, 255])

   if mäng_alustas:

       bird.draw(screen)

       toru_x -= 5

       toru = pygame.Rect([toru_x, 350, 60, 150])
       pygame.draw.rect(screen, [30, 127, 11], toru)

       toru_üleval = pygame.Rect([toru_x, 0, 60, 150])
       pygame.draw.rect(screen, [30, 127, 11], toru_üleval)

       bird.update()

       if toru_x < -60:
           toru_x = 300

       if bird.collide(toru):
           bird.y = 250
           toru_x = 300
           mäng_alustas = False

       if bird.collide(toru_üleval):
           bird.y = 250
           toru_x = 300
           mäng_alustas = False

       if bird.y > 500:
           bird.y = 250
           toru_x = 300
           mäng_alustas = False

   pygame.display.flip()

   pygame.time.wait(50)
