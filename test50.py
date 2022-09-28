import  re
p = re.compile('[a-z]+')
m = p.findall('show me the money')
print(m)
# findall은 일치하는것이 있으면 찾아서 출력해준다

import  re
p = re.compile('[a-z]+')
m = p.finditer('show me the money')
for r in m:
    print(m)

