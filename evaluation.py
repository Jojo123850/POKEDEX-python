import tkinter as tk
from tkinter import messagebox
import os

fenetre = tk.Tk()
fenetre.title("Mon projet pokedex")

# LES IMAGES
image1 = tk.PhotoImage(file="IMG/Abo.png",)
imageabo = image1.subsample(10, 10)
image2=  tk.PhotoImage(file="IMG/Abra.png")
imageabra= image2.subsample(10, 10)
image3=  tk.PhotoImage(file="IMG/Akwakwak.png")
imageakwa = image3.subsample(14,14)
logo= tk.PhotoImage(file="IMG/Pokemon-Symbol-logo.png")
logo1= logo.subsample(3,3)

listbox = tk.Listbox(fenetre, width=50)
listbox.place(x=300, y=100)

#CLASSE POKEMON
class Pokemon:
    def __init__ (self, nom, type , capacites, attaques, talent, image):
        self.name = nom
        self.type = type
        self.capacity = capacites
        self.attack= attaques
        self.talent= talent
        self.image= image
        

# LES DONNEES
Abo = Pokemon("Abo", "poison", "Sa mâchoire peut se désarticuler.","Morsure", "Mue, intidmidation", imageabo) 
Abra = Pokemon("Abra","Psy","il utilise dans son sommeil.","Charbourg","Synchro, Attention",imageabra)
Akwakwak = Pokemon("Akwakwak", "Eau", "Il nage à vitesse max grâce à ses pattes palmées", "Pistolet à 0 et Hydrocanon", "Ciel gris, Moiteur", imageakwa)

Pokedex = [Abo, Abra, Akwakwak]


# AJOUT POKEMON DANS LISTBOX
for p in Pokedex:
    listbox.insert(tk.END, p.name)

# FONCTION 
def user():
    try:
        if not listbox.curselection():
         return
        

        index = listbox.curselection()[0]
        selection = listbox.get(index)
        for p in Pokedex:

            if p.name== selection:
                label_nom.config(text= f"Nom: {p.name}")
                label_type.config(text= f"Type: {p.type}")
                label_capacites.config(text= f"Capacité: {p.capacity}")
                label_attaques.config(text= f"Attaque: {p.attack}")
                label_talent.config(text= f"Description: {p.talent}")
                
                label_image.config(image=p.image)
    except ValueError:
            print("Aucun pokemon n'a été trouvé")


# LOGO POKEDEX
label_titre = tk.Label(fenetre,text="POKEDEX",font=("Arial", 24, "bold"),fg= "red")

# LES LABELS DE LA LISTBOX
label_titre.place(x=300, y=10)
label_logo = tk.Label(fenetre, image=logo1)
label_logo.place(relx=0.45,y=10)

label_nom= tk.Label(fenetre, text = "Nom:")
label_nom.place(x=300, y=270)

label_type= tk.Label(fenetre, text = "Type:")
label_type.place(x=300, y=290)

label_capacites= tk.Label(fenetre, text = "Capacité:")
label_capacites.place(x=300, y=310)

label_attaques= tk.Label(fenetre, text = "Attaque:")
label_attaques.place(x=300, y=330)

label_talent= tk.Label(fenetre, text = "Talent:")
label_talent.place(x=300, y=350)

label_image = tk.Label(fenetre)
label_image.place(x=300, y=380)

# BOUTON POUR VOIR LE POKEMON DANS LA LISTE
bouton = tk.Button(fenetre, text="Voir le pokémon", command= user)
bouton.place(x=300, y=500)

#AJOUT D'UN NOUVEAU POKEMON DANS LA LISTE
def ajouter_pokedex(): 
        nom1= champ_saisie_nom.get()
        type1= champ_saisie_type.get()
        capacites1= champ_saisie_capacites.get()
        attaques1= champ_saisie_attaques.get()
        talent1= champ_saisie_talent.get()
        imageO = 0
        image12= nom1.capitalize()
        
 
        nom1 = champ_saisie_nom.get().strip()


# LES MESSAGES D'ERREUR
    # Nom vide
        if nom1 == "":
            messagebox.showerror("Erreur", "Le nom du Pokémon est vide.")
            return

    # Pour les pokémons qui existent déjà dans le Pokédex
        for p in Pokedex:
            if p.name.lower() == nom1.lower():
                messagebox.showerror("Erreur",
                    "Ce Pokémon existe déjà dans le Pokédex.")
                return
    
        if not all([nom1, type1, capacites1, attaques1, talent1]):
            messagebox.showerror("Erreur",
                "Tous les champs doivent être remplis.")
            return

# POUR VERIFIER SI CE QU'ON VIENT D'AJOUTER 
        file_path = f"IMG/{image12}.png"
        if os.path.exists(file_path):
            image123= tk.PhotoImage(file=f"IMG/{image12}.png")
            imageO= image123.subsample(10, 10)

        nouveau_pokemon= Pokemon(nom1, type1, capacites1, attaques1, talent1,imageO)


# Ajouter un nouveau pokemon
        Pokedex.append(nouveau_pokemon)       
        listbox.insert(tk.END, nouveau_pokemon.name)  
        messagebox.showinfo("Succès", f"{nom1} a été ajouté au Pokédex !")


# Pour vider les champs après ajout
        champ_saisie_nom.delete(0, tk.END)
        champ_saisie_type.delete(0, tk.END)
        champ_saisie_capacites.delete(0, tk.END)
        champ_saisie_attaques.delete(0, tk.END)
        champ_saisie_talent.delete(0, tk.END)  

# Champ pour ajouter un pokemon
label_text= tk.Label(fenetre, text = "Ajouter un nouveau pokémon:")
label_text.place(x=650, y=80)


label_nom1= tk.Label(fenetre, text = "Nom:")
label_nom1.place(x=650, y=110)
champ_saisie_nom = tk.Entry(fenetre,width=50)
champ_saisie_nom.place(x=650, y=140)

label_type1= tk.Label(fenetre, text = "Type:")
label_type1.place(x=650, y=170)
champ_saisie_type = tk.Entry(fenetre, text="Type:",width=50)
champ_saisie_type.place(x=650, y=200)

label_capacites1= tk.Label(fenetre, text = "Capacité:")
label_capacites1.place(x=650, y=230)
champ_saisie_capacites = tk.Entry(fenetre, text="Capacité:", width=50)
champ_saisie_capacites.place(x=650, y=260)
 
label_talent1= tk.Label(fenetre, text = "Talent:")
label_talent1.place(x=650, y=290)
champ_saisie_talent = tk.Entry(fenetre, text="Talent:",width=50)
champ_saisie_talent.place(x=650, y=320)

label_attaques1= tk.Label(fenetre, text = "Attaque:")
label_attaques1.place(x=650, y=350)
champ_saisie_attaques = tk.Entry(fenetre, text="Attaques",width=50)
champ_saisie_attaques.place(x=650, y=380)

# Bouton de sauvegarde
bouton1 = tk.Button(fenetre, text="Sauvergarder", command= ajouter_pokedex
)
bouton1.place(x=650, y=500)


fenetre.geometry("1024x768")
fenetre.mainloop()

