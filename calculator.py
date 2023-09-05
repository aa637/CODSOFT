#python program for simple calculator
#function to add two numbers
def add(num1,num2):
    return  num1+num2
#function to substract two numbbers
def substract(num1,num2):
    return num1-num2
#function to multiply two numbers
def multiply(num1,num2):
    return num1*num2
#function to divide two numbers
def divide(num1,num2):
    return num1/num1
print("select the operation.")
print("a.Add")
print("b.substract")
print("c.multiply")
print("d.divide")
while True:
    #take  input from the user
    choice=input("Enter the choice(1/2/3/4):")
    #check if the choice is one of the four options
    if choice in('1','2','3','4'):
        try:
            num1=float(input("enter the first number:"))
            num2=float(input("Enter the second number:"))
        except ValueError :
            print("invalid input.please enter a number.")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",substract(num1,num2))
        elif choice=='3':
            print (num1,"*",num2,"=", multiply(num1, num2))
        elif choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))
#check if the user wants another calculation
#break while loop if answer is no
next_calculation=input("lets do next calculation?(yes/no):")
if next_calculation=="no":
    brake
else:
    print("Invalid Input")
