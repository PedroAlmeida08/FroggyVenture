import pygame
from pygame import mixer

clock = pygame.time.Clock()
fps = 60

WIDTH = 1280
HEIGHT = 640
SIZE = 32

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = 0
main_menu = True
level = 1
max_level = 3
vidas = 3

mushroom_group = pygame.sprite.Group()
heart_group = pygame.sprite.Group()
lvl_group = pygame.sprite.Group()
check_group = pygame.sprite.Group()

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.mixer.music.load('./Assets/Sounds/Menu.mp3')
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.set_volume(0.25)
death_sound = pygame.mixer.Sound('./Assets/Sounds/Dead.mp3')
death_sound.set_volume(0.5)
jump_sound = pygame.mixer.Sound('./Assets/Sounds/Jump.mp3')
jump_sound.set_volume(0.5)
victory_sound = pygame.mixer.Sound('./Assets/Sounds/Victory.mp3')
