# class란 함수랑 변수가 똑같은 구조로 여러번 써야할때  하나로 묶어서 설계도로 만든 것 
class Calculator:
    # class쓰고 뒤에는 대문자로 시작하는 클래스이름쓰기 
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))