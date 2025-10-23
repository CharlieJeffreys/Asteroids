import pygame
import constants as con
import player
import asteroid
import asteroidfield

def main():
    pygame.init()
    print("Starting Asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable, )
    field = asteroidfield.AsteroidField()
    player.Player.containers = (updatable, drawable)
    ship = player.Player(x = con.SCREEN_WIDTH/2, y = con.SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for obj in asteroids:
            if obj.collision_check(ship):
                print("Collision detected!")
                raise SystemExit("Game over!")

        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()