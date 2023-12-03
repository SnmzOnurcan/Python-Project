from tkinter import *

from tkinter import messagebox

pencere = Tk()

pencere.title("Liste oluşturma")
pencere.geometry("350x200")

# grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()

Lb1 = Listbox(uygulama)
Lb1.insert(1, "Python")
Lb1.insert(2, "C#")
Lb1.insert(3, "JAVA")
Lb1.insert(4, "JAVASCRIPT")
Lb1.grid(padx=110, pady=10)

# formu çiz
pencere.mainloop()