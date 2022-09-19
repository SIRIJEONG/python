 # 파이썬에서 정규 표현식을 지원하는 re모듈

import  re
p = re.compile('[a-z]+') #a부터 z까지 +(반복)
m = p.match('python')
print(m)
# 매치가 안되는것을 입력할 경우 none이 출력된다.