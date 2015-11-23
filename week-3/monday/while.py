a = 0

while a < 100 :
    print(a)
    a += 3


for x in  range(0, 100, 4):
    print(x)

numbers = [1,2,3,4,5]
a = 0

while len(numbers) > a:
        numbers[a] *= 2
        a += 1

print(numbers)

numbers = [1,2,3,4,5]
a = 0
summa = 0
while len(numbers) > a:
        summa += numbers[a]
        a += 1

print(summa)

numbers = [1,5,6,3,11,14,12]

i = 0

while i < len(numbers):
    if numbers[i] % 3 == 0:
        print(numbers[i])
        break
    i += 1

numbers = [1,2,3,4,5]

summa = 0
for n in numbers:
    summa += n

print(summa)


x = 1
while x < 100:

    if x % 5 == 0 and x % 3 == 0:
        print('FIZZBUZZ')
    elif x % 3 == 0:
        print('FIZZ')
    elif x % 5 == 0:
        print('BUZZ')
    else:
        print(x)
    x += 1

for x in range(0, 100, 1):

        if x % 5 == 0 and x % 3 == 0:
            print('FIZZBUZZ')
        elif x % 3 == 0:
            print('FIZZ')
        elif x % 5 == 0:
            print('BUZZ')
        else:
            print(x)

for x in range(0, 100, 1):

        if '3' in str(x) and '5' in str(x):
            print('FIZZBUZZ')
        elif '3' in str(x):
            print('FIZZ')
        elif '3' in str(x):
            print('BUZZ')
        else:
            print(x)


def prim():
    inte = 2113
    i = 2
    while inte > i:

        if inte % i == 0:
            print(i)
            print(inte, " nem prim")
            break
        elif inte-1 == i:
            print(inte, " primszám")
        i += 1

prim()

def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x > 1:
        return fibo(x-1) + fibo(x-2)

print("A 30", "-ik fibonacci ",fibo(30))

def fibolist(i):
    for x in range(2, i+1, 1):
        print("Az ", x ,"-ik fibonacci ",fibo(x))

fibolist(35)
