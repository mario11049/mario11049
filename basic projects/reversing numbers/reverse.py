num = int(input("enter the number you want to reverse: "))
temp = 0
while num > 0:
    digit = num % 10
    temp = temp * 10 + digit
    num = num // 10
print(temp)