import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

last_opened_file = None  # Globální proměnná pro uchování cesty k poslednímu otevřenému souboru

def uloz_text():
    global last_opened_file
    text = text_widget.get("1.0", "end-1c")  # Získání textu z textového pole
    if last_opened_file:
        with open(last_opened_file, "w") as soubor:
            soubor.write(text)
        tk.messagebox.showinfo("Info", "Soubor byl úspěšně uložen!")
    else:
        uloz_jako()

def uloz_jako():
    global last_opened_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as soubor:
            text = text_widget.get("1.0", "end-1c")
            soubor.write(text)
        last_opened_file = file_path

def nacti_text():
    global last_opened_file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as soubor:
            text = soubor.read()
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", text)
        last_opened_file = file_path

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Textový editor")

# Vytvoření textového pole
text_widget = tk.Text(root)
text_widget.pack()

# Tlačítka pro uložení, uložení jako a načtení textu
uloz_tlacitko = tk.Button(root, text="Uložit text", command=uloz_text)
uloz_tlacitko.pack()

uloz_jako_tlacitko = tk.Button(root, text="Uložit jako", command=uloz_jako)
uloz_jako_tlacitko.pack()

nacti_tlacitko = tk.Button(root, text="Načíst text", command=nacti_text)
nacti_tlacitko.pack()

# Spuštění hlavní smyčky aplikace
root.mainloop()