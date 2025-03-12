def classify_triangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a valid triangle"
    sides = sorted([a, b, c])
    a, b, c = sides
    if a + b <= c:
        return "Not a valid triangle"
    if a == b == c:
        return "equilateral"
    epsilon = 1e-7
    is_right = abs(a**2 + b**2 - c**2) < epsilon

    if a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    if is_right:
        triangle_type += " right triangle"
    return triangle_type
