import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)

            a1 = Asteroid(self.position.x, self.position.y, radius)
            a1.velocity = self.velocity.rotate(angle) * 1.2

            a2 = Asteroid(self.position.x, self.position.y, radius)
            a2.velocity = self.velocity.rotate(-angle) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt