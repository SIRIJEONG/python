from pdb import line_prefix


f = open("새파일.txt", "w")
# f를 오픈하고 새파일.txt를 만들고 w는 write의 의미이다.
# r 은읽기모드 기존의쓴 파일을 읽기만 가능할때 
# a 는 추가모드 이미 무언가 써져있는 파일이 있을때 무언가를 더 추가할때 
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

g = open("새파일.txt", 'r')
line = g.readline()
print(line)
g.close
# readline이라는 함수는 파일에서 한줄씩 읽어오는 함수 반드시 close를 해줘야한다.

h = open("새파일.txt", 'r')
while True:
    line = h.readline()
    if not line: break
    # 라인이 없을때 브레이크 해라 라는 뜻 
    print(line)
h.close
# 여러줄을 가져올떄 쓴다 

i = open("새파일.txt", 'r')
lines = i.readlines()
for line in lines:
    print(line)
i.close()
# readlines는 리스트 형태로 가져와서 출력하는 것. 출력될때는 한줄씩 띄어서 출력이 되는데 그것을 막으려면 print(line, end="")를 입력하면된다,
# 또는 print(line.strip("\n"))을 입력해도 똑같이 출력된다. .strip()이란 양쪽끝에서 특정 문자를 제거해주는 함수이다.
# 만일 한줄로 다 출력하고 싶다면 print(line.strip("\n"), end=" ")라고 입력하면 된다.


j= open("새파일.txt", 'r')
data = j.read()
print(data)
j.close
# read라는 함수는 통째로 읽어오는 함수이다.

with open("apple.txt","w") as k:
    k.write("show me the money")
# close 를 안쓰는 방법 
# apple.txt를 열어서 k라는 변수에 저장한다. 지역변수개념이라 벗어나게되면 자동으로 close된다.