# Simple calculator program

while True:

   print("Enter 'add' to add two numbers")
   print("Enter 'sub' to subtract two numbers")
   print("Enter 'mul' to multiply two numbers")
   print("Enter 'div' to divide two numbers")
   print("Enter 'quit' to end the program")
   
   user_input = input("Entered options:\t")
   
# Convert the user input to upper case   
   user_input = user_input.upper()   
   
# Accept to two to perform calculation
   num1 = input("\nEnter number 1: ")
   num2 = input("\nEnter number 2: ")
   num1 = float(num1)
   num2 = float(num2)
       
# If user enters 'Quit'
if user_input == "QUIT":
    print("Program quited!")
    break
# If user enters 'Add'
elif user_input == "ADD":
    result = num1 + num2
    print("Addition of {0:.2f} and {1:.2f} is: {2:.2f}" .format(num1,num2,result))
    break
# If user enters 'Sub'    
elif user_input == "SUB":
    result = num1 - num2
    print("Subtraction of {0:.2f} and {1:.2f} is: {2:.2f}" .format(num1,num2,result))
    break
# If user enters 'Mul'    
elif user_input == "MUL":
    result = num1 * num2
    print("Multiplication of {0:.2f} and {1:.2f} is: {2:.2f}" .format(num1,num2,result))
    break
# If user enters 'Div'    
elif user_input == "DIV":
    if num2 <= 0:
        print("Not possible to divide a number by zero")
        break
    else:
        result = num1 / num2
        print("Division of {0:.2f} and {1:.2f} is: {2:.2f}" .format(num1,num2,result))
        break
else:
    print("Invalid input")
    break
