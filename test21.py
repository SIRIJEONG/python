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