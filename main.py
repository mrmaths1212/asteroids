import pygame
from constants import *
from player import Player
from asteroid import Asteroid   
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    time = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updatables, drawables, asteroids)  
    AsteroidField.containers = (updatables)
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, drawables, updatables)
    asteroid_field = AsteroidField()
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    break
                # Handle collision (e.g., end game, reduce health, etc.)
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = time.tick (60) / 1000.0  # Convert milliseconds to seconds
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}", "\n" ,f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
