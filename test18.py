test_list = ['one' , 'two' , 'three']
for i in test_list:
    print(i)
# for(반복문) 리스트

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
# for(반복문) 튜플

marks = [90, 25, 67, 45, 80]
number = 0
for mark in  marks:
    number = number + 1
    if mark >= 60:
        print("%d번 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)