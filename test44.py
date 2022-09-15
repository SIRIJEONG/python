 # 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지수를 출력하는 프로그램
  # 게시판 페이징

def page(m,n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(page(5, 10))
print(page(15, 10))
print(page(25, 10))
print(page(30, 10))