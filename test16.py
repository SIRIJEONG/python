from email import message


money = True
if money :
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# 조건문(if) 들여쓰기 꼭 잘하기 

a = 1
b = 2
if a<b:
    print("apple")
else:
    print("banana")

c = 2000
if c >= 3000:
    print("red")
else:
    print("black")  

# and는 &  or은 | 

d = 23
e = 55
if 1 in [1,2,3]:
    print("good")
else:
    print("bad")
# 만약 [1,2,3] 안에 1 이있다면 true and false 라는뜻 not in 이면 [1,2,3]안에 1이 없냐 라는뜻 

pocket = ['paper' , 'cellphone']
card = False
a = True
if 'money' in pocket:
    pass
elif card:
    print("택시를 타고 가라")
elif a :
    print("버스를 타고 가라")
else:
    print("걸어가라")

score = 70
message = "success" if score >= 60 else "failure"
print(message)
# 조건부 표현식 else일때의 값을 꼭 써줘야한다.