# 1 variant
age=int(input('Please enter your age: '))
if age%2==0: #%2==0 формула четных чисел
    age=list(range(0,age+1)[::2])
    print('This is an even number: ',age)
else:
    age=list(range(0,age+1)[1::2])
    print('It is not an even number: ',age)

# 2 variant

age = int(input("Please enter your age: "))
n = 0
if age % 2 == 0:
    for n in range(2,age,2):
        print(n ,end=" ")
    print("")
else:
    for n in range(1,age,2):
        print(n ,end=" ")
print("")
for i in range(0, age, 1):
    print( i)
