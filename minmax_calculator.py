def main():
    try:
        # 사용자로부터 입력을 받고 공백 기준으로 나눔
        numbers = input("Enter numbers separated by spaces: ").split()
        
        if not numbers or all(num.strip() == "" for num in numbers):
            print("Invalid input.")
            return


        # 문자열을 실수(float)로 변환
        float_numbers = [float(num) for num in numbers]

        # 첫 번째 숫자를 기준으로 최소값과 최대값 초기화
        minimum = float_numbers[0]
        maximum = float_numbers[0]

        # 나머지 숫자들을 순회하며 최소값과 최대값 갱신
        for num in float_numbers[1:]:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num

        # 결과 출력
        print(f"Min: {minimum}, Max: {maximum}")

    except ValueError:
        # 숫자가 아닌 값이 입력된 경우 예외 처리
        print("Invalid input.")

# 프로그램의 진입점
if __name__ == "__main__":
    main()
