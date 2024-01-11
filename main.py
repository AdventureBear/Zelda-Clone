import pygame
import sys
import screen as s
import character as c

# Initialize Pygame
pygame.init()

# Set up the display
# screen_width = 800
# screen_height = 600
screen = pygame.display.set_mode((s.screen_width, s.screen_height))
pygame.display.set_caption("Zelda Clone")


# Map elements (for example, walls or trees)
wall_color = (139, 69, 19)  # Brown color for walls

# Dungeon walls with entrance and exit
wall_thickness = 20
entrance_width = 100

walls = [
    # Top wall
    pygame.Rect(0, 0, s.screen_width, wall_thickness),
    # Bottom wall
    pygame.Rect(0, s.screen_height - wall_thickness, s.screen_width, wall_thickness),
    # Left wall (with entrance gap)
    pygame.Rect(0, 0, wall_thickness, s.screen_height // 2 - entrance_width // 2),
    pygame.Rect(0, s.screen_height // 2 + entrance_width // 2, wall_thickness, s.screen_height // 2 - entrance_width // 2),
    # Right wall (with exit gap)
    pygame.Rect(s.screen_width - wall_thickness, 0, wall_thickness, s.screen_height // 2 - entrance_width // 2),
    pygame.Rect(s.screen_width - wall_thickness, s.screen_height // 2 + entrance_width // 2, wall_thickness, s.screen_height // 2 - entrance_width // 2),

    # Internal obstacles
    pygame.Rect(320, 100, 20, 400),  # Vertical obstacle
    pygame.Rect(320, 140, 20, 300),  # Another vertical obstacle
    # pygame.Rect(350, 300, 300, 20),  # Horizontal obstacle
]




#Collision Detection
def check_collision(rect, obstacles):
    for obstacle in obstacles:
        if rect.colliderect(obstacle):
            return True
    return False


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for pressed keys
    keys = pygame.key.get_pressed()

    # Movement logic with collision detection
    next_x = c.character_x
    next_y = c.character_y
    if keys[pygame.K_LEFT]:
        next_x -= c.character_speed
    if keys[pygame.K_RIGHT]:
        next_x += c.character_speed
    if keys[pygame.K_UP]:
        next_y -= c.character_speed
    if keys[pygame.K_DOWN]:
        next_y += c.character_speed

    # Create a rect for the next position and check for collisions
    next_rect = pygame.Rect(next_x, next_y, c.character_width, c.character_height)
    if not check_collision(next_rect, walls):
        c.character_x = next_x
        c.character_y = next_y
    else:
        print("Collision Detected")  # Debugging print

    # Fill the screen with a color
    screen.fill((0, 0, 0))  # Black background for now

    for wall in walls:
        pygame.draw.rect(screen, wall_color, wall)

    # Draw the character
    pygame.draw.rect(screen, c.character_color, (c.character_x, c.character_y, c.character_width, c.character_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
