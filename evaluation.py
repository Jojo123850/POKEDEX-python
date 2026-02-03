import tkinter as tk
from tkinter import messagebox
import os


fenetre = tk.Tk()
fenetre.title("Mon projet pokedex")

# LES IMAGES
image1 = tk.PhotoImage(file="IMG/Abo.png",)
imageabo = image1.subsample(2, 2)
image2=  tk.PhotoImage(file="IMG/Abra.png")
imageabra= image2.subsample(2, 2)
image3=  tk.PhotoImage(file="IMG/Akwakwak.png")
imageakwa = image3.subsample(2,2)
logo= tk.PhotoImage(file="IMG/Pokemon-Symbol-logo.png")
logo1= logo.subsample(20,20)

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
                label_name.config(text= f"Nom: {p.name}")
                label_type.config(text= f"Type: {p.type}")
                label_capacity.config(text= f"Capacité: {p.capacity}")
                label_attack.config(text= f"Attaque: {p.attack}")
                label_talent.config(text= f"Description: {p.talent}")
                
                label_image.config(image=p.image)
    except ValueError:
            print("Aucun pokemon n'a été trouvé")


# LOGO POKEDEX
label_titre = tk.Label(fenetre,text="POKEDEX",font=("Arial", 24, "bold"),fg= "red")
label_titre.place(x=375, y=25)
label_logo = tk.Label(fenetre, image=logo1)
label_logo.place(x=290,y=10)

# LES LABELS DE LA LISTBOX



label_name= tk.Label(fenetre, text = "Nom:")
label_name.place(x=300, y=270)

label_type= tk.Label(fenetre, text = "Type:")
label_type.place(x=300, y=290)

label_capacity= tk.Label(fenetre, text = "Capacité:")
label_capacity.place(x=300, y=310)

label_attack= tk.Label(fenetre, text = "Attaque:")
label_attack.place(x=300, y=330)

label_talent= tk.Label(fenetre, text = "Talent:")
label_talent.place(x=300, y=350)

label_image = tk.Label(fenetre)
label_image.place(x=650, y=100)

# BOUTON POUR VOIR LE POKEMON DANS LA LISTE
bouton = tk.Button(fenetre, text="Voir le pokémon", command= user)
bouton.place(x=300, y=430)

#AJOUT D'UN NOUVEAU POKEMON DANS LA LISTE
def add_pokedex(): 
        name1= champ_saisie_name.get()
        type1= champ_saisie_type.get()
        capacity1= champ_saisie_capacity.get()
        attack1= champ_saisie_attack.get()
        talent1= champ_saisie_talent.get()
        imageO = None
        image12= name1.capitalize()
        
 
        name1= champ_saisie_name.get().strip()


# LES MESSAGES D'ERREUR
    # Nom vide
        if name1 == "":
            messagebox.showerror("Erreur", "Le nom du Pokémon est vide.")
            return

    # Pour les pokémons qui existent déjà dans le Pokédex
        for p in Pokedex:
            if p.name.lower() == name1.lower():
                messagebox.showerror("Erreur",
                    "Ce Pokémon existe déjà dans le Pokédex.")
                return
    
        if not all([name1, type1, capacity1, attack1, talent1]):
            messagebox.showerror("Erreur",
                "Tous les champs doivent être remplis.")
            return

# POUR VERIFIER SI CE QU'ON VIENT D'AJOUTER 
        file_path = f"IMG/{image12}.png"
        if os.path.exists(file_path):
            image123= tk.PhotoImage(file=f"IMG/{image12}.png")
            imageO= image123.subsample(3, 3)

        nouveau_pokemon= Pokemon(name1, type1, capacity1, attack1, talent1,imageO)


# Ajouter un nouveau pokemon
        Pokedex.append(nouveau_pokemon)       
        listbox.insert(tk.END, nouveau_pokemon.name)  
        messagebox.showinfo("Succès", f"{name1} a été ajouté au Pokédex !")

        fichier= open("sauvegarde.txt", "a")
        fichier.write(f"{nouveau_pokemon.name}, {nouveau_pokemon.type}, {nouveau_pokemon.capacity}, {nouveau_pokemon.attack}, {nouveau_pokemon.talent}, {nouveau_pokemon.image}+\n")
        with open("sauvegarde.txt", "r", encoding= "utf-8") as f:
             lines= f.readlines()


        for line in lines:
            liste = line.split(", ")
            name1 = liste[0]
            type1 = liste[1]
            capacity1 = liste[2]
            attack1 = liste[3]
            talent1 = liste[4]



          
# Supprimer les pokemon
def delete():
        index = listbox.curselection()[0]
        selection = listbox.get(index)
        namedel= listbox.get(index)
        for p in Pokedex:
             if p== namedel:
                  Pokedex.remove(p)
                  break
      
        listbox.delete(index)
        
        
# Pour vider les champs après ajout
        champ_saisie_name.delete(0, tk.END)
        champ_saisie_type.delete(0, tk.END)
        champ_saisie_capacity.delete(0, tk.END)
        champ_saisie_attack.delete(0, tk.END)
        champ_saisie_talent.delete(0, tk.END)  

# Champ pour ajouter un pokemon
label_text= tk.Label(fenetre, text = "Ajouter un nouveau pokémon:")
label_text.place(x=650, y=80)


label_name1= tk.Label(fenetre, text = "Nom:")
label_name1.place(x=650, y=110)
champ_saisie_name = tk.Entry(fenetre,width=50)
champ_saisie_name.place(x=650, y=140)

label_type1= tk.Label(fenetre, text = "Type:")
label_type1.place(x=650, y=170)
champ_saisie_type = tk.Entry(fenetre, text="Type:",width=50)
champ_saisie_type.place(x=650, y=200)

label_capacity1= tk.Label(fenetre, text = "Capacité:")
label_capacity1.place(x=650, y=230)
champ_saisie_capacity = tk.Entry(fenetre, text="Capacité:", width=50)
champ_saisie_capacity.place(x=650, y=260)
 
label_talent1= tk.Label(fenetre, text = "Talent:")
label_talent1.place(x=650, y=290)
champ_saisie_talent = tk.Entry(fenetre, text="Talent:",width=50)
champ_saisie_talent.place(x=650, y=320)

label_attack1= tk.Label(fenetre, text = "Attaque:")
label_attack1.place(x=650, y=350)
champ_saisie_attack = tk.Entry(fenetre, text="Attaques",width=50)
champ_saisie_attack.place(x=650, y=380)

# Bouton de sauvegarde
bouton1 = tk.Button(fenetre, text="Sauvergarder", command= add_pokedex)
bouton1.place(x=650, y=430)

bouton2 = tk.Button(fenetre, text="Suprimer le Pokémon", command= delete,fg="black",activeforeground="red",)
bouton2.place(x=300, y=470)


fenetre.geometry("1024x768")
fenetre.mainloop()

