# Daniela Paez Rodriguez
# 2022-05-24
# Pac Man that eats cherries and makes sound

import pygame,os,random
from pygame import mixer
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("PacMan")
clock = pygame.time.Clock()

mixer.init()
mixer.music.load('Pacman-sound.mp3')
mixer.music.set_volume(0.7)




class renwu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.master_image = pygame.image.load('pukis.png').convert_alpha()  #  Import a character animation full image
        self.rect=self.master_image.get_rect()
        self.frame_width=self.rect.width//8  #The entire image is layered 8 lines - the width of each picture
        self.frame_height =self.rect.height//8  #8 columns of the entire image - is high for each picture
        self.image = self.master_image.subsurface((0,2*self.frame_height,self.frame_width,self.frame_height))
        #The initial movement to the right -2 line 0 column
        #Per frame screen
        self.mask=pygame.mask.from_surface(self.image)
        self.x=0   #X-axis per move amount
        self.y = 0  #  Y-axis per move
        self.han = 2  #  Record line
        self.lie = 0  #  Record columns
        self.li=0   #Column offset

    def update(self):  #  Update function
        self.rect.x =self.rect.x+self.x
        self.rect.y = self.rect.y + self.y
        #Update people coordinates
        if self.rect.x<0 :
            self.rect.x=639
        if self.rect.x>640:
            self.rect.x = -2
        #Prevent people from walking out of the screen
        self.lie+=self.li
        if self.lie>7:
            self.lie=0
        self.image = self.master_image.subsurface((self.lie*self.frame_width, self.han * self.frame_height, self.frame_width, self.frame_height))


class pinguo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('cherryOne.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
p_zu = pygame.sprite.Group()
r_zu=pygame.sprite.Group()      #Character group
for i in range(0,10):
    p=pinguo()
    p.rect.x=random.randint(0,640)
    p.rect.y = random.randint(80, 400)
    p_zu.add(p)

r=renwu()
r_zu.add(r)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  #  If you press the up key
                r.han=0  #Row
                r.y=-5
                r.li=1
            if event.key == pygame.K_LEFT:  #  If you press the left button
                r.han=6   #The sixth line to the left
                r.x=-5
                r.li = 1
            if event.key == pygame.K_DOWN:  #  If you press the down button
                r.han=4  #Chain 4
                r.y=5
                r.li = 1
            if event.key == pygame.K_RIGHT:  #  If you press it right click
                r.han=2  #Chain 2
                r.x=5
                r.li = 1
        elif event.type == pygame.KEYUP:  #  If there is a keyboard release
            if event.key == pygame.K_UP:  #  If released, it is up
                r.y=0
                r.li = 0
            if event.key == pygame.K_LEFT:  #  If released to the left button
                r.x=0
                r.li = 0
            if event.key == pygame.K_DOWN:  #  If released, the down button is
                r.y = 0
                r.li = 0
            if event.key == pygame.K_RIGHT:  #  If released, right-click
                r.x = 0
                r.li = 0


    b = pygame.sprite.spritecollide(r, p_zu, True, pygame.sprite.collide_mask)  #  Elf and group accurate collision detection
    if b:
        mixer.music.play()
    screen.fill((255,255,255))
    r_zu.update()  #  Update function for performing character wizard
    p_zu.draw(screen)
    r_zu.draw(screen)
    clock.tick(30)
    pygame.display.update()
