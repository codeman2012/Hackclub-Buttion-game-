from cmath import rect

import pygame
import random
import sys

pygame.init()

#screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Button Game")

#color
WHITE = (255, 255, 255)
Blue = (0,100,255)
Black = (0, 0, 0)

#font
font = pygame.font.Font(None, 40)

#Button settings
button_size = 80
buttion = pygame.Rect(
    random.randint(0, WIDTH - button_size),
    random.randint(0, HEIGHT - button_size),
    button_size,
    button_size

)
score=0
clock = pygame.time.Clock()
running = True

def draw_button(surface, react, hovered):
    #shadow
    shadow = react.move(4, 4) 
    pygame.draw.rect(surface, (0, 0, 0), shadow, border_radius=15)

    #color changes when hovered
    color = (0, 170, 255) if hovered else (0, 120, 230)

    #main buttion
    pygame.draw.rect(surface, color, react, border_radius=15)

    #shine hilight
    hilight = pygame.Rect(
        react.x + 5,
        react.y + 5,
        react.width - 10,
        react.height // 3
    )
    pygame.draw.rect(surface, (140, 220, 255), hilight, border_radius=10)

#game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttion.collidepoint(event.pos):
                score += 1

                #move the button
                buttion.x = random.randint(0, WIDTH - button_size)
                buttion.y = random.randint(0, HEIGHT - button_size)
    #draw
    screen.fill(WHITE)

    pygame.draw.rect(screen, Blue, buttion)
    score_text = font.render(f"Score: {score}", True, Black)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()