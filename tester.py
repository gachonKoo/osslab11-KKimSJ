# tester.py
from geo.utils import calculate_area  # geo 폴더 내 모듈 가져오기

def test_functionality():
    print("Testing calculate_area function...")
    try:
        print("Circle:", calculate_area("circle", radius=10))  # Example test
        print("Rectangle:", calculate_area("rectangle", width=4, height=6))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_functionality()
