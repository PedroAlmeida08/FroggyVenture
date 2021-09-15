import pygame
import pickle
from os import path
import Draw_Text
import Reset_Level
import World
import Player
import Button
import Globals as gl

pygame.init()

font = pygame.font.SysFont('Bauhaus 93', 64)

pygame.display.set_caption('FroggyVenture')

# load images
tela_menu = pygame.image.load('./Assets/Background/Tela_Menu.png')
bg_img = pygame.image.load('./Assets/Background/BackGround.png')
restart_img = pygame.image.load('./Assets/Buttons/Restart_Button.png')
won_img = pygame.image.load('./Assets/Buttons/Victory.png')
start_img = pygame.image.load('./Assets/Buttons/Start.png')
exit_img = pygame.image.load('./Assets/Buttons/Exit.png')
life_img = pygame.image.load('./Assets/Buttons/Life.png')
level_img = pygame.image.load('./Assets/Buttons/Level.png')
back_img = pygame.image.load('./Assets/Buttons/Back.png')
close_img = pygame.image.load('./Assets/Buttons/Close.png')
rstrt_img = pygame.image.load('./Assets/Buttons/Restart.png')
game_over_img = pygame.image.load('./Assets/Buttons/Game_Over.png')

player = Player.Player(64, gl.HEIGHT - (gl.SIZE * 7))

if path.exists('./Assets/Level/level{}_data'.format(gl.level)):
    pickle_in = open('./Assets/Level/level{}_data'.format(gl.level), 'rb')
    world_data = pickle.load(pickle_in)
world = World.World(world_data)

# create buttons
start_button = Button.Button(gl.WIDTH // 2 - 224, 352, start_img)
exit_button = Button.Button(gl.WIDTH // 2 + 96, 352, exit_img)
restart_button = Button.Button(gl.WIDTH // 2 - 96, gl.HEIGHT // 2 - 128, restart_img)
won_button = Button.Button(gl.WIDTH // 2 - 96, gl.HEIGHT // 2 - 128, won_img)
back_button = Button.Button(gl.WIDTH - 224, 48, back_img)
rstrt_button = Button.Button(gl.WIDTH - 160, 48, rstrt_img)
close_button = Button.Button(gl.WIDTH - 96, 48, close_img)
game_over_button = Button.Button(gl.WIDTH // 2 - 160, gl.HEIGHT // 2 - 128, game_over_img)

life_text = Button.Button((gl.WIDTH // 2) - 128, 48, life_img)
level_text = Button.Button(32, 48, level_img)

run = True
while run:

    gl.clock.tick(gl.fps)

    if gl.main_menu:
        gl.screen.blit(tela_menu, (0, 0))
        if start_button.draw():
            gl.vidas = 3
            gl.game_over = 0
            gl.main_menu = False
        if exit_button.draw():
            run = False
    else:
        gl.screen.blit(bg_img, (0, 0))

        world.draw()

        gl.lvl_group.draw(gl.screen)

        life_text.draw()
        level_text.draw()

        if back_button.draw():
            player.reset(64, gl.HEIGHT - (gl.SIZE * 7))
            gl.main_menu = True
        if rstrt_button.draw():
            player.reset(64, gl.HEIGHT - (gl.SIZE * 7))
            gl.game_over = 0
        if close_button.draw():
            run = False

        gl.check_group.draw(gl.screen)

        if gl.level <= gl.max_level:
            Draw_Text.draw_text(str(gl.level), font, (255, 255, 255), 184, 40)
        Draw_Text.draw_text(str(gl.vidas), font, (255, 255, 255), 668, 40)

        if gl.game_over == 0:
            gl.mushroom_group.update()
            if pygame.sprite.spritecollide(player, gl.mushroom_group, False):
                if gl.vidas > 1:
                    gl.vidas -= 1
                else:
                    gl.game_over = 2
        gl.mushroom_group.draw(gl.screen)

        gl.game_over = player.update(gl.game_over, world)

        # if player has died
        if gl.game_over == -1:
            gl.death_sound.play()
            if restart_button.draw():
                world_data = []
                world = Reset_Level.reset_level(gl.level, player)
                gl.game_over = 0
        if gl.game_over == 2:
            gl.death_sound.play()
            if game_over_button.draw():
                player.reset(64, gl.HEIGHT - (gl.SIZE * 7))
                gl.level = 1
                world_data = []
                world = Reset_Level.reset_level(gl.level, player)
                gl.main_menu = True
        if gl.game_over == 3:
            # reset game and go to next level
            gl.level += 1
            if gl.level <= gl.max_level:
                # reset level
                world_data = []
                world = Reset_Level.reset_level(gl.level, player)
                gl.game_over = 0
            else:
                # restart game
                gl.victory_sound.play()
                if won_button.draw():
                    level = 1
                    world_data = []
                    world = Reset_Level.reset_level(level, player)
                    gl.main_menu = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
