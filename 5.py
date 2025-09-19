#Topic: functions in Python(indetailed)
def say_hello():
    print("Hello, world!")
    print("This is my first function!")
    return

say_hello()

#function with argument
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Vikas")

#function with multiple arguments
def calculate_sum(a, b):
    return a + b

result = calculate_sum(5, 10)
print(result)

#function with default argument
def greet_person_with_default(name="World"):
    print(f"Hello, {name}!")

greet_person_with_default()
greet_person_with_default("Vikas")

#function with variable number of arguments
def greet_people(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_people("Vikas", "Harsha", "Arjun")


#global variable and local variable


def increment_local_variable(local_variable):
    local_variable += 1
    print(f"Local variable after increment: {local_variable}")
    return local_variable

local_variable = 10
increment_local_variable(local_variable)
print(f"Local variable after increment: {local_variable}")

def spam():
    print(spam)
    eggs = "spam"

eggs = "global"
spam()

#simple calculator
def calculator(fun,num1,num2):
    if (fun.upper() == "ADD"):
        return num1+num2
    elif (fun.upper() == "Subtract"):
        return num1-num2
    elif (fun.upper() == "Multiply"):
        return num1*num2
    elif (fun.upper() == "Divide"):
        try:
            return num1/num2
        except ZeroDivisionError:
            return "Error: Division by zero"
        
print("if you want to divide, please do not enter zero for second number! ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

fun = input("Enter the operation to perform (Add, Subtract, Multiply, Divide): ")
result = calculator(fun,num1,num2)
print(f"Result: {result}")

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num = int(input("Enter a number to calculate its factorial: "))
value = fact(num)
print(f"Factorial of {num} is: {value}")

cat =[]
while True:
    name = input(f"Enter the name of the {len(cat)+1} cat (or press Enter to finish): ")
    if name == "":
        break
    cat = cat + [name]
print(f"The cat names are: {', '.join(cat)}")
