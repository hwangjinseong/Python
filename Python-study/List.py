# 리스트: 변수 여러 개를 묶는 역
a = [1, 2, "int", "char", ["황진성", "Manse samdori"]]
print(a[3])
print(a[4][1])

# 리스트의 인덱싱
a2 = [1, 2, 3]
print(a2[0])
print(a2[0] + a2[2])

# 리스트 더하기
a1 = [1, 2, 3]
b1 = [4, 5, 6]
print(a1 + b1)

# 리스트 반복하기
b = [1, 2, 3]
print(b * 3)

# 리스트에서 하나의 값을 수정하기
c = [1, 2, 3]
c[2] = 4 
print(c)

# 리스트에서 연속된 범위의 값 수정하기
c[1:2]
print(c[1:2])
c[1:2] = ['a', 'b', 'c']
print(c[1:2])

# 리스트에 요소 추가(append)
d = [1, 2, 3]
d.append(4)
print(d)

# 리스트 정렬(sort)
d1 = [1, 4, 3, 2, 6, 5]
d1.sort()
print(d1)

# 리스트 뒤집기(reverse)
d2 = ['a', 'c', 'b']
d2.reverse()
print(d2)

# 위치 빈환(index)
d3 = [1, 2, 3]
print(d3.index(2))

# 리스트에 요소 삽입(insert)
e = [1, 2, 3]
e.insert(0, 4)
print(e)

# 리스트 요소 제거(remove) 
e1 = [1, 2, 3, 1, 2, 3]
e1.remove(3)
print(e1)

# 리스트 확장(extend)
f = [1, 2, 3]
f.extend([4, 5])
print(f)
g = [6, 7]
f.extend(g)
print(f)

# List
# 하나씩 사용하던 변수를 붙여서 한 줄로 붙여놓는 개념
# 리스트는 종이상자를 한 줄로 붙인 후에 박스 전체의 이름을 지정하여 사용함
# 대괄호 안에 값을 선언

# 리스트의 다양한 형태
numlist = []
intlist = [10, 20, 30]
strlist = ['난생처음', '황진성', 'good']
mixlist = [10, 20, 'mix']

# 리스트를 하나씩 추가하기
# 리스트이름.append(값)
numlist = []
numlist.append(0)
numlist.append(0)
numlist.append(0)
numlist.append(0)
print(numlist)

# 반복문 사용해서 리스트 값 추가하기
numlist = []
for i in range(0, 4):
    numlist.append(0)
len(numlist)

# 반복문 사용해서 값 대입
numlist = []
for i in range(0, 4):
    numlist.append(0)
hap = 0
for i in range(0, 4):
    numlist[i] = int(input("숫자 : "))
hap = numlist[0] + numlist[1] + numlist[2] + numlist[3]
print(hap)

# 첨자를 활용한 리스트 접근 방법
# 첨자가 음수 값인 경우
numlist = [1, 2, 3, 4]
numlist[-1] = 4
numlist[-2] = 3

# 콜론을 사용하여 범위를 지정
numlist = [1, 2, 3, 4, 5, 6, 7]
#print(numlist[0:3]) = [1, 2, 3]
#print(numlist[2:]) = [3, 4]
#print(numlist[::2]) = [1, 3, 5, 7]
#print(numlist[::-1]) = [7, 6, 5, 4, 3, 2, 1]

# 리스트 덧셈
# 요소들이 합쳐져 하나의 리스트가 됨
numlist = [10, 20, 30]
mylist = [40, 50, 60]
#print(numlist + mylist) = [10, 20, 30, 40, 50, 60]

# 리스트 곱셈
#print(numlist * 3) = [10, 20, 30, 10, 20, 30, 10, 20, 30,]

