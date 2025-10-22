import pygame
import constants as con
import player

def main():
    pygame.init()
    print("Starting Asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    ship = player.Player(x = con.SCREEN_WIDTH/2, y = con.SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        ship.draw(screen)
        ship.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
