import pygame
import Globals as gl


class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over, world):
        delta_x = 0
        delta_y = 0
        walk_cooldown = 1

        if gl.game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                gl.jump_sound.play()
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                delta_x -= 10
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                delta_x += 10
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            delta_y += self.vel_y

            # check for collision
            self.in_air = True
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + delta_x, self.rect.y, self.width, self.height):
                    delta_x = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + delta_y, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        delta_y = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        delta_y = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # check for collision with enemies
                if pygame.sprite.spritecollide(self, gl.mushroom_group, False):
                    gl.game_over = -1

            # check for collision with exit
                if pygame.sprite.spritecollide(self, gl.check_group, False):
                    gl.game_over = 3

            # update player coordinates
            self.rect.x += delta_x
            self.rect.y += delta_y

        elif gl.game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5

        # draw player onto screen
        gl.screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return gl.game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 14):
            img_right = pygame.image.load('./Assets/Froggy/Froggy_{}.png'.format(num))
            img_right = pygame.transform.scale(img_right, (gl.SIZE, gl.SIZE))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('./Assets/Froggy/Dead_Froggy.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True