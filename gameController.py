import pygame
from pyrsistent import b
from paddle import Paddle
from ball import Ball
from brick import Brick

class GameController():
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 500
        self.BG_COLOR = (255,255,255)
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.running = True

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.player = Paddle(self)
        self.ball = Ball(self)
        self.bricks = self.create_bricks()
        self.lives = 3


    def create_bricks(self):
        bricks = []
        for row in range(1, 6):
            for col in range(1, 14):
                if row % 2:
                    bricks.append(Brick(self, 55*col+25, 100 + 20*row))
                else:
                    bricks.append(Brick(self, 55*col, 100 + 20*row))
        return bricks

    def draw(self):
        self.win.fill(self.BG_COLOR)
        self.player.draw()
        self.ball.draw()
        for brick in self.bricks:
            brick.draw()
        lives_text = pygame.font.SysFont("Monaco", 20).render(f"Lives: {self.lives}", False, (0,0,0))
        self.win.blit(lives_text, (20, 20))

        pygame.display.update()
        self.clock.tick(self.FPS)

    def handle_lose_lives(self):
        if self.ball.pos_y > self.player.shape.bottom:
            self.lives -= 1
            if self.lives <= 0:
                self.restart()
            else:
                self.ball.sticky = True
    
    def restart(self):
        self.ball.sticky = True
        self.player.center = self.WIDTH // 2, self.HEIGHT - 20
        self.bricks = [Brick(self, 55*i, 100 + 20*j)for i in range(1, 14) for j in range(1, 6)]
        self.lives = 3

    def handle_bricks(self):
        for i ,brick in enumerate(self.bricks):
            if brick.collision_detection(): del self.bricks[i]

    def game_loop(self):
        while self.running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.launch_ball()

                pos_x, _ = pygame.mouse.get_pos()
                self.player.move(pos_x)
            
            self.ball.move()
            self.handle_lose_lives()
            self.handle_bricks()

            self.draw()
            
        pygame.quit()
    
    def launch_ball(self):
        self.ball.sticky = False

