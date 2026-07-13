import math
print("1. addition(+)")
print("2. subscration(-)")
print("3. multiplication(*)")
print("4. division(/)")
print("5. power(^2)")
print("6. square root")
print("7. percentage(%)")
print("8. exit")
choice = input("choose from(1-8): ")
if choice == "1":
    num1 = float(input("enter number 1 : "))
    num2 = float(input("enter number 2 : "))
    print(num1 + num2)
elif choice == "2":
    num1 = float(input("enter number 1 : " ))
    num2 = float(input("enter number 2 : " ))
    print(num1 - num2)
elif choice == "3":
    num1 = float(input("enter number 1 : "))     
    num2 = float(input("enter number 2 : "))
    print(num1 * num2)
elif choice == "4":
    num1 = float(input("enter number 1 : "))
    num2 = float(input("enter number 2 : "))
    print(num1 / num2)
elif choice == "5":
     num1 = float(input("enter number 1 : "))
     num2 = float(input("enter number2 : "))
     print(num1 ** num2)
elif choice == "6":
    num1 = float(input("enter number : "))
    print( math.sqrt(num1))
elif choice == "7":
    num1 = float(input("enter number 1 : "))
    num2 = float(input("enter the total number : "))
    print(num1 / num2 * 100,"%")
elif choice == "8": 
    print("thanck you for using my calculator!!!")
else: 
    print("invalid option selected!!!")