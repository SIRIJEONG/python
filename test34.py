# 모듈 - 미리만들어 놓은 .py 파일(함수 , 변수 , 클래스)
#test34.py
def add(a,b):
    return a+ b

def sub(a,b):
    return a - b

if __name__ == "__main__":
    print(add(1,4))
    print(add(2,7))
# 언더바 name이 언더바 main 이랑 일치할때 실행해라 라는 뜻 
# 이걸쓰지않고 test35에서 오로지 import test34를 가져다 쓴다면 프린트까지 실행되어 5와 9가 출력될것이다.