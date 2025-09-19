arr = [1,2,3,4,5]
left_product = [1]
right_product = [1]
for i in range (len(arr)-1):
    left_product.append(left_product[-1]*arr[i])
for j in range (len(arr)-1,0,-1):
    right_product.append(right_product[-1]*arr[j])
right_product = right_product[::-1]
sum_product = []
for k in range (len(arr)):
    sum_product.append(left_product[k]*right_product[k])  
while True:    
    in1 = int(input("enter the position to find the product: "))
    if in1>len(arr) or in1<=0:
        print("enter correct position")
        continue
    else:
        print(sum_product[in1-1])# Product of array except self without using division
        break
