#Control statements

num = 0

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")
 
#python5#
 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the seconf munber: "))

if num1 > num2:
    print(num1, "is greater than" , num2)
elif num2 > num1:
    print(num2, "is greater than" , num1)
else:
    print("Both numbers are equal")