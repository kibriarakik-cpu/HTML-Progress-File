str="Argentina"
for char in str:
    print(char)
for i in range( 1, 11):
    print(i)
    print(f"Square of {i} is {i*i}")
    print(f"23 times {i} is {23*i}")
n=int(input("Enter the number of rows: "))
num=int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j,"*", end=" ")
    print()
total_sum=0
num=1
while num<=10:
    total_sum+=num
    num+=1  
print("The sum of first 10 natural numbers is:", total_sum)