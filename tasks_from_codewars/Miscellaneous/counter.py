from tkinter import *


def clear_txt_word():
    txt_word.delete(0, END)


def len_word():
    get_word = len(txt_word.get())
    lbl_len_word = Label(win, text=f"Количество символов: {get_word}")
    lbl_len_word.grid(column=1, row=3, columnspan=2, pady=5)


win = Tk()
win.title("Счетчик символов")
window_height = 150
window_width = 300
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
win.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
win.resizable(False, False)

lbl_title = Label(win, text=('Введите слово'),font=("Arial Bold",))
lbl_title.grid(column=1, row=0, pady=15, columnspan=2)

txt_word = Entry(win, width=30)
txt_word.grid(column=1, row=1, columnspan=2, padx=60)
txt_word.focus()

btn_len = Button(win, command=len_word, text=('Ввести'), height=1, width=8)
btn_len.grid(column=1, row=2, pady=5, padx=10, sticky='e')

btn_clear = Button(win, command=clear_txt_word, text=('Очистить'), height=1, width=8)
btn_clear.grid(column=2, row=2, pady=5, sticky='w')

win.mainloop()
