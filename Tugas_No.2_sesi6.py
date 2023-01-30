import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg='black')
window.geometry('500x500')
window.resizable(False, False)
window.title('Kalkulator Kalori')

input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill='x',expand=True)

nama_depan = ttk.Label(input_frame,text='Menghitung Kalori')
nama_depan.pack(padx=10,pady=10,fill='x',expand=True)

window.mainloop()

