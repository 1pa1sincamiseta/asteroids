import pygame
import sys
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# Here is when the game begins
	pygame.init()
 
	# Here is the setup for the player
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	
	# Here is the setup for asteroids
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
 
	# Here is the setup for shots
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	clock = pygame.time.Clock()
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
  
		for entity in updatable:
				entity.update(dt)

		for entity in drawable:
			entity.draw(screen)
   
		for asteroid in asteroids:
			if player.check_colission(asteroid):
				print("Game over!")
				sys.exit()
  
		for shot in shots:
			for asteroid in asteroids:
				if shot.check_colission(asteroid):
					shot.kill()
					asteroid.split()

		pygame.display.flip()

		dt = clock.tick(60) / 1000
		

if __name__ == "__main__":
    main()

