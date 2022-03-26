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

# 양쪽 공백 지우기(strip)
f6 = "  hi  "
print(f6.strip())

# 문자열 바꾸기(replace)
g = "Life is too short"
print(g.replace("Life", "Your leg"))

# 문자열 나누기(split)
g2 = "Life is too short"
print(g2.split())
g3 = "a:b:c:d"
print(g3.split(':'))