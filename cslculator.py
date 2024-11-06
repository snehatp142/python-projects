
from tkinter import *

# Initialize main window
x = Tk()
x.title("Calculator")
x.geometry("278x300")

# Entry widget to display inputs and results
a = StringVar()
e1 = Entry(x, width=42, bd=5, textvariable=a)
e1.grid(row=0, columnspan=4)
result_shown = False

def clear():
    global result_shown
    a.set("")
    result_shown = False

def click(y):
    global result_shown
    current = a.get()
    
    # Prevent multiple operators in a row
    if result_shown:
        if y in "+-*/%":
            a.set(current + y)
        else:
            a.set(y)
        result_shown = False
        return

    # Restrict alphabetic input
    if y.isalpha():
        a.set("Error: No letters allowed")
        result_shown = True
        return

    # Check for consecutive operators and prevent
    if current and current[-1] in "+-*/%" and y in "+-*/%":
        a.set("Error: Invalid Expression")
        result_shown = True
        return

    # Update the input field
    a.set(current + y)

def equal():
    global result_shown
    expression = a.get()
    
    # Handle invalid expressions
    try:
        # Remove unnecessary leading zeros after operators
        expression = expression.replace('+0', '+').replace('-0', '-').replace('*0', '*').replace('/0', '/')
        result = eval(expression)  # Evaluate the expression
        a.set(result)  # Display the result
    except:
        a.set("Error: Invalid Expression")  # Error message for invalid inputs
    result_shown = True

def backspace():
    current = a.get()
    if len(current) > 0:
        a.set(current[:-1])

# Create buttons
buttons = [
    ("clear", clear, 1, 0), ("<", backspace, 1, 1), ("%", lambda: click('%'), 1, 2), ("/", lambda: click('/'), 1, 3),
    ("7", lambda: click('7'), 2, 0), ("8", lambda: click('8'), 2, 1), ("9", lambda: click('9'), 2, 2), ("*", lambda: click('*'), 2, 3),
    ("4", lambda: click('4'), 3, 0), ("5", lambda: click('5'), 3, 1), ("6", lambda: click('6'), 3, 2), ("-", lambda: click('-'), 3, 3),
    ("1", lambda: click('1'), 4, 0), ("2", lambda: click('2'), 4, 1), ("3", lambda: click('3'), 4, 2), ("+", lambda: click('+'), 4, 3),
    ("+/-", lambda: click('-'), 5, 0), ("0", lambda: click('0'), 5, 1), (".", lambda: click('.'), 5, 2), ("=", equal, 5, 3),
]

# Add buttons to grid
for (text, command, row, col) in buttons:
    Button(x, text=text, bg="black", fg="white", height=3, width=8, command=command).grid(row=row, column=col)

# Run the calculator application
x.mainloop()
