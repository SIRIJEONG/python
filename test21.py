from readline import read_init_file


def sum_and_mul(a,b):
    return a+b, a*b

print(sum_and_mul(1,2))
# 여러개의 값을 하나로 리턴하고 그것을 하나의 튜플로 나타낸다. 그 중 하나의 값만 리턴하고 싶다면 (1,2)뒤에 [0] 이라고 작성한다면 0번째 값인 a+b값만이 출력된다.

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("augenstern",20,True)
# 변수 초깃값을 머저 설정하는법 man=True라고 미리 설정해놓고 출력을 한다면 남자입니다로 출력된다 그리고 입력값에 True가 아닌 flase를 입력하게 된다면 
# 설정된 초깃값이 있더라도 여자입니다로 출력될것이다.

a = 1
def vartest(a):
    a = a + 1
# 변수의 범위 위의 함수는 지역변수라 그안에서만 작용한다.
vartest(a)
print(a)
# 그렇기 때문에 2 가아닌 1이 출력된다.

b = 1
def vartest(b):
    b = b + 1
    return b
# return 이라는 output을 만들어서 밖으로 보내기 때문에
b = vartest(b)
print(b)
# 그렇기떄문에 2가 출력이된다.

c = 1
def vartest():
    global c
    c = c + 1
# global을 쓰게된다면 지역변수에서 전역변수로 바뀌며 전체에서 사용할수있는 변수로 바뀌게 된다.
vartest()
print(c)
# 그렇기떄문에 2가 출력이된다.

add = lambda d,e:d + e
print(add(1,2))
# lamda라는 함수를 사용해 축약할수있다.
myList = [lambda f,g:f+g, lambda f,g:f*g]
print(myList[1](1,2))
# lamda함수의 또다른 예시 / 리스트안의 함수를 불러와서 입력하고 출력할수있다. 