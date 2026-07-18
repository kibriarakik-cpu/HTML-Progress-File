str="Argentina"
for char in str:
    print(char)
for i in range( 1, 11):
    print(i)
    print(f"Square of {i} is {i*i}")
    print(f"23 times {i} is {23*i}")
n=int(input("Enter the number of rows: "))
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