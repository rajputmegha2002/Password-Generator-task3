from tkinter import*
import  random 
import string

cube = Tk()
cube.geometry("400x300")
cube.title("Password Generator")
label=Label(cube, text="Password Generator",fg="black", font="lucida 15 bold")
label.grid()

passstr=StringVar()
len=IntVar()

def get_pass():
    s1=string.ascii_letters + string.digits +string.punctuation
    password =""

    for x in range(len.get()):
        password=password +random.choice(s1)
        passstr.set(password)

def reset_pass():
    passstr.set("")

def accept_pass():
    passstr.set(" Password Accepted")    


label1=Label(cube, text="  Enter your Username", fg="blue", font="lucida 10")
label1.grid( row=1,column=0,padx=5,pady=10)
name=Entry(cube,fg="black",font="ludica 10 bold" )
name.grid( row=1,column=2,padx=10,pady=10)

label1=Label(cube, text="Enter Length of Password", fg="blue", font="lucida 10")
label1.grid( row=2,column=0,padx=8,pady=10)
name1=Entry(cube,textvariable=len, fg="black",font="ludica 10 bold" )
name1.grid( row=2,column=2,padx=10,pady=10)



label1=Label(cube, text="Generated Password", fg="blue", font="lucida 10")
label1.grid( row=3,column=0,padx=8,pady=10)
name=Entry(cube,textvariable=passstr,fg="black",font="ludica 10 bold" )
name.grid( row=3,column=2,padx=10,pady=1)


button=Button(cube,text="Generate Password", command=get_pass, bg="black",fg="white",font="lucida 10 bold")
button.grid(row=4,column=2,padx=10,pady=10)
button=Button(cube,text="Accept",command=accept_pass,fg="black",bg="white",font="lucida 10 bold")
button.grid(row=5,column=2,padx=10,pady=10)
button=Button(cube,text="Reset",command=reset_pass,fg="black",bg="white",font="lucida 10 bold")
button.grid(row=6,column=2,padx=10,pady=10)


cube.mainloop()

