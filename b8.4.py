from tkinter import *
tk = Tk()
tk.title("xin chao den voi likegeeks app")
tk.geometry('400x250')
lbl = Label(tk, text="xin chao!")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="ban da bam vao nut nay!!")
btn = Button(tk, text="click me", command=clicked)
btn.grid(column=1, row=0)
tk.mainloop()
