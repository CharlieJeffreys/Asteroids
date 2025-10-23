import circleshape
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.center = (x,y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    