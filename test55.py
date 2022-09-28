 # 그루핑 ()
import re
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())
# 그루핑은 괄호를 이용하여 표현식을 묵어주는 것

import re
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))
# 매치 객체에서 따로 불러올수도 있다.

import re
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())
# \1 = 걸린게 한번더 반복된다 이기 떄문에 the the 가 걸린것이다.

# 그루핑된 문자열에 이름붙이기 ?P<name>
import re
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))
# ?P<원하는이름> 을하면 원하는 그룹에 이름을 붙여서 불러올수있다

import re
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('paris in the the spring').group())
# 특정 그룹에 이름을 붙이고 (?P=원하는이름)을 써서 뒷쪽에서 불러올수있다.

# 전방탐색 : 긍정형 (?=)
import re
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
# 검색조건에는 포함되나 결과에는 포함에 안돼기때문에 http만 출력이된다.

# 전방탐색: 부정형 (?!)
import re
p = re.compile(".*[.](?!bat$|exe$).*$", re.M)
l = p.findall("""
autoxec.exe
autoxec.bat
autoxec.jpg
""")
print(l)

# 문자열 바꾸기sub
import re
s = re.compile('(blue|blue|red)')
print(s.sub('colour', 'blue socks and red shoes'))

# Greedy vs Non-Greedy
import re
x = '<html><head><title>title</title>'
print(re.match('<.*>', x).group()) #greedy
print(re.match('<.*?>', x).group()) #non-greedy = 최소한으로 반복하겠다

