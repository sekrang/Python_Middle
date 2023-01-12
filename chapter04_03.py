#chapter04-3
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시테이블 : Key에 Value를 저장하는 구조
# 파이썬 자체의 엔진이 해시테이블로 이루어짐
# 파이썬 dict 해쉬 테이블 ex. 
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 -> Key에 대한 Value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1)) # 해시함수는 불변형만 가능
# print(hash(t2)) 리스트는 값의 수정이 가능해서 해시함수 사용 불가 

print()
print()

# Dict Setdefault ex
source = (('k1', 'val1'),
        ('k1', 'val2'),
        ('k2', 'val3'),
        ('k2', 'val4'),
        ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의 - 덮어 씌어짐
new_dict3 = {k: v for k, v in source}

print(new_dict3)

print()
print()
