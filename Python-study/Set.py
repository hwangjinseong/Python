# 집합: 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형, 중복은 허용하지 않는다, 순서가 없다
# 집합 자료형
s1 = set([1, 2, 3])
print(s1)

# 순서가 없고 중복이 허용되지 않는다
s2 = set("Hello")
print(s2)

# 리스트로 나타낼 때
l = [1, 2, 2, 3, 3]
newList = list(set(l))
print(newList)

# 교집합 1
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5 ,6, 7, 8, 9])
print(s1&s2)
# 교집합 2
print(s1.intersection(s2))

# 합집합 1
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5 ,6, 7, 8, 9])
print(s1 | s2)
# 합집합 2
print(s1.union(s2))

# 차집합
s5 = set([1, 2, 3, 4, 5, 6])
s6 = set([4, 5 ,6, 7, 8, 9])
print(s5.difference(s6))
print(s6.difference(s5))

# 값 1개 추가하기(add)
se1 = set([1, 2, 3])
se1.add(4)
print(se1)

# 값 여러 개 추가하기(update)
se2 = set([1, 2, 3])
se2.update([4, 5, 6])
print(se2)
# 특정 값 제거하기
se3 = set([1, 2, 3])
se3.remove(2)
print(se3)