from tkinter import * #pyhton's GUI library for interacting with icons
import random #to randomize password

def generate():
    password = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numeric = "1234567890"
    characters = "!@#$%^&*~,.+-*<>?/"
    
    #converting to arrays
    weakArray = list(alphabet) 
    mediumArray = list(alphabet + numeric)
    strongArray = list(alphabet + numeric + characters)
    
    #getting variables from user input
    strengthVal = strength.get() #gets from radial button option
    password_length = int(length.get()) #gets from length entry
    
    #generating password
    #join concats to password
    
    if strengthVal == 1:
        password = ''.join(random.choice(weakArray) for _ in range(password_length))
    elif strengthVal == 2:
        password = ''.join(random.choice(mediumArray) for _ in range(password_length))
    elif strengthVal == 3:
        password = ''.join(random.choice(strongArray) for _ in range(password_length))
        
    #showing in Entry
    showPassword.delete(0, END)
    showPassword.insert(0, password)

#allows you to copy password to cliboard
def copy_password():
    password = showPassword.get() #gets from entry field
    window.clipboard_clear()
    window.clipboard_append(password)

window = Tk() #window for display
window.config(bg='white') #properties

heading = Label(window, text='Generate a Password!', font=('cursive', 50, 'italic'), bg='white')
heading.grid(pady=10) #allows you to see in window

strength = IntVar()
weak = Radiobutton(window, text='Weak', value=1, variable=strength, width=30, fg='black', bg='white', font=('times new roman', 35))
medium = Radiobutton(window, text='Medium', value=2, variable=strength, width=30, fg='black', bg='white', font=('times new roman', 35))
strong = Radiobutton(window, text='Strong', value=3, variable=strength, width=30, fg='black', bg='white', font=('times new roman', 35))

weak.grid(pady=10)
medium.grid(pady=10)
strong.grid(pady=10)

length_label = Label(window, text='Enter desired length of password', width=30, bg='black', fg='white', font=('times new roman', 35), )
length_label.grid(pady=5)

length = Spinbox(window, from_=3, to=30, width=30, fg='black', bg='white', font=('times new roman', 35))
length.grid(pady=5)

generate_button = Button(window, text='Generate Password', command=generate, width=30,bg='black', fg='white', font=('times new roman', 35))
generate_button.grid(pady=5)

copy_button = Button(window, text='Copy Password', command=copy_password, width=30, bg='black', fg='white', font=('times new roman', 35))
copy_button.grid(pady=5)

showPassword = Entry(window, width=30, bg='black', fg='white', font=('times new roman', 40))
showPassword.grid()

window.mainloop() #allows you to see it while it runs aka it loops
