import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Get the screen width and height
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# Constants
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BACKGROUND_COLOR = BLACK
POINT_COLOR = (255, 0, 0)
CURVE_COLOR = (0, 0, 255)
TEXT_COLOR = WHITE
FONT_SIZE = 30

# Initialize window with screen width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Bézier Curve Fitting")

# Create a font for displaying text
font = pygame.font.Font(None, FONT_SIZE)

# List to store control points
control_points = []

# formula from https://en.wikipedia.org/wiki/B%C3%A9zier_curve and 
# https://math.stackexchange.com/questions/26846/is-there-an-explicit-form-for-cubic-b%C3%A9zier-curves

def cubic_bezier(t, control_points):
    P0, P1, P2, P3 = control_points
    x = (1 - t) ** 3 * P0[0] + 3 * (1 - t) ** 2 * t * P1[0] + 3 * (1 - t) * t**2 * P2[0] + t**3 * P3[0]
    y = (1 - t) ** 3 * P0[1] + 3 * (1 - t) ** 2 * t * P1[1] + 3 * (1 - t) * t**2 * P2[1] + t**3 * P3[1]
    return x, y

def generate_polynomial_equation(control_points):
    P0, P1, P2, P3 = control_points
    x_term = f"(1 - t)^3 * {P0[0]} + 3 * (1 - t)^2 * t * {P1[0]} + 3 * (1 - t) * t^2 * {P2[0]} + t^3 * {P3[0]}"
    y_term = f"(1 - t)^3 * {P0[1]} + 3 * (1 - t)^2 * t * {P1[1]} + 3 * (1 - t) * t^2 * {P2[1]} + t^3 * {P3[1]}"
    return x_term, y_term

def display_polynomial_info(polynomial, position):
    text = font.render("Polynomial: " + polynomial, True, TEXT_COLOR)
    screen.blit(text, position)

running = True
drawing = True
draw_curve = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # mouse position from https://stackoverflow.com/questions/66349281/pygame-function-to-draw-a-line-between-two-points-is-not-working
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button
            if event.button == 1 and drawing:  
                control_points.append(event.pos)
                # Select four control points
                if len(control_points) == 4: 
                    drawing = False
                    draw_curve = True
        
        # Check for the 'r' key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            control_points = []
            drawing = True
            draw_curve = False
            BACKGROUND_COLOR = BLACK
            TEXT_COLOR = WHITE

        if keys[pygame.K_w]:
            BACKGROUND_COLOR = WHITE
            TEXT_COLOR = BLACK
        
        # Check for the 'q' key press to quit
        if keys[pygame.K_q]:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    # Draw control points
    for point in control_points:
        pygame.draw.circle(screen, POINT_COLOR, point, 5)

    if draw_curve:
        t_values = np.linspace(0, 1, 1000)
        x_values = [cubic_bezier(t, control_points)[0] for t in t_values]
        y_values = [cubic_bezier(t, control_points)[1] for t in t_values]
        # Curve drawing
        # Connect points with lines from https://lorenzod8n.wordpress.com/2007/05/27/pygame-tutorial-2-drawing-lines/
        pygame.draw.lines(screen, CURVE_COLOR, False, list(zip(x_values, y_values)), 5)
        
        # Calculate and display the polynomial equation
        polynomial = generate_polynomial_equation(control_points)

        # print(f"x(t) = {polynomial[0]}")
        # print(f"y(t) = {polynomial[1]}")

        display_polynomial_info("x(t)= " + polynomial[0], (10, 10))
        display_polynomial_info("y(t)= " + polynomial[1], (10, 50))
        display_polynomial_info("Points:" + str(control_points) , (10,90))

    pygame.display.flip()

pygame.quit()
