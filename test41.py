# 외장함수 = 라이브러리에서 가져다 쓰는 함수 (import해서 쓰는 것)
from cmath import pi
import random
lotto = sorted(random.sample(range(1,46),6))
print(lotto)
# 로또 랜덤 번호 

import time
for i in range(5):
    print(i)
    time.sleep(1)
# 외장함수 time은 0부터 4까지 1초간격으로 출력 

import sys
print(sys.argv)

import pickle
f = open("text.txt",'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()
# 외장함수 pickle은 딕셔너리 같은 데이터를 덤프라는 명령어로 저장해서 언제든 딕셔너리 형태로 꺼내쓸수있다.

import time
print(time.time())
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간 초 

import webbrowser
webbrowser.open("http://google.com")