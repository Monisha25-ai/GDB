i = 1
while i<=20:
    print(i)
    i += 1

for i in range (1,50):
    if(i % 2==0):
        print(i)
    else:
        continue

for i in range(1,10):
    print(f"{i} * 7 = {i*7}")

sum = 0
for i in range(1,101):
    sum += i
print(f"Sum of first {i} natural numbers is {sum}")


i = 10
while i>= 1:
    print(i)
    i -= 1

for i in range(1,30):
    if(i % 3==0):
        continue
    print(i)

fact = 0
num = int(input("Enter a number: "))
while num > 0:
    fact *= num
    num -= 1
print(f"Factorial of {num} is {fact}")

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")

num = int(input("Enter a number: "))
list = [10, 20, 30, 40, 50]
if num in list:
    print(f"{num} is present in the list")
else:
    print(f"{num} is not in the list")


#OR

for i in list:
    if i == num:
        print("Number found")
        break
    elif i not in list:
        print("Number not found")
        break


#CORRECT ORDER AND REVERSE ORDER
name = input("Enter your name: ")
print(f"Correct order : {name}")
#reverse order
for i in range(len(name)-1, -1,-1):#IF IN THE RANGE (-1,-1) 
    print(name[i], end="")

#PRIME NUMBERS FROM 1 TO 100 USING NESTED FOR LOOP 
for i in range(1, 101):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(i, end=" ")

#diamond pattern
rows = 5
for i in range(1,rows+1):
    print(" " * (rows - i ) + "*" * (2 * i - 1))
for i in range(rows-1,-1,-1):
    print(" " * (rows - i ) + "*" * (2 * i - 1))

n = 7  # size of the square
for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n - 1 or      # top/bottom border
            j == 0 or j == n - 1 or      # left/right border
            i == j or                    # main diagonal
            i + j == n - 1               # anti-diagonal
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


import random as rand
rand_num = rand.randint(1, 50)
guess = int(input("Guess a number between 1 and 50: "))
while guess!= rand_num:
    if guess < rand_num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 50: "))
print(f"Congratulations! You guessed the number {rand_num}.")

# 2 2d array sum
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr1 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
sum = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum.append(arr[i][j] + arr1[i][j])
#printing in matrix form
for i in range(len(arr)):
    print(sum[i*len(arr[i]):(i+1)*len(arr[i])])

#printing spiral traversal in number
# Note: The above code is not complete and will not print the spiral traversal correctly.
# To complete the spiral traversal, you need to modify the code as follows:
#code below prints the spiral traversal in number

n = 4
num = 1
direction = 0
rows = n
cols = n
while rows > 0 and cols > 0:
    if direction == 0:  # right
        for i in range(cols):
            print(num, end="  ")
            num += 1
        rows -= 1
    elif direction == 1:  # down
        for i in range(rows):
            print(num, end="  ")
            num += 1
        cols -= 1
    elif direction == 2:  # left
        for i in range(cols):
            print(num, end="  ")
            num += 1
        rows -= 1
    elif direction == 3:  # up
        for i in range(rows):
            print(num, end="  ")
            num += 1
        cols -= 1
    direction = (direction + 1) % 4
    print()
    
 



n=4
num =1

while True:
    if num%n !=0:
        print(num,end="  ")
        num += 1
    else:break
print(num,end="  ") 
print()

for i in range(n+1):
    for j in range((n),-1,-1):
        if j == n:
            print("  "*(n+1)+str(num))
            int(num)
            num += 1
        elif i == n:
            print("  "*j+str(num),end="")
