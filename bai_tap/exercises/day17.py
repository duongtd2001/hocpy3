import tkinter as tk


def yes_click():
    root.destroy()


def no_click():
    pass


root = tk.Tk()
root.title('Bài tập 17')
root.geometry('480x320+640+200')
root.resizable(False, False)
root.config(bg='#99D9EA')

lbl = tk.Label(root, text='Hê sờ lô - Hơ sờ ly ly', bg='white', fg='red')
lbl.grid(row=0, column=0, padx=(180, 0), pady=(75, 0))

yes_button = tk.Button(text='Yes', command=yes_click, bg='white', fg='green')
yes_button.grid(row=1, column=0, padx=(0, 0), pady=(75, 0))
no_button = tk.Button(text='No', command=no_click, bg='white', fg='green')
no_button.grid(row=1, column=0, padx=(320, 0), pady=(75, 0))

root.mainloop()
