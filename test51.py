 # match객체의 메서드
# group() 매치된 문자열을 리턴한다.
# start() 매치돤 문자열의 시작 위치를 리턴한다.
# end() 매치된 문자열의 끝 위치를 리턴한다.
# span() 매치된 문자열의 (시작,끝)에 해당되는 튜플을 리턴한다.

import  re
p = re.compile('[a-z]+')
m = p.match('python')
print(m.group())
print((m.start()))
print(m.end())
print(m.span())
