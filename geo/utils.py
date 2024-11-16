def calculate_area(shape, **dimensions):
    """
    Calculate the area of different shapes.
    :param shape: Type of shape (e.g., 'circle', 'rectangle', 'triangle')
    :param dimensions: Keyword arguments for shape dimensions
    :return: Area of the shape
    """
    if shape == "circle":
        radius = dimensions.get("radius", 0)
        return 3.14159 * radius**2
    elif shape == "rectangle":
        width = dimensions.get("width", 0)
        height = dimensions.get("height", 0)
        return width * height
    elif shape == "triangle":
        base = dimensions.get("base", 0)
        height = dimensions.get("height", 0)
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape!")
