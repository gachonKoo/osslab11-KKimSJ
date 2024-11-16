from geo.utils import calculate_area  # geo 폴더의 utils.py에서 함수 임포트

def test_functionality():
    # 테스트 코드
    radius = 10
    area = calculate_area("circle", radius=radius)
    print(f"c = {radius}")
    print(f"area = {area}")

if __name__ == "__main__":
    test_functionality()
