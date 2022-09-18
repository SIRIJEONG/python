 # 정규표현식
# 주민번호의 뒷자리를 *문자로 변경하시오

import re
data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]{7}")
print(pat.sub("\g<1>-*******", data))