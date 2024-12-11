from pygame import *

img_racket = "C:/Users/HP/Downloads/racket.png"
img_ball = "C:/Users/HP/Downloads/tenis_ball.png"

BACKGROUND_COLOR = (200, 255, 255)
width, height = 600, 500
window = display.set_mode((width, height))
window.fill(BACKGROUND_COLOR)
display.set_caption("Ping Pong")

clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
 #class constructor
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #call for the class (Sprite) constructor:
       sprite.Sprite.__init__(self)


       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #every sprite must have the rect property that represents the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #method drawing the character on the window
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
   
   def fill(self):
       draw.rect(window, BACKGROUND_COLOR, self.rect)


#main player class
class Player(GameSprite):
   #method to control the sprite with arrow keys
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < height - 80:
           self.rect.y += self.speed

   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < height - 80:
           self.rect.y += self.speed

paddl_1 = Player(img_racket, 30, 200, 50, 150, 4)
paddl_2 = Player(img_racket, 530, 200, 50, 150, 4)
ball = GameSprite(img_ball, 200, 200, 50, 50, 4)

speed_x = 3
speed_y = 3

font.init()
font_1 = font.SysFont("Times", 30)

lose_1 = font_1.render("Player 1, You lost!", True, (215, 0, 64))
lose_2 = font_1.render("Player 2, You lost!", True, (215, 0, 64))

run = True
finish = False
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        paddl_1.fill()
        paddl_2.fill()
        ball.fill()

        paddl_1.update_l()
        paddl_2.update_r()
        ball.rect.x += speed_x   
        ball.rect.y += speed_y

        if ball.rect.y > height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, paddl_1) or sprite.collide_rect(ball, paddl_2):
            speed_x *= -1

        if ball.rect.x < 0:
            window.blit(lose_1, (200, 200))
            finish = True

        if ball.rect.x > width-50:
            window.blit(lose_2, (200, 200))
            finish = True

        
        paddl_1.reset()
        paddl_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
