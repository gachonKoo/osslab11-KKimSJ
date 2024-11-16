# 유틸리티 함수 정의
def calculate_area(shape, **kwargs):
    """
    Calculate the area of different shapes.
    :param shape: Type of shape ('circle', 'square', 'rectangle')
    :param kwargs: Additional parameters like radius, length, breadth
    :return: Area of the shape
    """
    if shape == 'circle':
        radius = kwargs.get('radius', 0)
        return 3.14159 * radius ** 2
    elif shape == 'square':
        side = kwargs.get('side', 0)
        return side ** 2
    elif shape == 'rectangle':
        length = kwargs.get('length', 0)
        breadth = kwargs.get('breadth', 0)
        return length * breadth
    else:
        raise ValueError("Unsupported shape")
