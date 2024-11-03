import pygame
import numpy as np
import sys


# Initialize Pygame and set up constants
pygame.init()

# Get the screen width and height
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h


# Colors and other constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = WHITE
POINT_COLOR = (255, 0, 0)
CURVE_COLOR = (0, 0, 255)
TEXT_COLOR = BLACK
FONT_SIZE = 37
ANIMATION_SPEED = 0.003  # Controls the curve drawing speed

# Load and scale background image
background_image = pygame.image.load("grid.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Font for displaying text
font = pygame.font.Font(None, FONT_SIZE)

# Control points list
control_points = []

# De Casteljau's algorithm (https://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm)
def de_casteljau(t, control_points):
    n = len(control_points)
    points = control_points.copy()
    for r in range(1, n):
        for i in range(n - r):
            points[i] = ((1 - t) * points[i][0] + t * points[i + 1][0],
                         (1 - t) * points[i][1] + t * points[i + 1][1])
    return points[0]

# Generates polynomial equations (https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
def generate_polynomial_equation(control_points):
    P0, P1, P2, P3 = control_points
    x_term = f"(1 - t)^3 * {P0[0]} + 3 * (1 - t)^2 * t * {P1[0]} + 3 * (1 - t) * t^2 * {P2[0]} + t^3 * {P3[0]}"
    y_term = f"(1 - t)^3 * {P0[1]} + 3 * (1 - t)^2 * t * {P1[1]} + 3 * (1 - t) * t^2 * {P2[1]} + t^3 * {P3[1]}"
    print(x_term)
    print(y_term)
    return x_term, y_term

# Display polynomial information
def display_polynomial_info(polynomial, position):
    text = font.render("Polynomial: " + polynomial, True, TEXT_COLOR)
    screen.blit(text, position)

# Main loop function
def main(gui_points = []):
    global control_points, screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    manual_mode = False

    if len(gui_points) > 0:
        control_points = gui_points
        manual_mode = True

    pygame.display.set_caption("Bézier Curve Fitting")
    
    # Main loop variables
    running = True
    drawing = True
    draw_curve = False
    t_current = 0  # Animation parameter

    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                    running = False

            elif not manual_mode:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and drawing:
                        control_points.append(event.pos)
                        if len(control_points) == 4:
                            drawing = False
                            draw_curve = True
                            t_current = 0
                
                if keys[pygame.K_r]:
                    control_points = []
                    drawing = True
                    draw_curve = False
                    t_current = 0

            else: draw_curve = True
        # Draw background, points, and curve
        screen.blit(background_image, (0, 0))
        for point in control_points:
            pygame.draw.circle(screen, POINT_COLOR, point, 10)
        
        if draw_curve:
            if t_current <= 1:
                t_current += ANIMATION_SPEED
            t_values = np.linspace(0, t_current, int(t_current * 1000))
            x_values = [de_casteljau(t, control_points)[0] for t in t_values]
            y_values = [de_casteljau(t, control_points)[1] for t in t_values]
            if len(x_values) > 1:
                pygame.draw.lines(screen, CURVE_COLOR, False, list(zip(x_values, y_values)), 8)

            polynomial = generate_polynomial_equation(control_points)
            display_polynomial_info("x(t)= " + polynomial[0], (10, 10))
            display_polynomial_info("y(t)= " + polynomial[1], (10, 50))
            display_polynomial_info("Points: " + str(control_points), (10, 90))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()
