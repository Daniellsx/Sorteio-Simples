import tkinter as tk
import random
import time
from threading import Thread

class SorteioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteio de Nomes")
        
        # Lista de nomes
        self.nomes = ["Daniel", "Mateus", "Sarah", "Deborah", 'Ana']
        
        # Label para exibir o nome sorteado
        self.label_nome = tk.Label(root, text="", font=("Helvetica", 24))
        self.label_nome.pack(pady=20)
        
        # Botão para iniciar e parar o sorteio
        self.button = tk.Button(root, text="Iniciar Sorteio", command=self.toggle_sorteio, font=("Helvetica", 14))
        self.button.pack(pady=20)
        
        # Variáveis de controle
        self.sorteando = False
        self.thread = None

    def toggle_sorteio(self):
        if not self.sorteando:
            self.sorteando = True
            self.button.config(text="Parar Sorteio")
            self.thread = Thread(target=self.iniciar_sorteio)
            self.thread.start()
        else:
            self.sorteando = False
            self.button.config(text="Iniciar Sorteio")
            if self.thread:
                self.thread.join()

    def iniciar_sorteio(self):
        while self.sorteando:
            nome = random.choice(self.nomes)
            self.label_nome.config(text=nome)
            time.sleep(0.1)  # Isntervalo para dar efeito de sorteio

# Criar a interface
if __name__ == "__main__":
    root = tk.Tk()
    app = SorteioApp(root)
    root.mainloop()
