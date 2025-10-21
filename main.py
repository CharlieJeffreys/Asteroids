import pygame
import constants as con

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
