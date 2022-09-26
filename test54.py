 # 메타문자 |
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
# | = or 이라는 뜻

# 메타문자 ^
import re
print(re.search('^Life','Life is too short'))
print(re.search('^Life','My Life'))
# ^ = 맨처음 이라는 뜻

# 메타문자 $
import re
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))
# $ = 맨끝이라는 뜻

# 메타문자 \b
import re
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))
# \b = 공백이라는 뜻

