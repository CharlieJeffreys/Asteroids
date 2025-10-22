import pygame
import constants as con
import player

def main():
    pygame.init()
    print("Starting Asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    ship = player.Player(x = con.SCREEN_WIDTH/2, y = con.SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
            updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()