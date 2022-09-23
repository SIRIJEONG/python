 # 컴파일 옵션 , DOTALL, S

import re
# p = re.compile('a,b')
# m = p.match('a\nb')
# print(m)
# 로쓴다면 none으로 출력된다. Dot(.) = 줄바꿈 (₩n)을 제회한 모든 문자와 매치

p = re.compile('a.b',re.DOTALL) #re.S 라고 써도된다.
m = p.match('a\nb')
print(m)
# 줄바꿈이 있어도 매치할수 있도록 해주는 옵션이다.

# 컴파일 옵션 IGNORECASE,I
import re
p = re.compile('[a-z]',re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
# 대소문자를 무시하고 매칭할수 있도록 해주는 옵션이다.

# MULTILINE, M
import re
p = re.compile("^python\s\w+",re.M)
# ^ = 맨처음이라는 뜻 \s = 공백 \w = 알파벳,숫자,_중의 한문자
data = """python one
show me the money
python two
talk to me goose
python three"""

print(p.findall(data))
# re.M 은 ^를 맨처음만이아닌 각라인 처음으로 인식시키는 옵션이다.
