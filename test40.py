# 내장함수 - 파이썬안에 기본적으로 가지고있는 함수 
print(abs(-3))
# abs 는 절댓값
print(all([1,2,3]))
print(all([1,2,3,0]))
# all 은 모두 참인지 검사하는것 
print(any([1,2,3,0]))
print(any([0,""]))
# any 는 하나라도 참이있는지 검사하는것 
print(chr(97))
print(chr(48))
# chr 은 ASCII(아스키코드)를 입력받아 문자로 출력한것 
# ASCII(아스키 코드) 란 0~127사이의 숫자를 각 문자에 대응 
print(dir([1,2,3]))
# dir이란 자체적으로 가지고있는 변수나 함수를 보여줌 
print(divmod)
print(divmod(1.3,0.2))
# divmod 란 몫과 나머지를 튜플 형태로 돌려줌 
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i,name)
    # 리스트가 있으면 딕셔너리 처럼 빼서 출력할수있다 .
print(eval('1+2'))
print(eval("'hi' + 'a'"))
# eval 이란 실행 후 결과값을 돌려주는 것 
def positive(x):
    return x>0

a = list(filter(positive, [1,-3,2,0,-5,6]))
print(a)
# filter는 리스트가 있다면 필터로 걸러서 참인것만 출력하는 것 

b = 3
print(id(3))
# 주소값

