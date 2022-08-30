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

a = FourCal(1,2)