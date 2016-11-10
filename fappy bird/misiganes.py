import pygame

class birdobject():
    def __init__(self, y, bird_color):
        self.y = y
        self.color = bird_color
        self.y_vel = 0
        self.rect = pygame.rect([130, self.y, 40, 40])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, slf.rect)

    def jump(self, vel):
        self.y_vel = vel

    def update(self):
        self.y_vel += 5
        self.y += self.y_vel
        self.rect = pygame.rect([130, self.y, 40, 40])

    def collide(self, target):
        a = self.rect.colliderect(target)
        return a
    
    
