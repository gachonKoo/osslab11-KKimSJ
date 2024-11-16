from geo.utils import calculate_area

def test_functionality():
    print("Testing geo package functionality...")

    # Test cases
    circle_area = calculate_area('circle', radius=5)
    print(f"Circle area (radius=5): {circle_area}")

    square_area = calculate_area('square', side=4)
    print(f"Square area (side=4): {square_area}")

    rectangle_area = calculate_area('rectangle', length=6, breadth=3)
    print(f"Rectangle area (6x3): {rectangle_area}")

if __name__ == "__main__":
    test_functionality()
