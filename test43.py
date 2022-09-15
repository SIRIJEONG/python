 # 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9 이다. 이들의 총합은 23이다. 1000미만의 자연수에서 3의 배수다 5의 배수의 총합을 구하라
result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
            # or를 썼기때문에 중복은 되는것은 한번만 출력된다.
            result += n
print(result)
