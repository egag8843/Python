"""
날짜 : 2021/05/13
이름 : 장경준
내용 : 코딩 테스트 - 1이 될때 까지
https://github.com/chhak2021/Python
"""
n, k = map(int, input().split())
result = 0

while True:

    if n == 1:
        break

    if n % k == 0:
        n /= k
    else:
        n -= 1

    result += 1

print(result)

