f = open("새파일.txt", "w")
# f를 오픈하고 새파일.txt를 만들고 w는 write의 의미이다.
# r 은읽기모드 기존의쓴 파일을 읽기만 가능할때 
# a 는 추가모드 이미 무언가 써져있는 파일이 있을때 무언가를 더 추가할때 
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

