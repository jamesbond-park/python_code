# 구구단 출력 (2단부터 9단까지)
for i in range(2, 10):  # 2단부터 9단까지
    print(f"--- {i}단 ---")
    for j in range(1, 10):  # 1부터 9까지 곱하기
        print(f"{i} × {j} = {i * j}")
    print()  # 단 사이의 줄바꿈
print("프로그램이 종료 되었습니다.")