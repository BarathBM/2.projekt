import tkinter as Tk
import random
import tkinter.font as tkFont

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

legjobb_ido=float('inf')
eltelt_ido=0
start_ido=0
target_szo=''
target_szin=''
max_szinek=1  # Alapértelmezett választási szám





def create_gui():
    global time_label, best_time_label, feedback_label, word_label, entry, dropdown, dropdown_menu, root
    root=Tk.Tk()
    root.title("Színválasztós")
    cimsor=Tk.Label(root, text="Színválasztó")
    myfont=tkFont.Font()
    root.mainloop()