import test34
print(test34.add(1,2))
# test34의 함수를 가져다 썼다.

from test34 import add
print(add(1,2))
# 여러함수에서 원하는것만 가져오고 싶을때는 이렇게 쓴다. 

import test34

# 만일 파일은 같은 공간에 없다면 
import sys
sys.path.append( )
# 괄호안에 파일경로를 써주면 된다.