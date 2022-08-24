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