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
BLACK = (0, 0, 0)
BACKGROUND_COLOR = WHITE
POINT_COLOR = (255, 0, 0)
CURVE_COLOR = (0, 0, 255)
TEXT_COLOR = BLACK
FONT_SIZE = 37
ANIMATION_SPEED = 0.003  # Control how fast the curve is drawn

# Initialize window with screen width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Bézier Curve Fitting")

background_image = pygame.image.load("grid.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Create a font for displaying text
font = pygame.font.Font(None, FONT_SIZE)

# List to store control points
control_points = []

# De Casteljau's algorithm to calculate a point on the Bézier curve
# straight from wikipedia, https://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm
def de_casteljau(t, control_points):
    n = len(control_points)
    points = control_points.copy()  # Make a copy of control points

    # Perform De Casteljau's algorithm
    for r in range(1, n):
        for i in range(n - r):
            points[i] = ((1 - t) * points[i][0] + t * points[i + 1][0],
                         (1 - t) * points[i][1] + t * points[i + 1][1])

    return points[0]  # The first point is the result

# formula from https://en.wikipedia.org/wiki/B%C3%A9zier_curve and 
# https://math.stackexchange.com/questions/26846/is-there-an-explicit-form-for-cubic-b%C3%A9zier-curves
def generate_polynomial_equation(control_points):
    P0, P1, P2, P3 = control_points
    x_term = f"(1 - t)^3 * {P0[0]} + 3 * (1 - t)^2 * t * {P1[0]} + 3 * (1 - t) * t^2 * {P2[0]} + t^3 * {P3[0]}"
    y_term = f"(1 - t)^3 * {P0[1]} + 3 * (1 - t)^2 * t * {P1[1]} + 3 * (1 - t) * t^2 * {P2[1]} + t^3 * {P3[1]}"
    return x_term, y_term

# Function to display polynomial information on the screen
def display_polynomial_info(polynomial, position):
    text = font.render("Polynomial: " + polynomial, True, TEXT_COLOR)
    screen.blit(text, position)

# Main loop variables
running = True
drawing = True
draw_curve = False
# for animating curve
t_current = 0  

# Main Pygame loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # mouse position from https://stackoverflow.com/questions/66349281/pygame-function-to-draw-a-line-between-two-points-is-not-working
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and drawing:  
                control_points.append(event.pos)
                # Select four control points
                if len(control_points) == 4: 
                    drawing = False
                    draw_curve = True
                    t_current = 0  # Reset animation

        # Check for the 'r' key press to reset
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            control_points = []
            drawing = True
            draw_curve = False
            t_current = 0

        # Check for the 'q' key press to quit
        if keys[pygame.K_q]:
            running = False
            pygame.quit()
            sys.exit()

    # Fill screen with the background color
    screen.blit(background_image, (0, 0))

    # Draw control points
    for point in control_points:
        pygame.draw.circle(screen, POINT_COLOR, point, 10)

    # Draw the curve gradually using De Casteljau's algorithm
    if draw_curve:
        if t_current <= 1:
            # https://stackoverflow.com/questions/28074461/animating-growing-line-plot
            t_current += ANIMATION_SPEED  # Gradually increase t
        control_points = [(0,0) , (500,500), (1000,700), (1000,1000)]
        t_values = np.linspace(0, t_current, int(t_current * 1000))
        x_values = [de_casteljau(t, control_points)[0] for t in t_values]
        y_values = [de_casteljau(t, control_points)[1] for t in t_values]

        # Draw the curve incrementally
        if len(x_values) > 1:
            pygame.draw.lines(screen, CURVE_COLOR, False, list(zip(x_values, y_values)), 8)
        
        # Calculate and display the polynomial equation
        polynomial = generate_polynomial_equation(control_points)
        display_polynomial_info("x(t)= " + polynomial[0], (10, 10))
        display_polynomial_info("y(t)= " + polynomial[1], (10, 50))
        display_polynomial_info("Points: " + str(control_points), (10, 90))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
