import pygame

class Ball ():
    MAX_VEL = 5

    def __init__(self, game):
        self.game = game
        self.radius = 5
        self.pos_x = 0
        self.pos_y = 0
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, self.radius, self.radius)
        self.hitbox.center = self.pos_x, self.pos_y

        self.vel_x = 0
        self.vel_y = -5
        self.sticky = True

    def draw(self):
        self.hitbox.center = self.pos_x, self.pos_y
        pygame.draw.circle(self.game.win, "green",
                           (self.pos_x, self.pos_y), self.radius)

    def move(self):
        if self.sticky:
            self.pos_x = self.game.player.pos_x
            self.pos_y = self.game.player.pos_y - self.game.player.height//2 - self.radius
        else:
            # Collision with celing
            if self.pos_y - self.radius <= 0:
                self.vel_y *= -1
            # Collision with paddle
            if self.pos_x >= self.game.player.shape.topleft[0] and \
                    self.pos_x <= self.game.player.shape.topright[0] and \
                    (self.pos_y >= self.game.player.shape.topright[1] - self.radius + 1 and self.pos_y < self.game.player.shape.center[1]):
                self.vel_y *= -1
                difference_x = self.game.player.pos_x - self.pos_x
                reduction_factor = (self.game.player.width // 2) / self.MAX_VEL
                self.vel_x = -difference_x / reduction_factor

            # Collision with walls
            if self.pos_x - self.radius <= 0 or self.pos_x + self.radius >= self.game.WIDTH:
                self.vel_x *= -1

            self.pos_x += self.vel_x
            self.pos_y += self.vel_y