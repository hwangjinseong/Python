# 인덱싱(indexing)
a = "Life is too short, You need Python"
print(a[0])
print(a[12])
print(a[-1])

# 슬라이싱(Slicing)
b = "20010331Riny"
date = b[:8]
weather = b[8:]
print(date)
print(weather)
print(b[::2])

# 문자열 포매팅
c = "I eat %d apples." % 3
print(c)
number = 10
day = "three"
c2 = "I ate %d apples. so I was sick for %s days." % (number, day)
print(c2)

# 정렬과 공백
d = "%10s" % "hi"
d2 = "%-10sjane." % "hi" 
print(d)
print(d2)

# 소수점 표현
e = "%0.4f" % 3.4211223
e2 = "%10.4f" % 3.4211223
print(e)
print(e2)

# 문자열 개수 세기(count)
f = "hobby"
print(f.count('b'))

# 위치 알려주기(find)
f2 = "Python is best choice"
print(f2.find('b'))

# 문자열 삽입(join)
f3 = ","
print(f3.join('abcd'))

# 소문자를 대문자로 바꾸기(upper)
f4 = "hi"
print(f4.upper())

# 대문자를 소문자로 바꾸기(lower)
f5 = "HI"
print(f5.lower())

# 대문자와 소문자 변환
ss = 'Python is Easy. 그래서 programming이 재미있습니다'
print(ss.swapcase())
print(ss.title())

# 양쪽 공백 지우기(strip)
f6 = "  hi  "
ss = "   파   이   썬   "
ss2 = "---파---이---썬---"
print(f6.strip())
print(ss.rstrip())
print(ss.lstrip())
print(ss2.strip("-"))

# 문자열 바꾸기(replace)
g = "Life is too short"
print(g.replace("Life", "Your leg"))

# 문자열 나누기(split)
g2 = "Life is too short"
print(g2.split())
g3 = "a:b:c:d"
print(g3.split(':'))

# 문자열 찾기
ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'
ss.count('공부')
print(ss.find('공부'), ss.rfind('공부'), ss.find('공부', 5), ss.find('없다'))
print(ss.index('공부'), ss.rindex('공부'), ss.index('공부', 5))
print(ss.startswith('파이썬'), ss.startswith('파이썬', 10), ss.endswith('^^')), 

# 공백지우기
# ss = input("입력: ")
# result = ss.replace(" ","")
# print(result)

# ss = input("입력: ")
# result = ss.replace("o","$")
# print(result)

# 문자열 분리 결합하기: split(), splitlines(), join()

# year = int(input("연: "))
# month = int(input("월: "))
# day = int(input("일: "))

# year = year + 10
# print(year/month/day)

# 함수명에 대입하기: map()함수
# before = ['2019', '12', '31']
# after = list(map int, before)
# print(before)

# 문자열 정렬하기, 채우기: center(), ljust(), rjust(), zfill()
# ss = '파이썬'
# ss.center(10)
# ss.center(10, '-')
# ss.ljust(10)
# ss.rjust(10)
# ss.zfill(10)
# print(ss)

# 문자열 구성 파악하기: isdigit(), isalpha(), isalnum(), islower(), isupper(), isspace()
# '1234'.isdigit()
# 'abcd'.isalpha()
# 'abc123'.isalnum()
# 'abcd'.islower()
# 'ABCD'.isupper()
# '    '.isspace()

