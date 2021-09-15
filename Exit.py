import pygame
import Globals as gl


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('./Assets/Itens/CheckPoint.png')
        self.image = pygame.transform.scale(img, (gl.SIZE * 2, gl.SIZE * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
