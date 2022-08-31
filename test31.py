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

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
# 자식클래스에 메서드 추가 
# pow 함수는 **을 쓰면 제곱이된다.

a = MoreFourCal(4,2)
print(a.pow())