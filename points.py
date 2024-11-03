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


my_list = [(0.0, 0.0),(1.495, 1.4140000000000001),(2.9600000000000004, 2.6720000000000006),(4.364999999999999, 3.797999999999999),(5.68, 4.816000000000001),(6.875, 5.75),(7.92, 6.6240000000000006),(8.785, 7.462),(9.44, 8.288),(9.855, 9.126000000000001),(10.0, 10.0)]

print(len(my_list))