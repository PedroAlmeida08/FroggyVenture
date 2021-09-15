import pygame
import Globals as gl
import Enemy
import Exit


class World:
    def __init__(self, data, ):
        self.tile_list = []

        # load images
        canto_dir_img = pygame.image.load('./Assets/Terreno/0.png')        # 0
        meio_cima_img = pygame.image.load('./Assets/Terreno/1.png')        # 1
        canto_esq_img = pygame.image.load('./Assets/Terreno/2.png')        # 2
        meio_dir_img = pygame.image.load('./Assets/Terreno/3.png')         # 3
        meio_meio_img = pygame.image.load('./Assets/Terreno/4.png')        # 4
        meio_esq_img = pygame.image.load('./Assets/Terreno/5.png')         # 5
        inf_dir_img = pygame.image.load('./Assets/Terreno/8.png')          # 6
        inf_meio_img = pygame.image.load('./Assets/Terreno/7.png')         # 7
        inf_esq_img = pygame.image.load('./Assets/Terreno/6.png')          # 8
        hud_canto_dir_img = pygame.image.load('./Assets/Terreno/9.png')    # 9
        hud_meio_cima_img = pygame.image.load('./Assets/Terreno/10.png')   # 10
        hud_canto_esq_img = pygame.image.load('./Assets/Terreno/11.png')   # 11
        hud_meio_dir_img = pygame.image.load('./Assets/Terreno/12.png')    # 12
        hud_meio_meio_img = pygame.image.load('./Assets/Terreno/13.png')   # 13
        hud_meio_esq_img = pygame.image.load('./Assets/Terreno/14.png')    # 14
        hud_inf_dir_img = pygame.image.load('./Assets/Terreno/15.png')     # 15
        hud_inf_meio_img = pygame.image.load('./Assets/Terreno/16.png')    # 16
        hud_inf_esq_img = pygame.image.load('./Assets/Terreno/17.png')     # 17

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 0:
                    img = pygame.transform.scale(canto_dir_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 1:
                    img = pygame.transform.scale(meio_cima_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(canto_esq_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(meio_dir_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(meio_meio_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(meio_esq_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(inf_esq_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(inf_meio_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(inf_dir_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 9:
                    img = pygame.transform.scale(hud_canto_dir_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 10:
                    img = pygame.transform.scale(hud_meio_cima_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 11:
                    img = pygame.transform.scale(hud_canto_esq_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 12:
                    img = pygame.transform.scale(hud_meio_dir_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 13:
                    img = pygame.transform.scale(hud_meio_meio_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 14:
                    img = pygame.transform.scale(hud_meio_esq_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 15:
                    img = pygame.transform.scale(hud_inf_dir_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 16:
                    img = pygame.transform.scale(hud_inf_meio_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 17:
                    img = pygame.transform.scale(hud_inf_esq_img, (gl.SIZE, gl.SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gl.SIZE
                    img_rect.y = row_count * gl.SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 19:
                    mushroom = Enemy.Enemy(col_count * gl.SIZE, row_count * gl.SIZE)
                    gl.mushroom_group.add(mushroom)
                if tile == 20:
                    checkPoint = Exit.Exit(col_count * gl.SIZE, row_count * gl.SIZE + gl.SIZE)
                    gl.check_group.add(checkPoint)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            gl.screen.blit(tile[0], tile[1])
