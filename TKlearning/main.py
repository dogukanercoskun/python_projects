import tkinter


window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=450, height=450)


#label
my_label = tkinter.Label(text="Bu bir etiket", font=("Arial",30, "bold"))
my_label.config(bg="black", fg="white")
my_label.pack()

#button

def click_button():
    user_input = my_entry.get()
    print(user_input)

my_button=tkinter.Button(text="Bu bir buton", command=click_button)
my_button.pack()

#Entry

my_entry = tkinter.Entry(width=20)
my_entry.pack()

window.mainloop()