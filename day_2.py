#----------functions----------#

def greet():
    print("hello")

greet()

def welcome(name):
    print("hello",name)
welcome("parth")

def add(a,b):
    return a+b

result = add(5,3)
print(result)

def square(x):
    return x*x

sqre = square(4)
print (sqre)

def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

number = 4
print(even_odd(number))

def calculator(num1,num2,operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return  num1 * num2
    elif operation == "division":
        return num1 / num2
    else:
        return "invalid choice"
    
res = calculator(10,5, "add")
print(res)

#----------------------------------#

#----------loops-------------------#

for i in range(5):
    print(i)

for j in range(1,11):
    print(j)

for k in range(0,11,2):
    print(k)

fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

i = 1
while i <= 5:
    print(i)
    i += 1

for num in range(10):
    if num == 5:
        break
    print(num)
    
#----------------------------------------#

#-----------------lists----------------#

