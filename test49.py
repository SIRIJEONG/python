 # 파이썬에서 정규 표현식을 지원하는 re모듈

import  re
p = re.compile('[a-z]+') #a부터 z까지 +(반복)
m = p.match('python')
print(m)
# 매치가 안되는것을 입력할 경우 none이 출력된다.

import  re
p = re.compile('[a-z]+') #a부터 z까지 +(반복)
m = p.search('3 python')
print(m)

# match는 일치하지 구문이있다면 none으로 표시 되지만 search는 일치하지 않는 구문이 있어도 일치하는 구문을 찾는다.