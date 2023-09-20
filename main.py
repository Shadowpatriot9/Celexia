import pygame
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
BACKGROUND_COLOR = (0, 0, 0)
CELESTIAL_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbital Mechanics Simulator")

# Define a celestial body class
class CelestialBody:
    def __init__(self, x, y, radius, mass, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.velocity = velocity

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

# Create celestial bodies (e.g., Earth and Moon)
earth = CelestialBody(CENTER_X, CENTER_Y, 20, 500, [0, 0])
moon = CelestialBody(CENTER_X + 150, CENTER_Y, 5, 5, [0, -1])

# Main simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update celestial body positions
    earth.update()
    moon.update()

    # Draw the celestial bodies
    pygame.draw.circle(screen, CELESTIAL_COLOR, (int(earth.x), int(earth.y)), earth.radius)
    pygame.draw.circle(screen, CELESTIAL_COLOR, (int(moon.x), int(moon.y)), moon.radius)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.delay(10)

# Quit pygame
pygame.quit()
