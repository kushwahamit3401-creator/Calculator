def addition (x,y):
    return x+y
def subtraction (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y

print("Select Opration")
print("1.adition")
print("2.subtraction")
print("3.multiply")
print("4.divide")

while True :
    choice = input("Enter choice(1/2/3/4):")

    if choice in ("1","2","3","4"):
        try:
            num1= float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice =="1":
            print(num1,"+",num2,"=",addition(num1,num2))
        elif choice =="2":
            print(num1,"-",num2,"=",subtraction(num1,num2))
        elif choice =="3":
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice =="4":
            print(num1,"/",num2,"=",divide(num1,num2))
        next_calculation = input("Let's do next_calculation? (yes/no):")
        if next_calculation == "no":
            break
    else:
        print("Invalide Input")
