#Создай собственный Шутер!

from pygame import *

from time import time as tm

#создай окно 
window = display.set_mode((700, 450))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('forest.jpg'), (700, 450))

game = True
clock = time.Clock()
FPS = 60
points = 0

mixer.init()
font.init()

font1 = font.SysFont('Arial', 70)
font2 = font.SysFont('Arial', 30)
win = font1.render('p1 won!', True, (255, 0, 0))
lose = font1.render('p2 won!', True, (0, 0, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 365:
            self.rect.y += self.speed 

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 355:
            self.rect.y += self.speed  

player_l = Player('log.png', 45, 370, 10, 45, 75)
player_r = Player('log.png', 605, 370, 10, 45, 75)

finish = False

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player_l.reset()
        player_r.reset()
        player_l.update_l()
        player_r.update_r()

    display.update()
    clock.tick(FPS)
