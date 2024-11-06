


from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.title("Registration Form")
window.geometry("400x400")





# Name
label_name = Label(window, text="Name:")
label_name.place(x=20, y=20)
entry_name = Entry(window)
entry_name.place(x=150, y=20)

# Age
label_age = Label(window, text="Age:")
label_age.place(x=20, y=60)
entry_age = Entry(window)
entry_age.place(x=150, y=60)

# Gender
label_gender = Label(window, text="Gender:")
label_gender.place(x=20, y=100)
gender_var = StringVar()
radio_male = Radiobutton(window, text="Male", variable=gender_var, value="Male")
radio_male.place(x=150, y=100)
radio_female = Radiobutton(window, text="Female", variable=gender_var, value="Female")
radio_female.place(x=220, y=100)

# Email
label_email = Label(window, text="Email:")
label_email.place(x=20, y=140)
entry_email = Entry(window)
entry_email.place(x=150, y=140)

# Phone Number
label_phone = Label(window, text="Phone Number:")
label_phone.place(x=20, y=180)
entry_phone = Entry(window)
entry_phone.place(x=150, y=180)

# Language
label_language = Label(window, text="Language:")
label_language.place(x=20, y=220)
entry_language = Entry(window)
entry_language.place(x=150, y=220)

# Register button
def show_message():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    email = entry_email.get()
    phone = entry_phone.get()
    language = entry_language.get()

    # Basic validation
    if name and age and gender and email and phone and language:
        messagebox.showinfo("Registration Successful", f"Thank you for registering, {name}!")
    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

register_button = Button(window, text="Register", command=show_message)
register_button.place(x=150, y=260)

# Run the Tkinter event loop
window.mainloop()






