import pygame


class Paddle():
    def __init__(self, game):
        self.width = 100
        self.height = 20
        self.game = game
        self.pos_x = self.game.WIDTH // 2
        self.pos_y = self.game.HEIGHT - 20
        self.shape = pygame.Rect(
            self.pos_x, self.pos_y, self.width, self.height)
        self.shape.center = (self.pos_x, self.pos_y)

    def draw(self):
        pygame.draw.rect(self.game.win, "red", self.shape)

    def move(self, pos_x):
        if self.width // 2 < pos_x <= self.game.WIDTH - self.width // 2:
            self.pos_x = pos_x
        self.shape.center = (self.pos_x, self.pos_y)


