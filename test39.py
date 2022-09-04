try:
    4/0
except ZeroDivisionError as e:
    print(e)

# 4/0만 하면 ZeroDivisionError라는 애러가 뜬다 
# 그렇기 때문에 try로 애러를 쓰고 except에 ZeroDivisionError를 미리 잡아주면 print했을때 애러의 종류가 출력된다.

try:
    f = open('none', 'r')
except FileExistsError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

# 파일이 없다면 e 출력
# 하지만 try에 오류가 없다면 else를 실행 

a = open('apple.txt', 'w')
try:
    # 무언가를 실행한다.
    data = a.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close
# 파일을 처음 열었을때 닫아주기 위해 finally 사용 
# 어떤 오류가 발생할지 모를때는 Exception 을 사용한다.