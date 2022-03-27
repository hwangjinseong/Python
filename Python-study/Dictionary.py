# 딕셔너리: 연관 배열 또는 해시, 단어 그대로 해석하면 사전, Key를 통해 Value를 얻는다
dic = {'name': 'Eric', 'age': 15}
print(dic['name'])

# 딕셔너리 깡 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)
# 딕셔너리 요소 삭제하기
del a[1]
print(a)

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'jinseong': 18}
print(grade['pey'])
print(grade['jinseong'])

# 딕셔너리 만들 때 주의할 사항
a2 = {1:'a', 1:'b'}
print(a2)

# Key리스트 만들기(keys)
a3 = {'name': 'pey', 'phone': '01199993323', 'birth': '1118'}
print(a3.keys())

# Value리스트 만들기(values)
print(a3.values())

# Key, Value쌍 얻기(items)
print(a3.items())

# Key, Value쌍 모두 지우기(clear)
print(a3.clear())

# Key로 Value얻기(get)
print(a3.get('names', '없음'))