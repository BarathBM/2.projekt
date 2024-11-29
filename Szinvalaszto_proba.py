import tkinter as Tk
import random
import tkinter.font as tkFont
root=Tk.Tk()
root.title("Színválasztós")
cimsor=Tk.Label(root, text="Színválasztó")
myfont=tkFont.Font()





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

root.mainloop()