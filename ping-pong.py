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
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed

            



        



# kastryla = PlayerSprite('kastryla.png', 570, 420, 5, 80, 60)





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

    display.update()
    clock.tick(FPS)
