import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Mon projet pokedex")

# Les images
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

# Classe Pokemon
class Pokemon:
    def __init__ (self, nom, type , capacites, attaques, talent, image):
        self.name = nom
        self.type = type
        self.capacity = capacites
        self.attack= attaques
        self.talent= talent
        self.image= image
        

# Données
Abo = Pokemon("Abo", "poison", "Sa mâchoire peut se désarticuler.","Morsure", "Mue, intidmidation", imageabo) 
Abra = Pokemon("Abra","Psy","il utilise dans son sommeil.","Charbourg","Synchro, Attention",imageabra)
Akwakwak = Pokemon("Akwakwak", "Eau", "Il nage à vitesse max grâce à ses pattes palmées", "Pistolet à 0 et Hydrocanon", "Ciel gris, Moiteur", imageakwa)

Pokedex = [Abo, Abra, Akwakwak]


# Ajout Pokemon dans listbox
for p in Pokedex:
    listbox.insert(tk.END, p.name)

# Fonction 
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
label_titre = tk.Label(
    fenetre,
    text="POKEDEX",
    font=("Arial", 24, "bold"),
    fg= "red"
)
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

bouton = tk.Button(fenetre, text="Voir le pokémon", command= user)
bouton.place(x=300, y=500)

# Ajou d'un nouveau Pokemon dans la liste
def ajouter_pokedex():   
       
        nom1= champ_saisie_nom.get()
        type1= champ_saisie_type.get()
        capacites1= champ_saisie_capacites.get()
        attaques1= champ_saisie_attaques.get()
        talent1= champ_saisie_talent.get()
        imageO = 0
        image12= nom1.capitalize()

        image123= tk.PhotoImage(file=f"IMG/{image12}.png")
        imageO= image123.subsample(10, 10)

        nouveau_pokemon= Pokemon(nom1, type1, capacites1, attaques1, talent1,imageO)
        
        Pokedex.append(nouveau_pokemon)       
        listbox.insert(tk.END, nouveau_pokemon.name)  

        # Vider les champs après ajout
        champ_saisie_nom.delete(0, tk.END)
        champ_saisie_type.delete(0, tk.END)
        champ_saisie_capacites.delete(0, tk.END)
        champ_saisie_attaques.delete(0, tk.END)
        champ_saisie_talent.delete(0, tk.END)  

# Champ pour ajouter un pokemon
label_text= tk.Label(fenetre, text = "Ajouter un nouveau pokémon:")
label_text.place(x=650, y=80)


label_nom1= tk.Label(fenetre, text = "Nom:")
label_nom1.place(x=650, y=100)
champ_saisie_nom = tk.Entry(fenetre,width=50)
champ_saisie_nom.place(x=650, y=130)

label_type1= tk.Label(fenetre, text = "Type:")
label_type1.place(x=650, y=160)
champ_saisie_type = tk.Entry(fenetre, text="Type:",width=50)
champ_saisie_type.place(x=650, y=190)

label_capacites1= tk.Label(fenetre, text = "Capacité:")
label_capacites1.place(x=650, y=210)
champ_saisie_capacites = tk.Entry(fenetre, text="Capacité:", width=50)
champ_saisie_capacites.place(x=650, y=240)
 
label_talent1= tk.Label(fenetre, text = "Talent:")
label_talent1.place(x=650, y=270)
champ_saisie_talent = tk.Entry(fenetre, text="Talent:",width=50)
champ_saisie_talent.place(x=650, y=300)

label_attaques1= tk.Label(fenetre, text = "Attaque:")
label_attaques1.place(x=650, y=330)
champ_saisie_attaques = tk.Entry(fenetre, text="Attaques",width=50)
champ_saisie_attaques.place(x=650, y=360)

# Bouton de sauvegarde
bouton1 = tk.Button(fenetre, text="Sauvergarder", command= ajouter_pokedex)
bouton1.place(x=650, y=500)





fenetre.geometry("1024x768")
fenetre.mainloop()

