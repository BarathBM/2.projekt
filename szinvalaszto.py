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

        self.best_time = float('inf')  # A legjobb idő alapértelmezetten végtelen
        self.current_time = 0
        self.is_playing = False
        self.correct_answers = 0  # Helyes válaszok száma
        self.num_words = 1  # Alapértelmezetten 1 szó
        self.words = []  # Tárolja a véletlenszerűen választott szavakat
        self.colors_display = []  # Tárolja a megfelelő színeket
        self.user_input = []  # Tárolja a felhasználó válaszait

        # Különböző label-ek
        self.label_words = tk.Label(root, font=('Arial', 30), width=20, height=2)
        self.label_words.pack(pady=20)

        self.entry = tk.Entry(root, font=('Arial', 20))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_answer)  # Enter gombnyomáskor ellenőrzés

        self.time_label = tk.Label(root, text="Idő: 0.00", font=('Arial', 15))
        self.time_label.pack()

        self.best_time_label = tk.Label(root, text="Legjobb idő: N/A", font=('Arial', 15))
        self.best_time_label.pack()

        self.feedback_label = tk.Label(root, text="Visszajelzés: ", font=('Arial', 15))
        self.feedback_label.pack()

        # Legördülő menü a színek számának beállításához
        self.dropdown_var = tk.StringVar(root)
        self.dropdown_var.set("1")  # Alapértelmezetten 1 szó
        self.dropdown = tk.OptionMenu(root, self.dropdown_var, "1", "2", "3", "4", command=self.update_num_words)
        self.dropdown.pack(pady=10)

        # Kezdő gomb
        self.start_button = tk.Button(root, text="Játék indítása", font=('Arial', 15), command=self.start_game)
        self.start_button.pack(pady=20)

    def update_num_words(self, value):
        # A legördülő menüben kiválasztott számot eltároljuk
        self.num_words = int(value)

    def start_game(self):
        # Játék kezdése
        self.is_playing = True
        self.entry.delete(0, tk.END)  # Töröljük az eddigi bejegyzéseket
        self.current_time = time.time()
        self.correct_answers = 0  # Helyes válaszok száma reset
        self.words.clear()
        self.colors_display.clear()
        self.user_input.clear()

        self.time_label.config(text="Idő: 0.00")
        self.feedback_label.config(text="Visszajelzés: ")

        # Véletlenszerű színek és szavak generálása
        self.words, self.colors_display = self.generate_random_words(self.num_words)

        # Az első szót és színt megjelenítjük
        self.label_words.config(text=self.words[self.correct_answers], fg=self.colors_display[self.correct_answers])

        # Indítjuk a időmérőt
        self.update_time()

    def update_time(self):
        if self.is_playing:
            elapsed_time = round(time.time() - self.current_time, 2)
            self.time_label.config(text=f"Idő: {elapsed_time}")
            self.root.after(50, self.update_time)  # Minden 50ms-ban frissítjük az időt

    def generate_random_words(self, num_words):
        # Véletlenszerű szó és szín kiválasztása
        words = []
        colors_display = []
        for _ in range(num_words):
            word = random.choice(list(colors.keys()))  # Véletlenszerű szó
            color = random.choice(list(colors.keys()))  # Véletlenszerű szín
            words.append(word)
            colors_display.append(colors[color])
        return words, colors_display

    def check_answer(self, event):
        # Ellenőrizzük a felhasználó válaszát
        if not self.is_playing:
            return

        user_input = self.entry.get().strip().lower()

        # Ellenőrizzük, hogy a válasz helyes-e
        expected_color_en = self.colors_display[self.correct_answers]  # A helyes válasz angol neve
        expected_color_hu = list(colors.keys())[list(colors.values()).index(expected_color_en)]  # Magyar megfelelő

        if user_input == expected_color_en or user_input == expected_color_hu:
            self.correct_answers += 1
            self.user_input.append(user_input)
            elapsed_time = round(time.time() - self.current_time, 2)

            # Ha minden szóra válaszolt a felhasználó
            if self.correct_answers == self.num_words:
                self.is_playing = False  # Játék vége
                if elapsed_time < self.best_time:
                    self.best_time = elapsed_time
                    self.best_time_label.config(text=f"Legjobb idő: {self.best_time}s")
                self.feedback_label.config(text=f"Játék vége! Helyes válaszok: {self.correct_answers}")
                self.start_button.config(text="Új játék", command=self.start_game)
                return  # Játék befejeződött

            # Új szó következik
            self.label_words.config(text=self.words[self.correct_answers], fg=self.colors_display[self.correct_answers])
            self.feedback_label.config(text=f"Visszajelzés: Helyes válasz! ({self.correct_answers}/{self.num_words})")
        else:
            self.feedback_label.config(text="Visszajelzés: Hibás válasz!")

        # Az idő frissítése minden válasz után
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()
