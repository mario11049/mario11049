num = int(input("enter the number to check: "))
temp = 0
for i in range(1 , num):
    if num % i == 0:
        temp += i
if num == temp:
    print("perfect number")
else:
    print("not a perect number")