from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,weight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(weight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))






class Robot(GameSprite):
    direction_y = 'up'
    def update(self):
        borderTOP_y = 5
        borderDOWN_y = 325

        if borderDOWN_y <= self.rect.y:
            self.direction_y = 'up'
        if  borderTOP_y >= self.rect.y:
            self.direction_y = 'down'
        if self.direction_y == 'up':
            self.rect.y -= 3
        if self.direction_y == 'down':
            self.rect.y +=3



class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 1:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += 5    







window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
racket_main = Player('Computer.png',25, 220, 1, 20,150)
racket_AI = Robot('Player.png',660, 220, 1, 20,150)
ball_1 = GameSprite('Ball.png', 600, 220, 1, 40, 40)

font.init()
font = font.Font(None,70)
win = font.render('YOU ARE WIN', True, (255, 215, 0))
lost = font.render('YOU ARE LOSE', True, (255, 215, 0))


speed_x = 5
speed_y = 5
FPS = 60
clock = time.Clock()
finish = False
game = True
while game:
    for x in event.get():
        if x.type == QUIT:
            game = False
    if finish != True:
        window.fill((0, 255, 255))
        racket_main.reset()
        racket_AI.reset()
        racket_main.update()
        racket_AI.update()
        ball_1.rect.y += speed_y
        ball_1.rect.x += speed_x
        ball_1.reset()

        if sprite.collide_rect(ball_1,racket_AI) or sprite.collide_rect(ball_1, racket_main):
            speed_x *=-1
        if ball_1.rect.y >= 460:
            speed_y *=-1
        if  ball_1.rect.y <= 0:
            speed_y *=-1
        if ball_1.rect.x>=660:
            window.blit(win,(200, 50))
            finish = True
        if ball_1.rect.x<=0:
            window.blit(lost,(200,50))
            finish = True

        



    clock.tick(FPS)
    display.update()
