import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "purple", (self.position.x, self.position.y), self.radius, 2)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        random_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid1.velocity = velocity_1
        asteroid2.velocity = velocity_2
        
        Asteroid.containers[0].add(asteroid1)
        Asteroid.containers[0].add(asteroid2)
        
        