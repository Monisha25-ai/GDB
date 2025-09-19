for num in range(2, 100):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        if num%10 ==9:
            print(num)