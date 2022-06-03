# 모듈(module)이란 함수나 변수 또는 클래스 들을 모아 놓은 파일이다.
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만들어진 파이썬 파일이라고도 할 수 있다.

# 함수 선언 부분
def func1():
    print("Module.py의 func1()이 호출됨.")
def func2():
    print("Module.py의 func2()이 호출됨.")
def func3():
    print("Module.py의 func3()이 호출됨.")

# 모듈의 종류
# 표준 모듈, 사용자 정의 모듈, 서드 파티 모듈로 구분
# 표준 모듈: 파이썬에서 제공하는 모듈
# 사용자 정의 모듈 : 직접만들어서 사용하는 모듈
# 서드 파티 모듈 : 파이썬이 아닌 외부 회사나 단체에서 제공하는 모듈
#  * 파이썬 표준 모듈이 기능을 제공 않음
#  * 서드 파티 모듈 덕분에 파이썬에도 고급 가능

# 수학 계산 모듈 math
import math
dir(math)

# 패키지
# 모듈이 하나의 *.py 파일 안에 함수가 여러 개 들어 이ㅆ는 것이라면, 패키지는 여러 모듈을 모아 놓은 것을 말한다.

# 내부함수, lambda, map()
# 내부함수 : 함수 안에 함수가 있는 형태
def outFunc(v1, v2):
    def inFunc(num1, num2):
        return num1 + num2
    return inFunc(v1, v2)
print(outFunc(10, 20))
# outFUnc()함수 밖에서 호출하면 오류 발생
# print(inFunc(10, 20))

# 람다 함수: 함수를 한 줄로 간단라게 만들어 줌
def hap(num1, num2):
    res = num1 + num2
    return res
print(hap(10, 20))
# 람다 함수 사용
hap = lambda num1 = 10, num2 = 20: num1 + num2

# 리스트에 모두 10을 더하기
myList = [1, 2, 3, 4, 5]
def add10(num) :
    return num + 10

for i in range(len(myList)):
    myList[i] = add10(myList[i])
print(myList)

# 람다 함수와 map() 함수로 간단히
myList = [1, 2, 3, 4, 5]
add10 = lambda num : num + 10
myList = list(map(add10, myList))
print(myList)