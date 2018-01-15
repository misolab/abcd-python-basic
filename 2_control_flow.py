
# 문자열이 비었으면 False 로
str_value = "ABCD"
# str_value = ""

if str_value == "ABCD":
    print("ABCD sames str_value " + str_value)
elif str_value:
    print("str_value is " + str_value)
else:
    print("str_valie is empty")


# 컨테이너의 값이 빈 것은 False로
list_value = ["ABCD", "가나다라", "1234"]

if "ABCD" in list_value:
    print("ABCD contains list_value -> " + str(list_value))
elif list_value:
    print("list_value is " + list_value[0])
else:
    print("list_value is empty")


# for item in list_value:
#     print(item)

for idx, item in enumerate(list_value):
    print(str(idx) + " - " + item)


가나다라 = "가나다라"
for idx, item in enumerate(list_value):
    if item == 가나다라:
        print("소중한 한글 - " + item)
        break

    print(str(idx) + " - " + item)

else:
    print(가나다라 + " 없어요")
