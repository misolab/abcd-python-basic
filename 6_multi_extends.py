
class Group:

    MAX_MEMBER = 10

    def __init__(self, name):
        self.name = name
        self.member = ["한성일", "김수진"]

    def join(self, name):
        if self.member.__len__() < Group.MAX_MEMBER:
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
        for i, who in enumerate(self.member):
            print(i.__str__() + "." + who + "님")

    def write(self, text):
        print("Group의 글쓰기 입니다." + text)

    def __del__(self):
        print("서비스 망했네!!")


class Event:

    def __init__(self):
        self.events = []

    def create_event(self, event_name):
        self.events.append(event_name)
        print(event_name + " 이벤트가 추가되었습니다.")

    def show_events(self):
        print("우리 이벤트는 ")
        for item in self.events:
            print("\t" + item)
        print("가 있습니다. 많이 참여 해주세요")

    def write(self, text):
        print("Event의 글쓰기 입니다." + text)


class FacebookGroup(Event, Group):
    SERVICE_NAME = "페이스북 그룹"

    def __init__(self, name):
        Group.__init__(self, name)
        Event.__init__(self)

    def write(self, text):
        print("어떤 write 호출될까요??")
        # super().write(text)
        # Group.write(self, text)


abcd = FacebookGroup("abcd")
abcd.join("수지")
abcd.join("아이유")

abcd.introduce()

abcd.create_event("한번에 훅가는 파이썬&장고 스터디")
abcd.show_events()

abcd.write("파이썬 공부합시다")

del abcd
