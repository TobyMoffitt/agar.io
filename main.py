import pygame
import sys
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color=color
        self.diameter=random.randint(20,60)
        self.image=pygame.Surface((self.diameter,self.diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color,(self.diameter/2,self.diameter/2),self.diameter/2)
        
        self.direction=0
        self.rect = self.image.get_rect(center=(x,y))
    def move(self):
        if self.direction==0:
            self.rect.centery+=(1+(300//self.diameter)/5)
        elif self.direction==1:
            self.rect.centerx+=(1+(300//self.diameter)/5)
        elif self.direction==2:
            self.rect.centery-=(1+(300//self.diameter)/5)
        elif self.direction==3:
            self.rect.centerx-=(1+(300//self.diameter)/5)

#        if self.rect.left<0:
#            self.rect.left=5
#        if self.rect.right>800:
#            self.rect.right=795
#        if self.rect.top<0:
#            self.rect.top=5
#        if self.rect.bottom>600:
#            self.rect.bottom=595

class Dot(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image=pygame.Surface((10,10), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x,y))
        pygame.draw.circle(self.image, color,(5,5),5)

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.diameter=20
        self.direction=1
        self.color=color
        self.image=pygame.Surface((self.diameter,self.diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color,(self.diameter/2,self.diameter/2),self.diameter/2)
        self.rect = self.image.get_rect(center=(x,y))
    def move(self):
        if b==1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dist=[self.rect.centerx-mouse_x, self.rect.centery-mouse_y]
            self.rect.centerx-=(dist[0]/self.diameter)
            self.rect.centery-=(dist[1]/self.diameter)
        else:
            if self.direction==0:
                self.rect.centery-=(1+(300//self.diameter)/5)
            elif self.direction==1:
                self.rect.centerx+=(1+(300//self.diameter)/5)
            elif self.direction==2:
                self.rect.centery+=(1+(300//self.diameter)/5)
            elif self.direction==3:
                self.rect.centerx-=(1+(300//self.diameter)/5)
# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agar.io")
b=1
# Create clock to later control frame rate
clock = pygame.time.Clock()

enemies=pygame.sprite.Group()
for i in range(6):
    enemies.add(Enemy(random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]), 100+100*i, 200))
    enemies.add(Enemy(random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]), 100+100*i, 400))
dots=pygame.sprite.Group()
for i in range(50):
    dots.add(Dot(random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]), random.randint(20,780), random.randint(20,580)))
players=pygame.sprite.Group()
player=Player("White", 50, 50)
players.add(player)
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False
    # Fill the screen with a color (e.g., white)
    screen.fill("Black")
    if random.randint(0,10)==10: dots.add(Dot(random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]), random.randint(0,800), random.randint(0,600)))
    if random.randint(0,100)==1: enemies.add(Enemy(random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]), random.randint(-100,900), random.randint(-100,700)))
    for dot in dots:
        if player.rect.colliderect(dot.rect):
            player.diameter+=2
            player.image=pygame.Surface((player.diameter,player.diameter), pygame.SRCALPHA)
            pygame.draw.circle(player.image, player.color,(player.diameter/2,player.diameter/2),player.diameter/2)
            player.rect = player.image.get_rect(center=(player.rect.center[0],player.rect.center[1]))
            dots.remove(dot)
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            if player.diameter>enemy.diameter:
                player.diameter+=enemy.diameter/5
                player.image=pygame.Surface((player.diameter,player.diameter), pygame.SRCALPHA)
                pygame.draw.circle(player.image, player.color,(player.diameter/2,player.diameter/2),player.diameter/2)
                player.rect = player.image.get_rect(center=(player.rect.center[0],player.rect.center[1]))
                enemies.remove(enemy)
                print(player.diameter)
            elif player.diameter<enemy.diameter:
                players.remove(player)
        for dot in dots:
            if enemy.rect.colliderect(dot.rect):
                enemy.diameter+=2
                enemy.image=pygame.Surface((enemy.diameter,enemy.diameter), pygame.SRCALPHA)
                pygame.draw.circle(enemy.image, enemy.color,(enemy.diameter/2,enemy.diameter/2),enemy.diameter/2)
                enemy.rect = enemy.image.get_rect(center=(enemy.rect.center[0],enemy.rect.center[1]))
                dots.remove(dot)
        for enemy2 in enemies:
            if enemy!=enemy2 and enemy.rect.colliderect(enemy2.rect):
                if enemy.diameter>enemy2.diameter:
                    enemy.diameter+=enemy2.diameter/5
                    enemy.image=pygame.Surface((enemy.diameter,enemy.diameter), pygame.SRCALPHA)
                    pygame.draw.circle(enemy.image, enemy.color,(enemy.diameter/2,enemy.diameter/2),enemy.diameter/2)
                    enemies.remove(enemy2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.direction=3
    if keys[pygame.K_RIGHT]:
        player.direction=1
    if keys[pygame.K_UP]:
        player.direction=0
    if keys[pygame.K_DOWN]:
        player.direction=2
    if keys[pygame.K_BACKSPACE]:
        b*=-1
    dots.draw(screen)
    enemies.draw(screen)
    players.draw(screen)
    for enemy in enemies:
        enemy.move()
        if random.randint(0,5)==5:
            enemy.direction=random.randint(0,3)
    for player in players:
        player.move()


    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
