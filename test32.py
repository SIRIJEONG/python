class FourCal:
    def __init__(self,first, second):
        self.first = first
        self.second = second
        # __init__ 을 쓰게 된다면 무조건 제일먼처음 실행된다. 
    def setdata(self,first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def asub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0 
        else:
            return self.first / self.second

# 부모와 자식이 똑같은 메소드를 가지고있다면 자식에서 변형이 되었어도 자식클래스로 된다.
# 만약 자식클래스가 없었다면 0으로 나눴을때 오류가 나올텐데 자식클래스에서 0으로 나눈다면 0으로 출력하했기때문에 0으로나눠도 0으로 출력된다.
# 이것을 "메서드 오버라이딩" 이라고한다. 
a = SafeFourCal(4,2)
print(a.div())