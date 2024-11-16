# geo/tester.py
import sys
import os

# 현재 스크립트의 상위 경로를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import calculate_area

def test_functionality():
    print("Testing calculate_area function...")
    try:
        print("Circle:", calculate_area("circle", radius=5))  # Expected: 78.54
        print("Rectangle:", calculate_area("rectangle", width=4, height=6))  # Expected: 24
        print("Triangle:", calculate_area("triangle", base=3, height=7))  # Expected: 10.5
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_functionality()
