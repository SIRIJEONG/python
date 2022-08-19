from unittest import result


for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')
    # 구구단

result = [num*3 for num in a if num %2 == 0]
# result의 값은 num*3이라는 리스트 / a라는 리스트에서 num을 빼와서 result를 만들어라 / 단 num이 짝수일때만 추가해라 라는 뜻이다.
result = []
for num in a:
    if num%2 == 0:
        result.append(num*3)

result = [x * y for x in range(2,10) for y in range(1,10)]

result = []
for x in range(2,10):
    for y in range(1,10):
        result.append(x*y)