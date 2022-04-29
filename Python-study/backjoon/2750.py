# 정렬
num = int(input())
m = []
for i in range(num):
    m.append(int(input()))
m = sorted(m)
for i in range(len(m)):
    print(m[i])

# 버블정렬
num = int(input())
m = []
for i in range(num):
    m.append(int(input()))

for i in range(len(m)):
    for j in range(len(m)):
        if m[i] < m[j]:
            m[i], m[j] = m[j], m[i]
for k in m:
    print(k)

# 삽입정렬
num = int(input())
m = []
for i in range(num):
    m.append(int(input()))

for i in range(1, len(m)):
    while(i>0) & (m[i] < m[i-1]):
        m[i], m[i-1] = m[i-1], m[i]
        i -= 1
for k in m:
    print(k)