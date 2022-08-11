dic = {'name' : 'kate' , 'age' : 24}
print(dic['name'])
# 딕셔너리

a = {1: 'a'}
a['name'] = '익명'
print(a)
# 딕셔너리 쌍 추가하기 

b = {'age' : 24}
b['name'] = "apple"

del b['age']
print(b)
# 딕셔너리  요소삭제 
# value는 같아도되지만 key는 같으면 안된다.

c = {1:'apple' , 2:'banana' , 3:'orange'}
print(c.keys())
print(c.values())
print(c.items())
# key와 value와 items를 따로 뽑는 방법 

c.clear()
print(c)
# 요소 모두지우기 

print(c.get(4))
# 일반적으로 없는 요소를 찾을때는 KeyErorr가 출력되지만 get을 사용하게된다면 None으로 출력된다,
print(c.get(4,'없음'))
# none을 출력하기 싫다면 다른 것으로 지정할수있다
print(4 in c)
# 4가c 안에있냐 라는 함수이다. 있다면 true 가 출력될것이고 없다면 false가 출력될것이다.