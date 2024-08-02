#import sys includes the sys module in your script. The sys module provides access to some variables and functions that interact with the Python interpreter and the system.
import sys
#The below are Python Arithmetic Operators: They are used with numeric values to perform common mathematical operations. 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
#Error does not allow any item to be divided by error. If item id divided by 0 an Error will occur.
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
#Def is a keyword to define a function - in the case a calculator. Then prints the name of the calculator and also defines how to exit the calculator. 
def calculator():
    print("Karin's Sol-Tech Sakrekenaar")
    print("Tik 'verlaat' om te stop.")
#While true creates an infinite loop until that will run until it is explicitly broken out of using a break statement or some other exit condition within the loop. 
    while True:
        # Get user input
        user_input = input("Voer berekening in (e.g., 2 + 2 * 3 - 1): ")
#Below is the exit condition that will break the infinite loop that was created at while true. 
        # Exit condition
        if user_input.lower() == 'verlaat':
            print("U verlaat die sakrenenaar. Totsiens!")
            break
#try defines a block of code that will be tested for errors during execution. If an error occurs in the try block, it will be caught and handled by the corresponding except block. 
        try:
            # Evaluate the expression
            result = eval(user_input)
            print("Resultaat:", result)
        except Exception as e:
            print("Error:", e)
#if is a conditional statement used to execute a block of code, when the specified condition is true. 
if __name__ == "__main__":
    sentinel = True
#while sentinel loop is a loop that continues to run until it encounters a specific condition, known as the sentinel value. The loop will keep running until the sentinel value is encountered, at which point the loop will terminate.
#if ja/j keep being enterred the loop calculator will continue, if nee/n is entered the loop will terminate.
    while sentinel:
        calculator()
        user_response = input("Wil jy nog 'n berekening doen? (ja/nee): ")
        if user_response.lower() not in ['ja', 'j']:
            sentinel = False
            print("Totsiens!")