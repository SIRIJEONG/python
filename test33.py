class Family:
    lastname = "김"
# 클래스 변수 (공통으로 쓸때 사용한다.)
Family.lastname = "박"
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

# 각각 객체마다 변수를 쓸때는 객체변수를 쓴다.