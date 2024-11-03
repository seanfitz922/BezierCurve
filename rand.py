import random

# Set to store unique points
points = set()

# Generate unique points until the set has 500 elements
while len(points) < 10000:
    # Generate random x and y coordinates
    x = random.randint(0, 100_000)
    y = random.randint(0, 100_000)
    # Add the point as a tuple to the set
    points.add((x, y))

