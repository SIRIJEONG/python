a = "파이썬 %d번째 테스트입니다." %3
print(a)

b= "파이썬 " + str(3) + "번째 테스트입니다."
print(b)
# b 와같은 불편한 방식보단 a와 같이 쓰는것이 편하다.

number = 3
number2 = 4
c = "파이썬 %d번째 테스트 입니다. 나중에 %d번째 테스트를 하겠습니다." %(number , number2)
print(c)
# %s 는 문자열 %c는 문자1개 %d는 정수 %f는 부동소수 

d = "%5s" %"hi"
print(d)
# 중간에 숫자를 넣으면 원하는 숫자만큼 공백이 생긴다. -는 반대 공백 

e = "%0.4f" %3.1242323566
print(e)
# 소수점이 너무 길어서 잘라야할때 소숫점을 넣으면 점뒷값 만큼만 쓴다 

f = "파이썬 {0}번째 테스트 중입니다.".format(5)
print(f)

number3 = 20
number4 = 30
g = "파이썬 {0}번째 테스트 중입니다. 나중에 {1}번째 테스트를 하겠습니다.".format(number3 , number4)
print(g)

h = "파이썬 {number5}번째 테스트 중입니다. 나중에 {number6}번째 테스트를 하겠습니다.".format(number5 = 31 , number6 = 32)
print(h)

# 포멧팅