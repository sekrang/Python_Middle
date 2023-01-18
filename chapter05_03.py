#chapter05-3
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(래퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# closure 사용 
def closure_ex1():
    # Free Variable
    # 클로저 영역
    series = []
    def  avarager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return avarager

avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__)) # co가 붙은건 자유변수를 뜻함
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)

print()
print()

# 잘못된 클로저 사용
def closure_ex2():
    # Free vaiable
    cnt = 0
    total = 0

    def avarager(v):
        cnt += 1
        total += v
        return total / cnt
    return avarager

avg_closure2 = closure_ex2()

# print(avg_closure2(10)) # 예외

def closure_ex3():
    # Free vaiable
    cnt = 0
    total = 0

    def avarager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return avarager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))













