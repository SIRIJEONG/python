from cmath import pi


a = 80
b = 75
c = 55
# 순서대로 국영수다 세 과목의 평균을 구하여라 
print((a+b+c)/3)

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
# 주민번호 앞자리와 뒷자리 구분하여 출력하기

pin = "881120-1068234"
print(pin[7])
# 주민번호에서 성별을 나타내는 숫자출력 (1이면 남자 2면 여자)

a = "a:b:c:d"
b = a.replace(":","#")
print(b)
# 문자열안 원하는것을 바꿀떄 사용

a = [1,3,5,4,2]
a.sort()  #리스트를 바르게 정렬  
a.reverse() #리스트를 뒤에서부터 출력 
print(a)

e = ['Life','is','too','short']
resurt = " ".join(e)
print(resurt)
# 리스트 안에 문자들을 join함수를 이용해 공백을 넣어줘서 출력하기