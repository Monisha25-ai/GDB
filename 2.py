name = "vikas s"
age = 21
hobby = "Listening to music"
print(f"Hi , {name.title()}! I am {age} years old and my hobby is {hobby}.")

#swapping two numbers
a = 5
b = 10
print(f"Before swapping, a = {a} and b = {b}")
a, b = b, a
print(f"After swapping, a = {a} and b = {b}")

#Converting the data type
a = 3.0
print(f"The data type of a is {type(a)}")
a = int(a)
print(f"The data type of a after converting is {type(a)}")

b = "123"
print(f"The data type of b is {type(b)}")
b = int(b)
print(f"The data type of b after converting is {type(b)}")

#area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area}")

#converting temperature from celsius to fahrenheit
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

#age calculation
current_year = 2025
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"You are {age} years old.")

#SUM,DIFFERENCE, PRODUCT, AND QUOTIENT
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2!=0:
    quotient = num1 / num2
else:
    "Error: Division by zero"
print(f" Sum: {sum}\n", f"Difference: {difference}\n", f"Product: {product}\n", f"Quotient: {round(quotient,2)}\n")

# List practice
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print(f"{fruits[0]}, {fruits[2]}, {fruits[4]}")
fruits[1] = "grape"
print(fruits)
fruits.append("pineapple")
print(fruits)
fruits.insert(2, "watermelon")
print(f"Updated list: {fruits}")
fruits.remove("mango")
print(f"{fruits}")
fruits.pop()
print(f"Updated list after popping: {fruits}")
fruits.sort()
print(f"Sorted list:  {fruits}")
fruits.reverse()
print(f"Reversed list: {fruits}")

#list of 5 favorite movies
movies = ["The Shawshank Redemption", "The Godfather", "Pulp Fiction", "The Dark Knight", "Eternal Sunshine of the Spotless Mind"]
print(f"5 favorite movies are: {movies}")
new_movie = input("Enter a new favorite movie: ")
movies.append(new_movie)
print(f"Updated list of favorite movies: {movies}")
movies.remove(movies[2])
print(f"Updated list after removing a movie: {movies}")

# a fun project shopping cart
items = []
print("Hi!, add 5 items to your shopping cart.")
for i in range(5):
    item = input(f"Enter item {i+1}: ")
    items.append(item)
print(f"Items in your cart: {items}")
removal_item = input(print("Now specifiy the item you want to remove:"))
items.remove(removal_item)
print(f"Updated cart: {items}")

#student marks program
students_marks = []
print("Enter the marks of 5 students:")
for i in range(5):
    mark = int(input(f"Enter marks of student {i+1}: "))
    students_marks.append(mark)
print(f"Marks of the students: {students_marks}")
total_marks = sum(students_marks)
average_marks = total_marks / len(students_marks)
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks}")

highest_mark = max(students_marks)
lowest_mark = min(students_marks)
print(f"Highest mark: {highest_mark} and Lowest mark: {lowest_mark}")