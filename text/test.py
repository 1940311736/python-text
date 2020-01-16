print("hello world")
print("100+300=",100+300)
age =3
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')


height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi <18.5:
    print('过轻')
elif bmi>=18.5 and bmi<=25:
    print('正常')
elif bmi>25 and bmi<=28:
    print('过重')
elif bmi>28 and bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')


sum = 0
for i in range(101):
    sum = sum +i
    print(sum)

    n = 1
    while n<=100:
        print(n)
        n=n+2
        print('end')

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

    print(my_abs(52))


def power(x):
    return x*x
print(power(5))


def lld(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
        return s
    print(lld(6,2))


extra = {'city':'lps','job':'text'}


def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
    person('jack', 24, **extra)
