import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Mon projet pokedex")

class Pokemon:
    def __init__ (self, nom, type , capacites, attaques, description):
        self.nom = nom
        self.type = type
        self.capacites = capacites
        self.attaques= attaques
        self.description= description

fenetre.geometry("1024x768")
fenetre.mainloop()

