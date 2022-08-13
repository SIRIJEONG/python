# 변수를 만들때는 =(assignment)기호를 사용한다.
# 파이썬에서 사용하는 변수는 객체를 가리키는 것

from copy import copy


a = [1,2,3]
b = a  
# a 리스트의 주소를 b에게 준것 
a[1] = 4
# a의 첫번째 인덱스를 4로 바꿈
print(b)
print(a)
# a 와 b 둘다 바뀌었다.
print(id(a))
print(id(b))
# 주소값도 같다.
print(a is b)
# 같은 주소를 바라보고있냐 라는 뜻이다. 같은주소를 가지고있다면 True가 출력된다.

c = [1,2,3]
d= c[:]
c[1] = 4
print(c)
print(d)
# 슬라이싱 해서 새로운 값을 넣으면 다른 주소를 가질수있다.
print(id(c))
print(id(d))

from copy import copy
e = [1,2,3]
f= copy(e)
e[1] = 4
print(e)
print(f)
# 다른 주소값을 가지게하는 다른방법 (값을 복사해서 a리스트를 b한테 새롭게 할당하겠다.)
print(id(e))
print(id(f))


g,h = ('python' , 'life')
print(g)
print(h)
# 리스트를 해도 똑같다. g = h = 'hello를 사용해도 g,h값에 똑겉이 hello가 출력된다.

i = 3
j = 5
tmp = j 
# tmp라는 임시변수에 j를 저장
j = i
# a값을 b에 덮어씌움
i = tmp
# 임시변수에 저장해놓은 tmp를 다시꺼내와서 i에 넣는다.
print(i)
print(j)
# 일반적인 a와 b를 바뀌는 법

k = 3
l = 5
k,l = l,k
print(k)
print(l)
# 파이썬에서 a와 b바꾸는법 (easy)