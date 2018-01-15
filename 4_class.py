
class ABCD:

    MAX_MEMBER = 10

    def __init__(self, name):
        self.name = name
        self.member = ["한성일", "김수진"]

    def join(self, name):
        if self.member.__len__() < ABCD.MAX_MEMBER:
            self.member.append(name)
            print("반갑습니다." + name)
        else:
            print(name + "님 죄송합니다.! 정원이 만땅입니다.")

    def leave(self, name):
        self.member.remove(name)
        print("또만나요." + name)

    def introduce(self):
        print("우리 그룹은 " + self.name + "입니다.")
        print("우리 멤버는 다음과 같습니다")
        for i, who in enumerate(self.member, 1):
            print(i.__str__() + "." + who + "님")

    def __del__(self):
        print("서비스 망했네!!")


abcd = ABCD("abcd")
abcd.join("한기갑")
abcd.join("이호훈")
abcd.join("황승만")
abcd.join("수지")
abcd.join("아이유")
abcd.join("이효리")
abcd.join("멍멍이")
abcd.join("고양이")

abcd.introduce()

abcd.join("코끼리")
abcd.join("도옥현")

