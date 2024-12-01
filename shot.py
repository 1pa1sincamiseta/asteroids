import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Shot(CircleShape):
    def __init__(self, position, direction):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOOT_SPEED

        
    def draw(self, screen):
        pygame.draw.circle(screen, "green", (self.position.x, self.position.y), self.radius, 1)
        
    def update(self, dt):
        self.position += self.velocity * dt