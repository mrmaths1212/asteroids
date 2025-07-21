from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, r):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.hit_centers = [
        pygame.Vector2(x, y),  # centre du gland
        pygame.Vector2(x, y + 3 * r),  # centre vertical du rectangle
        pygame.Vector2(x - r, y + 6 * r),
        pygame.Vector2(x + r, y + 6 * r)
        ]
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = r

    def collide(self, CircleShape):
        if not hasattr(CircleShape, "position") or not hasattr(CircleShape, "radius"):
            raise TypeError("Other object must have 'position' and 'radius' attributes")
    
        for center in self.hit_centers:
            if center.distance_to(CircleShape.position) <= (self.radius + CircleShape.radius):
                return True
        return False
    #def draw(self, screen):
    #    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def draw(self, screen):

    # Corps du "pénis" : un rectangle vertical
        shaft_rect = pygame.Rect(self.position[0] - self.radius, self.position[1], 2*self.radius, 6*self.radius)
        pygame.draw.rect(screen, (255, 255, 255), shaft_rect)

    # Deux cercles à la base (testicules)
        pygame.draw.circle(screen, (255, 255, 255), (self.position[0] - self.radius, self.position[1] + 6*self.radius), self.radius)
        pygame.draw.circle(screen, (255, 255, 255), (self.position[0] + self.radius, self.position[1] + 6*self.radius), self.radius)

    # Tête arrondie en haut
        pygame.draw.circle(screen, (255, 255, 255), (self.position[0], self.position[1]), self.radius)



    def update(self, dt):
        # Asteroids do not move or rotate in this example
        self.position += self.velocity * dt
        for center in self.hit_centers:
            center += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        a1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        a1.velocity = v1*1.2
        a2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        a2.velocity = v2*1.2