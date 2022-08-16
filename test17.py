treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")

# while 반복문 

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중단합니다")
        break
    # 커피가 0개가 되었을때 0은 false이므로 not coffee는 true가 된다. 계속 반복되다가 break를 만나면 반복을 중지하고 벗어난다.

    a = 0
    while a < 10:
        a = a + 1
        if a % 2 == 0:
            continue
        print(a)
    # 홀수구분하는법 