# 명언 출력하기
import random
from secrets import randbelow
wiseSay = [
    "삶이 있는 한 희망은 있다",
    "언제나 현제에 집중할 수 있다면 행복할 것이다",
    "신은 용기있는 자를 결코 버리지 않는다",
    "피할 수 없으면 즐겨라",
    "행복한 삶을 살기위해 필요한 것은 거의 없다",
    "내일은 내일의 태양이 뜬다",
    "계단을 밟아야 계단 위에 올라설 수 있다",
    "행복한 습관이다, 그것이 몸에 지니라",
    "1퍼센트의 가능성, 그것이 나의 길이다",
    "작은 기회로 부터 종종 위대한 업적이 시작된다"
]
wise = random.randint(0 ,len(wiseSay)-1)
print(wiseSay[wise])

# 리스트 값 변경하기
numlist = [10, 20, 30]
numlist[1:2] = [200, 201]
#print(numlist) = [10, 200, 201, 30]

numlist = [10, 20, 30]
numlist[1] = [200, 201]
#print(numlist) = [10, [200, 201], 30]

numlist = [10, 20, 30]
numlist[2:3] = [200, 201]
#print(numlist) = [10, 20, 200, 201]

# 리스트에 값 삽입하기
# ppend(값) : 맨 뒤에 값 추가하기
# insert(위치, 값): 정해진 위치에 값 삽입하기
numlist = [10, 20, 30]
numlist.insert(1, 123)
#print(numlist) = [10, 123, 20, 30]

# 리스트 값 삭제하기
numlist = [10, 20, 30]
del(numlist[1])
#print(numlist)

aa = [10, 20, 30, 40, 50]
aa[1:4] = []
#print(aa) = [10, 50]
numlist = [10, 20, 30]
#dle(numlist)
# print(numlist) = 오류발생

numlist = [10, 20, 30]
numlist.remove(10)
#print(numlist) = [20, 30]

numlist = [10, 20, 30, 10, 10]
numlist.remove(10)
#print(numlist) = [20, 30, 10, 10]

# pop(): 제일 뒤의 값을 뽑아내서 값을 알려준 뒤 삭제함
numlist = [10, 20, 30]
numlist.pop()
#print(numlist) = [10, 20]

# 리스트에서 개수 세기
# count(찾을 값): 찾을 값이 몇 개인지 개수를 세서 알려줌

# sort(): 리스트의 값을 정렬함
numlist = [20, 10, 40, 50, 30]
numlist.sort()
#print(numlist) = [10, 20, 30, 40, 50]

# sort(reverse): 리스트의 값을 정렬함
numlist = [20, 10, 40, 50, 30]
numlist.sort()
#print(numlist) = [50, 40, 30, 20, 10]

# reverse(): 리스트의 마지막 인덱스부터 위치가 반대로 됨
numlist = [20, 10, 40, 50, 30]
numlist.reverse()
#print(numlist) = [30, 50, 40, 10, 20]

# copy(): 리스트의 내용을 새로운 리스트에 복사한다

myList = [30, 10, 20]
print("현재 리스트: %s" %myList)

myList.append(40)
print("append(40) 후의 리스트: %s" %myList)

print("pop()으로 추출한 값 : %s" %myList.pop())
print("pop() 후의 리스트 : %s" %myList)

myList.sort()
#print("sort() 후의 리스트: %s", %myList)    

myList.reverse()
print("reverse() 후의 리스트 : %s"%myList)

print("20값의 위치 : %d" %myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후의 리스트: %s" %myList)

myList.remove(222)
#print("remove(222) 후의 리스트: %s", %myList)

myList.extend([77, 88, 777])
#print("extend([77, 88, 777]) 후의 리스트: %s", %myList)

print("77값의 개수 : %d" %myList.count(77))

myList = [30, 10, 20]
newList = sorted(myList)
print("sorted() 후의 myLIst : %s" %myList)
print("sorted() 후의 newLIst : %s" %newList)

# 2차원 리스트
# 1차원 리스트를 여러 개 연결한 리스트
# 2개의 첨자를 사용함
# 리스트이름[행][열]([가로][세로])'

list1 = []
list2 = []
value = 1
for i in range(0, 3):
    for k in range(0, 4):
        list1.append(value)
        value += 1
        list2.append(list1)
        list1 = []

for i in range(0, 3):
    for k in range(0, 4):
        print("%3d" % list2[i][k], end=" ")
    print("")