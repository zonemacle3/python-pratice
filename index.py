multiline = '''"life is too short"
you need python
'''
line = "you raise"
print(multiline)
print(multiline*2)
print(len(line))    
print(multiline[3])

print("I eat %d apples." % 3)


hate = "%10s" % "hi"
'          hi'

print(hate)

sqr = "%0.4f" % 3.141592
print(sqr)

number = 3
day = 4
form = "i eat {0} apples, so i was sick for {1} days".format(number,day)
print(form)

date = "{0:=^10}".format("hi")
print(date)

num = 3.141592
dd = "{0:0.4f}".format(num)
print(dd)

name = "홍길동"
age = "30"
z = f'나의 이름은 {name}입니다. 나이는 {age} 입니다.'
print(z)

print(form.count('a')) 

print(",".join('abcd'))
print(",".join(['a','b','c','d']))

a=[1,2,3]
print(a[0]+a[2])

a=[1,2,3,['a','b','c']]
print(a[0])

a=[1,2,3,4,5]
del a[0:2]
print(a)

b=[5,8,2,4,3,5,6,7,8,9,10]
b.sort()
print(b)
b.reverse()
print(b)


t1 = (1,2,'a','b')
t2 = (3,4)
t3 = t2*3
print(t3)
print(len(t1))

a={1:'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1,2,3]
print(a)

del a[1]
print(a)

grade = {'pey':10,'jullet':99}
print(grade['pey'])
print(grade['jullet'])

a={'name'  :'pey','phone':'010-9999-1234','birth':'1118'}
print(a.keys())
print(a.values())
print(a.items())
print(a.get('phone'))
print('name' in a)

s1 = set([1,2,3])
print(s1)
s2 = set("hello")
print(s2)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1&s2)
print(s1|s2)
print(s2-s1)

s1 = set([1,2,3])
s1.add(4)
print(s1)

s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

s1 = set([1,2,3])
s1.remove(2)
print(s1)


a=True
b=False
print(type(a))
print(type(b))
print(2<1)


pocket =['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어 가라') 

pocket=['paper', 'money', 'card']
if 'money' in pocket: pass
else: print('카드를 꺼내라')

score = 100
message = "success" if score >= 50 else "false"
print(message)

treehit=0
while treehit < 10:
    treehit += 1
    print("나무를 %d번 찍었습니다" % treehit)
    if treehit == 10: print("나무 넘어갑니다")


# prompt ="""
# 1. add
# 2. del
# 3. list
# 4. quit

# enter number : """

# number = 0
# while number != 4: 
#     print(prompt)
#     number = int(input())


# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee -= 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         coffee -= 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0: continue
#     print(a)

# while True:
#     print("dd")


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first,sec) in a:
    print(first+sec)

marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번의 학생은 합격입니다." % number)
    else:
        print("%d번의 학생은 불합격입니다." % number)


marks = [90,60,75,25,80,40]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다." % number)
    
a = range(1,11)
print(a)

add = 0
for i in range(1,11):
    add += i
    
print(add)


mark=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("%d번 축하합니다." % (number+1))


for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ") # end 매개변수에는 \n이 기본값으로 설정되있음 
    print('')

a=[1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

resu = [x*y for x in range(2,10)
            for y in range(1,10)]

print(resu)


def add(a,b):
    return a+b

a = 3
b = 4
c = add(a,b)
print(c)