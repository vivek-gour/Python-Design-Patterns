import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Pygame Example")

# Define colors
RED = (255, 0, 0)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a red rectangle
    pygame.draw.rect(screen, RED, (100, 100, 200, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
