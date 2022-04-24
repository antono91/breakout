import pygame

class Brick():
    def __init__(self, game, x, y):
        self.game = game
        self.width = 50
        self.height = 15
        self.pos_x = x
        self.pos_y = y
        self.hits = 2
        self.shape = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.shape.center = (self.pos_x, self.pos_y)

    def draw(self):
        pygame.draw.rect(self.game.win, "purple", self.shape)
    
    def collision_detection(self):
        if self.shape.colliderect(self.game.ball.hitbox):
            self.game.ball.vel_y *= -1
            self.hits -= 1
        return self.hits < 0