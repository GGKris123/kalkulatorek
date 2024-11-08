import tkinter as tk

class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")

        self.wynik = tk.Entry(root)
        self.wynik.grid(row=0, column=0, columnspan=4)

        self.przyciski = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        self.row = 1
        self.col = 0

        for przycisk in self.przyciski:
            tk.Button(root, text=przycisk, command=lambda p=przycisk: self.naciśnij_przycisk(p)).grid(row=self.row, column=self.col)
            self.col += 1
            if self.col > 3:
                self.col = 0
                self.row += 1

        tk.Button(root, text='C', command=self.czysc).grid(row=self.row, column=0)

    def naciśnij_przycisk(self, przycisk):
        if przycisk == '=':
            try:
                wynik = str(eval(self.wynik.get()))
                self.wynik.delete(0, tk.END)
                self.wynik.insert(0, wynik)
            except:
                self.wynik.delete(0, tk.END)
                self.wynik.insert(0, 'Błąd')
        else:
            self.wynik.insert(tk.END, przycisk)

    def czysc(self):
        self.wynik.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    kalkulator = Kalkulator(root)
    root.mainloop()
