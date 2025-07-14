# 덧셈 함수
def add(a, b):
    return a + b

# 뺄셈 함수
def subtract(a, b):
    return a - b

# 곱셈 함수
def multiply(a, b):
    return a * b

# 나눗셈 함수
def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

# 메인 실행 블록
if __name__ == "__main__":
    try:
        # 두 개의 숫자 입력 받기
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        
        # 연산자 입력 받기
        operator = input("Enter an operator (+, -, *, /): ")

        # 연산자에 따라 함수 호출
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == '*':
            result = multiply(a, b)
        elif operator == '/':
            result = divide(a, b)
        else:
            result = "Invalid operator."

        # 결과 출력
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter integer values.")
