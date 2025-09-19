
for i in range (0,100):
    if i<=1:
        continue
    else:
        for j in range(2,int(i**0.5)+1):#why we increment by 2 is because even numbers are not prime
            if i%j!=0:
                continue
            else:
                break
        else:
            print(i)#how works

#prime number easy way
for num in range(2, 100):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        if num%10 ==9:
            print(num)
