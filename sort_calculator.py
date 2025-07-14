# 사용자 입력을 받아 float 숫자 리스트로 변환하고
# 버블 정렬 알고리즘을 사용하여 오름차순으로 정렬한 후 출력하는 프로그램입니다.

def bubble_sort(numbers):
    """
    버블 정렬 알고리즘을 사용하여 리스트를 오름차순으로 정렬합니다.
    sorted()나 .sort()는 사용하지 않습니다.
    """
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # 두 요소의 위치를 교환
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def main():
    try:
        # 사용자로부터 입력을 받음
        user_input = input("Enter numbers separated by spaces: ").strip()

        # 입력이 비어 있는 경우 예외 발생
        if not user_input:
            raise ValueError

        # 입력 문자열을 공백 기준으로 나눔
        str_numbers = user_input.split()

        # 각 문자열을 float으로 변환
        float_numbers = [float(num) for num in str_numbers]

        # 버블 정렬을 사용하여 정렬
        sorted_numbers = bubble_sort(float_numbers)

        # 정렬된 숫자들을 출력 (소수점 포함)
        print("Sorted:", " ".join(f"{num:.1f}" for num in sorted_numbers))

    except ValueError:
        # 숫자가 아닌 값이 포함되었거나 입력이 비어 있는 경우
        print("Invalid input.")

# 프로그램의 시작점
if __name__ == "__main__":
    main()
