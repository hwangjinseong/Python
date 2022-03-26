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