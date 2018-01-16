
f = open('README.md', 'r')
data = f.read()
print(data)

# 한줄 읽기
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)

# 파일을 전부 읽고 한줄 씩 리스트 아이템으로 읽기
lines = f.readlines()
for l in lines:
    print(l)

# for 문으로 1줄씩 순회 가능
for l in f:
    print(l)

f.close()

with open('README.md', 'r') as ff:
    for l in ff:
        print(l)

