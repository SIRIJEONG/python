# 클래스 상속
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
    pass
# 자식

a = MoreFourCal(4,2)
print(a.add())

# 부모가 만든걸 자식이 상속받아도 똑같이 다 쓸수있다.

