from math import pow
again = 'y'
while again == 'y':
    x=int(input('Enter first number: '))
    y=int(input('Enter second number: '))
    user_input=input("\n+\n-\n*\n/\npower\nChoose any of the above operators: ")
    # operator=("\n+\n-\n*\n/\n")
    if user_input == "+":
        print(x+y)
    elif user_input == "-":
        print(x-y)
    elif user_input == "*":
        print(x*y)
    elif user_input == "/":
        print(x/y)
    elif user_input == "power":
        print(pow(x,y))    
    else:
        print("Enter correct operator...")

    again=(input("If you want to continue then press y if no then press n: "))
