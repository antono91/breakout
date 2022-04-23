import pygame
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
        self.bricks = [Brick(self, 70*i+j*35, 100*j)for i in range(1, 11) for j in range(1, 3)]

    def draw(self):
        self.win.fill(self.BG_COLOR)
        self.player.draw()
        self.ball.draw()
        for brick in self.bricks:
            brick.draw()
        pygame.display.update()
        self.clock.tick(self.FPS)
    
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
            for i ,brick in enumerate(self.bricks):
                if brick.collision_detection(): del self.bricks[i]
            self.draw()
            
        pygame.quit()
    
    def launch_ball(self):
        self.ball.sticky = False

