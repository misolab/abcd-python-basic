
# ---------------
print("\n\n\n정수형 변수입니다.")
# ---------------

int_value = 9999999999999999999999999999999999
print(int_value)
print(type(int_value))

bin_data = 0b101010
print(bin_data)

oct_data = 0o1234567
print(oct_data)

hex_data = 0x1234567890abcdef
print(hex_data)


# ---------------
print("\n\n\n실수형 변수입니다.")
# ---------------

float_value = 1234567890.1234567890
print(float_value)
print(type(float_value))

f1 = 1.0
print(f1)

f2 = 3.14
print(f2)

f3 = 1.56e3
print(f3)

f4 = -0.4e-4
print(f4)


# ---------------
print("\n\n\n문자열 변수입니다.")
# ---------------

str_value = '문자열 입니다.'
print(str_value)
print(type(str_value))

str_data1 = "쌍따옴표도 됩니다."
print(str_data1)

str_data2 = """
쌍따옴표 3개면 멀티라인 입니다.
한줄 개행하면 
어떻게 나올가요?
"""
print(str_data2)

str_data3 = "따옴표를 써야 한다면 이렇게 쌍따옴표 안에서 '따옴표'를 이용하면 됩니다."
print(str_data3)

'''
     문자열 포매팅은 문장과 변수 사이엥 % 로 구분
     %s : 문자열
     %c : 문자나 기호 1개
     %f : 실수형
     %d : 정수형
     %% : %표시할때
'''
print("문자열 포매팅은 '%s', '%d', '%f'" % (str_value, int_value, float_value))


# ---------------
print("\n\n\n리스트(배열) 입니다.")
# ---------------

list_value = [1, 2, 3, 4]
# list_value = list([1, 2, 3, 4])
print(list_value)
print(type(list_value))


list_data_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(list_data_1)
print("len list_data_1 - %d" % len(list_data_1))

# 인덱싱
print(list_data_1[10])
print(list_data_1[-10])

# 슬라이싱
print(list_data_1[10: 20])
print(list_data_1[10:])
print(list_data_1[-10:])

print(list_data_1[: 10])
print(list_data_1[: -10])

print(list_data_1[0: 10: 2])

'''
    [start:stop] - start 이상 stop 미만
    [:stop] - stop 미만
    [start:] - start 이상 부터 끝까지
    [:-stop] - 처음부터 끝에서 stop 미만까지
    [-start:] - 끝에서 start 까지
    [start: stop: step] start 이상 stop 미만 step 간격으로
    
    문자열을 리스트처럼 사용 가능!!
'''

list_data_1 = [1, 2, 3]
list_data_a = ['a', 'b', 'c']

# 리스트 뒤에 리스트를 붙힘
list_plus = list_data_1 + list_data_a
print(list_plus)

# 리스트를 반복적으로 붙힘
list_multi = list_data_a * 3
print(list_multi)


# ---------------
print("\n\n\n딕셔너리(맵) 입니다.")
# ---------------

dict_value = {1: "a", 2: "b", 3: "c"}
# dict_value = dict({1: "a", 2: "b", 3: "c"})
print(dict_value)
print(type(dict_value))


# ---------------
print("\n\n\n집합(셋) 입니다.")
# ---------------

set_value = {1, 2, 3}
# set_value = set({1, 2, 3})
print(set_value)
print(type(set_value))


# ---------------
print("\n\n\n튜플(불변리스트) 입니다.")
# ---------------

tuple_value = (1, 2, 3)
# tuple_value = tuple(("1", 2, 3))
print(tuple_value)
print(type(tuple_value))


# ---------------
print("\n\n\nNone(null) 입니다.")
# ---------------

str_value = None
print(str_value)
print(type(str_value))

