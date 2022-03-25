# 클래스: 변수 & 메서드(함수)가 똑같은 구조를 계속 여러번 써야되니까 하나로 묶어서 설계도처럼 만듯 것입니다
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return  result
    def mul(self):
        result = self.first * self.second
        return  result
    def sub(self):
        result = self.first - self.second
        return  result
    def div(self):
        result = self.first / self.second
        return  result
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 2)
print(a.div())