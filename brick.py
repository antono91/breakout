import pygame

class Brick():
    def __init__(self, game, x, y):
        self.game = game
        self.width = 60
        self.height = 10
        self.pos_x = x
        self.pos_y = y
        self.shape = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.shape.center = (self.pos_x, self.pos_y)

    def draw(self):
        pygame.draw.rect(self.game.win, "purple", self.shape)
    
    def collision_detection(self):
        if self.shape.colliderect(self.game.ball.hitbox):
            self.game.ball.vel_y *= -1
            return True