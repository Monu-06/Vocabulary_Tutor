from tkinter import *
from project import values

root = Tk()
root.title('Vocabulary tutor')
root.geometry("700x700")
root.configure(background='gray27')

def submit():
    values(my_box1.get(),int(my_box2.get()))
    
read="""Welcome to Vocabulary Tutor,
this app allows you to set the timer.
You will be notified with an english
word and its meaning after every
specified time.Please fill the below
requirements to continue... """
my_label0 = Label(root, text=read, font=("Courier",18,"bold italic"),fg="light cyan",bg="gray27")
my_label0.pack(pady=20)

my_label1 = Label(root, text="Enter your name", font=("Helvetica",18),fg="gold",bg="gray27")
my_label1.pack(pady=20)
    
my_box1 = Entry(root)
my_box1.pack(pady=20)

my_label = Label(root, text="Set the timer (in sec)", font=("Times bold",18),fg = "gold",bg="gray27")
my_label.pack(pady=20)

my_box2 = Entry(root)
my_box2.pack(pady=20)

my_button = Button(root,text="Submit",fg='gray1', bg='PaleVioletRed1' ,activebackground='lawn green',command=submit)
my_button.pack(pady=50)
root.loop()


