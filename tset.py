def de_casteljau(t, control_points):
    n = len(control_points)
    points = control_points.copy()  # Make a copy of control points

    # Perform De Casteljau's algorithm
    for r in range(1, n):
        for i in range(n - r):
            points[i] = ((1 - t) * points[i][0] + t * points[i + 1][0],
                         (1 - t) * points[i][1] + t * points[i + 1][1])
            print(points)

    return points[0]  # The first point is the result

def compute_bezier_curve(control_points, steps=10):
    curve_points = []
    for t in [i / steps for i in range(steps + 1)]:
        point = de_casteljau(t, control_points)
        curve_points.append(point)
    return curve_points

# Control points: P1, P2, P3, P4
control_points = [(0, 0), (5, 5), (10, 7), (10, 10)]

# Compute the points on the Bézier curve
bezier_points = compute_bezier_curve(control_points, steps=10)

# Print the computed points
for i, point in enumerate(bezier_points):
    print(f"{point},",end='')
