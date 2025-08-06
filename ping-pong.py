from pygame import *
from random import *



clock = time.Clock()
FPS = 60
#создай окно игры
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, palyer_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = palyer_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class PlayerSprite(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 355:
            self.rect.y += self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 355:
            self.rect.y += self.speed


            



        



raketka1 = PlayerSprite('raketka.png', 600, 350, 5, 80, 150)
raketka2 = PlayerSprite('raketka.png', 30, 350, 5, 80, 150)
ball = GameSprite('ball.png',350,250,5,50,50)
speedx = 5
speedy = 5



window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("grass.jpg"), (700, 500))

game = True
finish = False


font.init()
font1 = font.SysFont("Arial", 70)
win = font1.render('YOU WIN!', True,(0,255,0))
lose = font1.render("YOU LOSE!", True,(255,0,0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        raketka1.update()
        raketka1.reset()
        raketka2.update1()
        raketka2.reset()
        ball.rect.x += speedx 
        ball.rect.y += speedy
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            speedy *= -1
        if sprite.collide_rect(raketka1, ball) or sprite.collide_rect(raketka2, ball):
            speedx *= -1

        ball.reset()
    display.update()
    clock.tick(FPS)
