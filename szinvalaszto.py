import tkinter as tk
import random
import time

# Elérhető színek és azok nevei
colors = {
    'piros': 'red',
    'zöld': 'green',
    'kék': 'blue',
    'sárga': 'yellow',
    'narancs': 'orange',
    'rózsaszín': 'pink',
    'lila': 'purple',
    'fehér': 'white',
    'fekete': 'black'
}

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Színválasztó Játék")

        self.legjobb_ido = float('inf') 
        self.jelenlegi_ido = 0
        self.jatszik = False
        self.helyes_valasz = 0  # Helyes válaszok száma
        self.szavak_szama = 1  # Alapértelmezetten 1 szó
        self.szavak = []  # Tárolja a random választott szavakat
        self.szin_megjelenites = []  # Tárolja a megfelelő színeket
        self.user_input = []  # Tárolja a felhasználó válaszait

        #Különböző labelek
        self.label_szavak=tk.Label(root,font=('Arial',30),width=20,height=2)
        self.label_szavak.pack(pady=20)

        self.entry = tk.Entry(root, font=('Arial', 20))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_answer)  # Enter gombnyomáskor ellenőrzés

        self.ido_label=tk.Label(root,text="Idő: 0.00",font=('Arial',15))
        self.ido_label.pack()

        self.best_ido_label=tk.Label(root,text="Legjobb idő: N/A",font=('Arial', 15))
        self.best_ido_label.pack()

        self.feedback_label = tk.Label(root, text="Visszajelzés: ", font=('Arial', 15))
        self.feedback_label.pack()

        # Legördülő menü a színek számának beállításához
        self.dropdown_var = tk.StringVar(root)
        self.dropdown_var.set("1")  # Alapértelmezetten 1 szó
        self.dropdown = tk.OptionMenu(root, self.dropdown_var, "1", "2", "3", "4", command=self.update_szavak_szama)
        self.dropdown.pack(pady=10)

        # Kezdő gomb
        self.start_button = tk.Button(root, text="Játék indítása", font=('Arial', 15), command=self.start_game)
        self.start_button.pack(pady=20)

    def update_szavak_szama(self, value):
        # A legördülő menüben kiválasztott számot eltároljuk
        self.szavak_szama = int(value)

    def start_game(self):
        # Játék kezdése
        self.is_playing = True
        self.entry.delete(0, tk.END)  # Töröljük az eddigi bejegyzéseket
        self.jelenlegi_ido = time.time()
        self.helyes_valasz = 0  # Helyes válaszok száma reset
        self.szavak.clear()
        self.szin_megjelenites.clear()
        self.user_input.clear()

        self.ido_label.config(text="Idő: 0.00")
        self.feedback_label.config(text="Visszajelzés: ")

        # Véletlenszerű színek és szavak generálása
        self.szavak, self.szin_megjelenites = self.generate_random_words(self.szavak_szama)

        # Az első szót és színt megjelenítjük
        self.label_szavak.config(text=self.szavak[self.helyes_valasz], fg=self.szin_megjelenites[self.helyes_valasz])

        # Indítjuk a időmérőt
        self.update_time()

    def update_time(self):
        if self.is_playing:
            eltelt_ido = round(time.time() - self.jelenlegi_ido, 2)
            self.ido_label.config(text=f"Idő: {eltelt_ido}")
            self.root.after(50, self.update_time)  # Minden 50ms-ban frissítjük az időt

    def generate_random_words(self, num_words):
        # Véletlenszerű szó és szín kiválasztása
        szavak = []
        szin_megjelenites = []
        for _ in range(num_words):
            szo = random.choice(list(colors.keys()))  # Véletlenszerű szó
            szin = random.choice(list(colors.keys()))  # Véletlenszerű szín
            szavak.append(szo)
            szin_megjelenites.append(colors[szin])
        return szavak, szin_megjelenites

    def check_answer(self, event):
        # Ellenőrizzük a felhasználó válaszát
        if not self.is_playing:
            return

        user_input = self.entry.get().strip().lower()

        # Ellenőrizzük, hogy a válasz helyes-e
        expected_color_en = self.szin_megjelenites[self.helyes_valasz]  # A helyes válasz angol neve
        expected_color_hu = list(colors.keys())[list(colors.values()).index(expected_color_en)]  # Magyar megfelelő

        if user_input == expected_color_en or user_input == expected_color_hu:
            self.helyes_valasz += 1
            self.user_input.append(user_input)
            eltelt_ido = round(time.time() - self.jelenlegi_ido, 2)

            # Ha minden szóra válaszolt a felhasználó
            if self.helyes_valasz == self.szavak_szama:
                self.is_playing = False  # Játék vége
                if eltelt_ido < self.legjobb_ido:
                    self.legjobb_ido= eltelt_ido
                    self.best_ido_label.config(text=f"Legjobb idő: {self.legjobb_ido}s")
                self.feedback_label.config(text=f"Játék vége! Helyes válaszok: {self.helyes_valasz}")
                self.start_button.config(text="Új játék", command=self.start_game)
                return  # Játék befejeződött

            # Új szó következik
            self.label_szavak.config(text=self.szavak[self.helyes_valasz], fg=self.szin_megjelenites[self.helyes_valasz])
            self.feedback_label.config(text=f"Visszajelzés: Helyes válasz! ({self.helyes_valasz}/{self.szavak_szama})")
        else:
            self.feedback_label.config(text="Visszajelzés: Hibás válasz!")

        # Az idő frissítése minden válasz után
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()
