# 집합은 중복된 요소를 가질수없다.
# 집합은 순서가 없다.

s1 = set([1,2,3,])
# s1 = {1,2,3} 을써도 똑같이 나온다. 중괄호로도 출력할수있다.
print(s1)

l  = [1,2,2,3,3]
newList = list(set(l))
# 리스트 안에서 중복되는 요소를 없애고싶을때 
print(newList)

s2 = set("hello")
print(s2)
# 순서가 없고 중복이 없어진다.

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print(s3 & s4)
# 교집합 print(s3.intersection(s4))라고 입력해도 똑같이 출력된다.
print(s3 | s4)
# 합집합  print(s3.union(s4)) 라고 입력해도 똑같이 출력된다.
print(s3 - s4)
# 차집합  print(s3.difference(s4)) 라고 입력해도 똑같이 출력된다.

s5 = set([2,3,4,5,6,7,8])
s5.add(9)
print(s5)
# 요소를 추가할때 

s6 = set([2,3,4,5,6,7,8])
s6.update([9,10,11])
print(s6)
# 여러개의 요소를 추가할때 (중복된 요소를 추가할때는 당연히 중복될수없길때문에 그대로 출력이된다.)
s6.remove(2)
print(s6)
# 요소를 제거하고 싶을때 
