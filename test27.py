from unittest import result


class FourCal:
    def setdata(self,first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(1,2)
print(a.first)
print(a.second)

# a 는 self로 들어간다 
# 1 는 first로 들어간다.
# 2 는 second로 들어간다.
