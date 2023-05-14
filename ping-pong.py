from pygame import *

font.init()
class Player():
    def __init__(self, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 10, 70)
        self.score = 0
    def updateP1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
        draw.rect(window, (0,0,0), self.rect)
    def updateP2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
        draw.rect(window, (0,0,0), self.rect)


class Ball():
    def __init__(self, x, y, speed):
        self.speed_x = speed
        self.speed_y = speed
        self.rect = Rect(x, y, 20, 20)
    def update(self):
        draw.rect(window, (0,0,0), self.rect)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > 780 or self.rect.x < 0:
            self.speed_x *= -1
            if self.rect.x > 780:
                player1.score += 1
            else:
                player2.score += 1
        if self.rect.y > 480 or self.rect.y < 0:
            self.speed_y *= -1




win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))


player1 = Player(30, 100, 5)
player2 = Player(win_width - 30, 100, 5)
ball = Ball(390, 240, 10)


game = True
finish = False
while game:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish:
                finish = False
                player1.score = 0
                player2.score = 0
                ball.rect.x = 390
                ball.rect.y = 240
                player1.rect.y = 230
                player2.rect.y = 230
                 
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill((79, 89, 105))
        player1.updateP1()
        player2.updateP2()
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x *= -1
        ball.update()
        score_text = font.Font(None, 80).render(f'{player1.score} : {player2.score}', True, (0,0,0))
        window.blit(score_text,(350,20))
        if player1.score == 3 or player2.score == 3:
            finish = True
        display.update()
        time.delay(30)