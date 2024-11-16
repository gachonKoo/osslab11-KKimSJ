# geo/tester.py
from geo.utils import calculate_area

def test_functionality():
    print("Testing calculate_area function...")

    # Test cases
    try:
        print("Circle area:", calculate_area("circle", radius=5))  # Expect 78.53975
        print("Rectangle area:", calculate_area("rectangle", width=4, height=6))  # Expect 24
        print("Triangle area:", calculate_area("triangle", base=3, height=7))  # Expect 10.5
        print("Invalid shape test:", calculate_area("hexagon"))  # Expect error
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    test_functionality()
