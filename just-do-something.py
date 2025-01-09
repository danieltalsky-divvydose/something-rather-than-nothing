def sierpinski_triangle(order, size):
    """
    Generate the Sierpinski triangle of a given order.

    A Sierpinski triangle is a self-similar fractal shape created by repeatedly removing 
    the central smaller equilateral triangle from a larger equilateral triangle, resulting 
    in a pattern of smaller triangles that repeat at different scales within the overall 
    triangular shape; it's named after the Polish mathematician Wacław Sierpiński 
    who first described it mathematically.

    Parameters:
    order (int): The order of the Sierpinski triangle.
    size (int): The size of the triangle.

    Returns:
    list: A list of strings representing the Sierpinski triangle.
    """
    if order == 0:
        return ["*"]
    else:
        prev_order = sierpinski_triangle(order - 1, size // 2)
        top = [line + " " * size + line for line in prev_order]
        bottom = [line * 2 for line in prev_order]
        return top + bottom

def print_sierpinski(order):
    """
    Print the Sierpinski triangle of a given order.

    Parameters:
    order (int): The order of the Sierpinski triangle.
    """
    size = 2 ** order
    triangle = sierpinski_triangle(order, size)
    for line in triangle:
        print(line.center(size * 2))

if __name__ == "__main__":
    order = 5  # Adjust this number for more or fewer iterations
    print_sierpinski(order)