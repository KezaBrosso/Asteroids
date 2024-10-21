# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

from constants import *

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

from shot import Shots



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shots.containers =(shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collision(player) == True:
               print("Game over!")
               sys.exit()
            for shot in shots:
                if item.collision(shot):
                    shot.kill()
                    item.split()
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
