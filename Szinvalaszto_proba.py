import tkinter as Tk
import random
import tkinter.font as tkFont
root=Tk.Tk()
root.title("Színválasztós")
cimsor=Tk.Label(root, text="Színválasztó")
myfont=tkFont.Font()
szin=Tk.Entry()




szinek=['kék', 'piros', 'zöld', 'sárga', 'narancs', 'rózsaszín', 'lila']
szinek_tömb={
    'kék':'blue',
    'piros':'red',
    'zöld':'green',
    'sárga':'yellow',
    'narancs':'orange',
    'rózsaszín':'pink',
    'lila':'purple'
    }
time_label = Tk.Label(root, text="Eltelt idő: 0", font=("Arial", 16))
time_label.pack(pady=10)
    
best_time_label = Tk.Label(root, text="Legjobb idő: Nincs", font=("Arial", 16))
best_time_label.pack(pady=10)
    
feedback_label = Tk.Label(root, text="", font=("Arial", 16), fg="red")
feedback_label.pack(pady=10)
    
word_label = Tk.Label(root, text="", font=("Arial", 24), width=20)
word_label.pack(pady=10)
    
entry = Tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

root.mainloop()