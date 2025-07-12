def get_geometric_series_term():
    """
    등비수열의 첫째항, 공비, 그리고 알고 싶은 항의 번호를 입력받아 해당 항의 값을 반환합니다.
    """
    while True:
        try:
            first_term = float(input("첫째항을 입력하세요: "))
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")

    while True:
        try:
            common_ratio = float(input("공비를 입력하세요: "))
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")

    while True:
        try:
            n_th_term = int(input("알고 싶은 항의 번호를 입력하세요 (예: 1, 2, 3...): "))
            if n_th_term <= 0:
                print("항의 번호는 1 이상의 정수여야 합니다.")
            else:
                break
        except ValueError:
            print("잘못된 입력입니다. 정수를 입력해주세요.")

    # 등비수열의 n번째 항 공식: a * r^(n-1)
    # 파이썬에서 **는 거듭제곱 연산자입니다.
    term_value = first_term * (common_ratio ** (n_th_term - 1))
    return term_value

if __name__ == "__main__":
    result = get_geometric_series_term()
    print(f"입력하신 등비수열의 해당 항의 값은: {result} 입니다.")
