# 함수: 입력값에 따라 결과가 다를수는 있지만 로직 자체는 같은 경우에 하나의 포장지 안에 넣어서 계속 재사용할 수 있게 만들어 놓은것을 함수라 합니다. 

# 함수에 별도의 반환값이 있다면 변수에 반환값을 받아야 함.
# 변수이름 = 함수이름()

# 반환값이 없는 함수 print()함수는 괄호 안에 들어있는 내용을 화면에 출력함
# print("난생처음 파이썬")

# 반환값이 있는 함수
# int() 함수는 입력받은 문자열을 변환해서 한다.

# 함수의 기본 형태
# 함수는 매개변수를 입력받은 후 그 매개변수를 가공 및 처리한 후에 반환값을 돌려줌
# def plus(v1, v2) :
#     result = 0
#     result = v1 + v2
#     return result

# hap = 0
# hap = plus(100, 200)
# print("100과 200의 더한 값:", hap)

#사용자 정의 함수의 필요성
# def plus(num1, num2):
#     num1 = int(input("숫자1 입력: "))
#     num2 = int(input("숫자2 입력: "))
#     result = num1 + num2
#     return result
# print("A님,  두 숫자를 입력하세요")
# hap = plus()
# print(hap)
# print("B님,  두 숫자를 입력하세요")
# hap = plus()
# print(hap)
# print("C님,  두 숫자를 입력하세요")
# hap = plus()
# print(hap)

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
# def xx(x, y):
#     return x**y

# print("사칙연산을 선택 하세요.")
# print("1.더하기")
# print("2.빼기")
# print("3.곱하기")
# print("4.나누기")
# print("5. 제곱")

# choice = input("선택 하세요(1/2/3/4):")

# num1 = int(input("첫번째 숫자 : "))
# num2 = int(input("두번째 숫자 : "))

# if choice == '1':
#     print(num1,"+",num2,"=", add(num1,num2))
# elif choice == '2':
#     print(num1,"-",num2,"=", subtract(num1,num2))
# elif choice == '3':
#     print(num1,"*",num2,"=", multiply(num1,num2))
# elif choice == '4':
#     print(num1,"/",num2,"=", divide(num1,num2))
# elif choice == '5':
#     print(num1,"**",num2,"=", xx(num1,num2))
# else:
#     print("잘못된 선택")

# 숫자2개의 합과 3개의 합을 구하는 함수
#함수에 매개변수의 개수를 정해 좋으면 함수를 호출할 때, 매개변수의 개수를 정확히 맞춰서 호출해야 함
# def para(v1, v2, v3 = 0):
#     result = 0
#     result = v1 + v2 + v3
#     return result

# hap = 0
# hap = para(10, 20)
# print("매개변수 호출 결과", hap)
# hap2 = para(10, 20, 30)
# print("매개변수 호출 결과", hap2)

# def para_func(*para):
#     result = 0
#     for num in para:
#         result = result + num
#     return result
# hap = 0
# hap = para_func(10, 20)
# print("매개변수 2개 %d" % hap)
# hap = para_func(10, 20, 30)
# print("매개변수 3개 %d" & hap)

# 딕셔너리 형태
# def dic_func(**para):
#     for k in para.keys():
#         print("%s --> %d명입니다" % (k, para[k]))
# dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)

# <값 반환하기>
# 반환값이 없는 함수
# 함수를 실행한 결과, 돌려줄 것이 없는 경우에는 return문을 생략함
# 또는 반환값 없이 return만 써도 됨(대체로 return만 써도 됨)
# 반환값 없이 함수를 마치면 아무것도 반환하지 않고 함수가 종료됨
def func1():
    print("반환값이 없는 함수 실행")
func1()

# 반환값이 1개있는 함수
# 함수에서 어떤 계산이나 작동을 한 후에 반환할 값이 있으면 'return 반환값' 형식으로 표현함
def func2():
    result = 100
    return result
hap = 0
hap = func2()
print("func2()에서 돌려준 값:", hap)

# 반환값이 2개 있는 함수
# 반환할 값이 2개라면 return반환값1, 반환값2 형식으로 표현
def multi(v1, v2):
    reList = []
    res1 = v1 + v2
    res2 = v1 + v2
    reList.append(res1)
    reList.append(res2)
    return reList

myList = []
hap, sub = 0, 0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print("multi()에서 올려준 값 %d, %d" % (hap, sub))

# pass키워드
# 함수의 이름과 형태만 만들어 놓고, 내부는 나중에 코딩하고 싶은 경우에 사용하는 키워드
def myfunc():
    pass

from datetime import datetime
import random 
def lotto(): 
    number = set() 
    while len(number) < 6: 
        number.add(random.randint(1, 45)) 
    number = list(number) 
    number.sort() 
    print(number) 
lotto()

# 지역변수
# 말 그대로 한정된 지역(local)에서만 사용되는 변수

# 전역변수
# 프로그램 전체(global)에서 사용되는 변수

# 지역변수와 전역변수의 이름이 같을 경우
# 지역변수가 우선됨
def func1():
    a = 10
    print("func1()에서 a의 값", a)
def func2():
    print("func1()에서 a의 값", a)
a = 20

func1()
func2()

# 재귀함수
# 자기 자신을 호출하는 함수
# 문제를 직관적으로 이해하고 코드를 간결하게 작성할 수 있는 경우 사용
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)

# global예약어
def func1():
    global a
    a = 10
    print("func1()에서 a의 값 ", a)
def func2():
    print("func2()에서 a의 값 ", a)
a = 20
func1()
func2()

# 비밀번호 생성
import random
 
def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
 
    for i in range(6):
        index = random.randrange(len(alphabet))
        password = password + alphabet[index]
    return password
 
print(genPass())
print(genPass())
print(genPass())


# def sum_many(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
# print(sum_many(1, 2, 3, 4, 5, 6))

# def say_myself(name, old, man=True):
#     print("나의 이름은 %s 입니다" % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("여자입니다.")
#     else:
#         print("남자입니다.")
# say_myself("황진성", 18, False)

# a = 1
# def vartest(a):
#     a = a + 1
# vartest(1)
# print(a)