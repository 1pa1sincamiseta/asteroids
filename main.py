import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
	print("Stating asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Scren height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	clock = pygame.time.Clock()
	dt = 0
 
	player.draw(screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
  
		player.draw(screen)
		
		pygame.display.flip()

		dt = clock.tick(60) / 1000
		

if __name__ == "__main__":
    main()

