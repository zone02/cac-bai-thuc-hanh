import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
v.set(1)
language =[
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("c",5)
]

def ShowChoice():
    print(v.get())

tk.Label(root, text ="""choose your favourite programing language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(language):
    tk.Radiobutton(root, text = language,indicatoron = 0, width = 20, padx = 20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)
root.mainloop()
