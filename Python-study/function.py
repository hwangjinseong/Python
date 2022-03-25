# 함수: 입력값에 따라 결과가 다를수는 있지만 로직 자체는 같은 경우에 하나의 포장지 안에 넣어서 계속 재사용할 수 있게 만들어 놓은것을 함수라 합니다. 
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1, 2, 3, 4, 5, 6))

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다" % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("여자입니다.")
    else:
        print("남자입니다.")
say_myself("황진성", 18, False)

a = 1
def vartest(a):
    a = a + 1
vartest(1)
print(a)