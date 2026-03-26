
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,PLAYER_TURN_SPEED
from logger import log_event, log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    my_clock_variable = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Step 4: The Game Loop
    dt = 0
    while True: 
        log_state()
        dt = my_clock_variable.tick(60) / 1000 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return 
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                   log_event("asteroid_shot")
                   shot.kill()
                   asteroid.split()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen) 

        pygame.display.flip()      



if __name__ == "__main__":
    main()
  
