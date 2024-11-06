# from tkinter import*
# window=Tk()
# window.tittle("calculator")
# window.geometry("64x300")
# a=StringVar()
# en1=Entry(window, width=42,bd=5, textvariable=a)




# from tkinter import *
# x = Tk()

# x.title("Calculator")
# x.geometry("278x300")
# a = StringVar()
# e1 = Entry(x, width=42, bd=5, textvariable=a)
# e1.grid(row=0, columnspan=4)
# result_shown = False

# def clear():
#     global result_shown
#     a.set("")
#     result_shown = False

# def click(y):

#     global result_shown
#     c = a.get()

#     if result_shown:
#         if y in "+-*/%":
#             a.set(c + y)  
#         else:
#             a.set(y)
#         result_shown = False
#         return

#     if c == "0":
#         a.set(y)
   
#     else:
#         a.set(c + y)


# def equal():
#     global result_shown
#     z = a.get()
#     z = z.replace('+0', '+').replace('-0', '-').replace('*0', '*').replace('/0', '/')
#     f = eval(z)
#     a.set(f)
#     result_shown = True

            
  

# def backspace():
#     c = a.get()
#     a.set(c[:-1])

# # Update button bindings without passing extra arguments
# b1 = Button(x, text="clear", bg="black", fg="white", height=3, width=8, command=clear)
# b1.grid(row=1, column=0)
# b2 = Button(x, text="<", bg="black", fg="white", height=3, width=8, command=backspace)  # backspace
# b2.grid(row=1, column=1)
# b3 = Button(x, text="%", bg="black", fg="white", height=3, width=8, command=lambda: click('%'))
# b3.grid(row=1, column=2)
# b4 = Button(x, text="/", bg="black", fg="white", height=3, width=8, command=lambda: click('/'))
# b4.grid(row=1, column=3)

# b1 = Button(x, text="7", bg="black", fg="white", height=3, width=8, command=lambda: click('7'))
# b1.grid(row=2, column=0)
# b2 = Button(x, text="8", bg="black", fg="white", height=3, width=8, command=lambda: click('8'))
# b2.grid(row=2, column=1)
# b3 = Button(x, text="9", bg="black", fg="white", height=3, width=8, command=lambda: click('9'))
# b3.grid(row=2, column=2)
# b4 = Button(x, text="*", bg="black", fg="white", height=3, width=8, command=lambda: click('*'))
# b4.grid(row=2, column=3)

# b1 = Button(x, text="4", bg="black", fg="white", height=3, width=8, command=lambda: click('4'))
# b1.grid(row=3, column=0)
# b2 = Button(x, text="5", bg="black", fg="white", height=3, width=8, command=lambda: click('5'))
# b2.grid(row=3, column=1)
# b3 = Button(x, text="6", bg="black", fg="white", height=3, width=8, command=lambda: click('6'))
# b3.grid(row=3, column=2)
# b4 = Button(x, text="-", bg="black", fg="white", height=3, width=8, command=lambda: click('-'))
# b4.grid(row=3, column=3)

# b1 = Button(x, text="1", bg="black", fg="white", height=3, width=8, command=lambda: click('1'))
# b1.grid(row=4, column=0)
# b2 = Button(x, text="2", bg="black", fg="white", height=3, width=8, command=lambda: click('2'))
# b2.grid(row=4, column=1)
# b3 = Button(x, text="3", bg="black", fg="white", height=3, width=8, command=lambda: click('3'))
# b3.grid(row=4, column=2)
# b4 = Button(x, text="+", bg="black", fg="white", height=3, width=8, command=lambda: click('+'))
# b4.grid(row=4, column=3)

# b1 = Button(x, text="+/-", bg="black", fg="white", height=3, width=8, command=lambda: click(''))
# b1.grid(row=5, column=0)
# b2 = Button(x, text="0", bg="black", fg="white", height=3, width=8, command=lambda: click('0'))
# b2.grid(row=5, column=1)
# b3 = Button(x, text=".", bg="black", fg="white", height=3, width=8, command=lambda: click('.'))
# b3.grid(row=5, column=2)
# b4 = Button(x, text="=", bg="black", fg="white", height=3, width=8, command=equal)
# b4.grid(row=5, column=3)

# x.mainloop()



























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
