from boid import Boid
import pygame
WIDTH, HEIGHT, = 900, 900

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIS")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
screen.blit(background, (0,0))
pygame.display.flip()
clock = pygame.time.Clock()

def drawBoid(boid):
    background.fill((250, 250, 250))
    screen.blit(background, (0,0))
    for b in boid.getBirds():
        pygame.draw.circle(screen, (127,0,0), b.getPixelPos(), 5)
        pygame.draw.line(screen, (255,0,0), b.getPixelPos(), [b.getPixelPos()[0] + b.dir[0]*15, b.getPixelPos()[1] + b.dir[1]*15], 2)
    pygame.display.flip()

boid = Boid(100, WIDTH, HEIGHT, screen)


while 1:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    drawBoid(boid)
    boid.step(5)
