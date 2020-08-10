import pygame,sys
import random




from pygame.locals import (
    RLEACCEL,K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT
)

sw = 800
sh = 600
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.image.load("bat.png").convert()
        self.surf = pygame.transform.scale(self.surf,(40,60))
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > sw:
            self.rect.right = sw
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > sh:
            self.rect.bottom = sh

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.image.load("ball.png").convert()
        self.surf = pygame.transform.scale(self.surf,(40,60))
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(sw + 20, sw + 100),
                random.randint(0, sh),
            )
        )
        self.speed = random.randint(5,20)
        
        
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

class Ref(pygame.sprite.Sprite):
     
    def __init__(self):
        super(Ref,self).__init__()
        self.surf = pygame.image.load("ref.png").convert()
        self.surf = pygame.transform.scale(self.surf,(40,60))
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(sw+ 20, sw + 100),
                random.randint(0, sh),
            )
        )
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right < 0:
            self.kill()


pygame.init()   

screen = pygame.display.set_mode([sw,sh])

player = Player()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,250)
ADDREF = pygame.USEREVENT + 2
pygame.time.set_timer(ADDREF,1000)

enemies = pygame.sprite.Group()
refs = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

background = pygame.image.load("grass.jpg").convert()
background = pygame.transform.scale(background,(sw,sh))
running  = True
pygame.font.init()
text = pygame.font.SysFont('Comic Sans MS', 30)
score = 0
while running:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
                
        elif event.type == ADDENEMY:

            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            
        elif event.type == ADDREF:
            new_ref  = Ref()
            refs.add(new_ref)
            all_sprites.add(new_ref)
        
    textSurf = text.render("Score:",score, (0,0,0))
    pressed_keys = pygame.key.get_pressed()
    screen.fill([0,0,0])
    enemies.update()  
    refs.update()   
    player.update(pressed_keys)
 

    screen.blit(background,[0,0])   
    screen.blit(textSurf,[0,0])
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)
 
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        running = False
    else:
        score +=1
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
