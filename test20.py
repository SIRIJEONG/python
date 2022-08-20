from cgitb import reset
from unittest import result


def sum(a,b):
    result = a + b
    return result
print(sum(1,2))
# 함수

def say():
    return 'hi'
print(say())
# 입력값이 없어도 출력값은 있을수있다. 

def sum(a,b):
    print("%d,%d의 합은 %d입니다." %(a,b,a+b))
sum(1,2)
# 입력값만 있고 출력값이 없어도 함수안에서 자체적으로 처리할수있다.

def say():
    print('hi')
print(say())
# 입출력값이 둘다 없기때문에 프린트 hi만 출력되고 리턴값이 없기에 none이 출력된다.

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))
# *args 를 쓰면 몇개든 상관없이 다 들어갈수있다.

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + kwargs[k])
print(print_kwargs(name="int 조수", b="2"))
# 딕셔너리 형태로 여러개의 값이 들어올수있게 하는 매개변수