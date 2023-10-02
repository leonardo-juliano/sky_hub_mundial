import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos,groups,colision_group):
        super().__init__(groups)
        original_image = pygame.image.load("assets/player-225.png")
        scale_factor = 0.5
        self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))
        self.rect = self.image.get_rect()
        self.colision_group = colision_group
        self.speed=5
        self.jump_force = 18
        self.direction = pygame.math.Vector2()
        self.gravity =0.8

        self.on_ground = False

        # self.flip = False
        # self.tick = 0
        # self.frame = 0

    def move(self):
        self.rect.x += self.direction.x * self.speed

        if self.on_ground == False:
            original_image = pygame.image.load("assets/player-225.png")
            scale_factor = 0.5
            self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))
            #self.image = pygame.transform.flip(self.image, self.flip, False)


    def gravity_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.move()
        self.gravity_force()
        self.y_colision()

    def y_colision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y>0:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top
                    self.on_ground = True


    # def animation(self, speed, n_img, path):
    #      self.tick+=1
    #      if self.tick > speed:
    #          self.tick=0
    #          self.frame= (self.frame+1) % n_img
    #          self.image=pygame.image.load(
    #              path+str(self.frame)+".png")
    #          self.image = pygame.transform.flip(
    #              self.image, self.flip, False)

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.direction.x = -1
            # self.flip = True
            # self.animation(8, 3, "assets/player-225")
        elif key[pygame.K_d]:
            self.direction.x = 1
            # self.flip = False
            # self.animation(8, 3, "assets/player-225")
        else:
            self.direction.x = 0
            # self.animation(16, 2, "assets/player-225")

        if key[pygame.K_SPACE] and self.on_ground:
            self.direction.y=-self.jump_force
            self.on_ground = False