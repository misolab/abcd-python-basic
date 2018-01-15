
import this

print("Hello ABCD")

# 다이내믹 타입핑이라서 아래처럼 변수형이 없이 선언이 가능합니다.
hello = "ABCD hello"
print(hello)

'''
    주석 여러줄일땐 이렇게 '+'+' 을 3개 붙혀서 가능합니다.
    아래는 블록{}을 사용하는 법으로 들여쓰기를 이용해 가능합니다.  
'''

if hello == "ABCD hello":
    print("if check")
    print("hello is " + hello)
    print("end if block")
else:
    print("hello is ..." + hello)
    print("end if-else block")

print("out if block")




