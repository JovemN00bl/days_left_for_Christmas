import datetime
import os.path
import tkinter as tk
from tkinter import simpledialog
def days_left():
    today = datetime.date.today()
    christmas = datetime.date(today.year, 12 , 25)


    if today > christmas:
        christmas = datetime.date(today.year + 1, 12, 25)

    diff = christmas - today

    print(f"Only {diff.days} days left until christmas!")
    return diff.days

file_config = "christmas_days.txt"

def loading_text():
    if os.path.exists(file_config):
        with open(file_config, "r", encoding="utf-8") as f:
            return f.read()
    return "days for christmas "

def save_New_Text():
    new_text = simpledialog.askstring("Change phrase", "What do you want to write?")


    with open(file_config, "w", enconding="utf-8") as f:
         f.write(new_text)


class AppMinimalista:
    def __init__(self, root):
        self.root = root

        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)


        self.root.config(bg="black")
        self.root.attributes("-transparentcolor", "black")

        self.dias = days_left()
        self.frase = loading_text()

        texto_completo = f"{self.dias} {self.frase}"
        if self.dias == 0:
            texto_completo = "Feliz Natal!"

        self.label = tk.Label(
            root,
            text=texto_completo,
            font=("Segoe UI", 40, "bold"),
            fg="white",
            bg="black"
        )
        self.label.pack()

        self.centralizar_janela()


        self.menu = tk.Menu(root, tearoff=0)
        self.menu.add_command(label="Mudar Frase", command=self.mudar_frase)
        self.menu.add_separator()
        self.menu.add_command(label="Fechar", command=root.destroy)

        root.bind("<Button-3>", self.mostrar_menu)

        self.root.bind("<Button-1>", self.iniciar_arraste)
        self.root.bind("<B1-Motion>", self.arrastar)

    def centralizar_janela(self):
        self.root.update_idletasks()
        largura = self.root.winfo_width()
        altura = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f'+{x}+{y}')

    def mostrar_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

    def mudar_frase(self):
        nova = simpledialog.askstring("Configurar", "Digite a nova frase (ex: dias para a ceia):")
        if nova:
            self.frase = nova
            save_New_Text(nova)
            self.label.config(text=f"{self.dias} {self.frase}")

    def iniciar_arraste(self, event):
        self.x = event.x
        self.y = event.y

    def arrastar(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppMinimalista(root)
    root.mainloop()