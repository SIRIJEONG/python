# Immutable (정수,실수,문자열,튜플) = 변하지 않는 자료형
# Mutable (리스트,딕셔너리,집합) = 변할 수 있는 자료형 

######Immutable######
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)
#####################

###### Mutable ######
b = [1,2,3]
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)
#####################
# 주소값을 넘겨주면 그대로 쓰게된다.