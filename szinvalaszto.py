import tkinter as tk
import random
import time

# Globális változók
colors = ['piros', 'kék', 'zöld', 'sárga', 'narancs', 'lila', 'rózsaszín']
color_dict = {
    'piros': 'red',
    'kék': 'blue',
    'zöld': 'green',
    'sárga': 'yellow',
    'narancs': 'orange',
    'lila': 'purple',
    'rózsaszín': 'pink'
}

best_time = float('inf')
elapsed_time = 0
start_time = 0
target_word = ''
target_color = ''
max_colors = 1  # Alapértelmezett választási szám

# GUI elemek
def create_gui():
    global time_label, best_time_label, feedback_label, word_label, entry, dropdown, dropdown_menu, root
    root = tk.Tk()
    root.title("Színválasztó Játék")
    
    # Idő címkék
    time_label = tk.Label(root, text="Eltelt idő: 0", font=("Arial", 16))
    time_label.pack(pady=10)
    
    best_time_label = tk.Label(root, text="Legjobb idő: Nincs", font=("Arial", 16))
    best_time_label.pack(pady=10)
    
    feedback_label = tk.Label(root, text="", font=("Arial", 16), fg="red")
    feedback_label.pack(pady=10)
    
    word_label = tk.Label(root, text="", font=("Arial", 24), width=20)
    word_label.pack(pady=10)
    
    entry = tk.Entry(root, font=("Arial", 16))
    entry.pack(pady=10)
    
    entry.bind("<Return>", check_answer)
    
    dropdown_label = tk.Label(root, text="Hány szín jelenjen meg?", font=("Arial", 16))
    dropdown_label.pack(pady=10)
    
    dropdown = tk.StringVar(root)
    dropdown.set('1')  # Alapértelmezett érték
    dropdown_menu = tk.OptionMenu(root, dropdown, '1', '2', '3', '4')
    dropdown_menu.pack(pady=10)
    
    new_game_button = tk.Button(root, text="Új játék", command=new_game, font=("Arial", 16))
    new_game_button.pack(pady=10)

    # A dropdown menü változtatásának kezelése
    dropdown.trace('w', update_max_colors)

    # Automatikusan új játék kezdése az alkalmazás indításakor
    new_game()

    root.mainloop()

# A dropdown menü figyelése és a max_colors frissítése
def update_max_colors(*args):
    global max_colors
    max_colors = int(dropdown.get())  # Frissíti a max_colors értéket
    new_game()  # Új játék indítása, hogy figyelembe vegye az új színválasztást

def new_game():
    global target_word, target_color, start_time, elapsed_time, max_colors
    
    # Véletlenszerű szín és szó beállítása
    target_word = random.choice(colors)
    
    # Véletlenszerűen kiválasztunk annyi színt, amennyi a kiválasztott szám
    possible_colors = random.sample(colors, max_colors)
    
    # A cél színe benne van a kiválasztott színek között
    target_color = random.choice(possible_colors)
    
    # Véletlenszerű szín és szó beállítása
    word_label.config(text=target_word, fg=color_dict[target_color])
    
    # Eltelt idő és visszajelzés nullázása
    elapsed_time = 0
    time_label.config(text="Eltelt idő: 0")
    feedback_label.config(text="")
    
    # Induljon a számláló
    start_time = time.time()

def check_answer(event=None):
    global best_time, elapsed_time
    
    user_input = entry.get().strip().lower()
    
    if user_input == target_color:
        # Ha a válasz helyes
        elapsed_time = time.time() - start_time
        time_label.config(text=f"Eltelt idő: {elapsed_time:.2f} másodperc")
        
        # Frissítjük a legjobb időt
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_time_label.config(text=f"Legjobb idő: {best_time:.2f} másodperc")
            
        feedback_label.config(text="Helyes válasz!", fg="green")
    else:
        feedback_label.config(text="Hibás válasz, próbáld újra!", fg="red")
    
    entry.delete(0, tk.END)  # Törli az Entry tartalmát
    new_game()  # Új kérdés generálása

# Alkalmazás indítása
create_gui()  # GUI inicializálása és indítása
