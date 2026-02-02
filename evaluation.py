import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Mon projet pokedex")

image1 = tk.PhotoImage(file="IMG/Abo.png",)
imageabo = image1.subsample(3, 3)
image2=  tk.PhotoImage(file="IMG/Abra.png")
imageabra= image2.subsample(2, 2)
image3=  tk.PhotoImage(file="IMG/Akwakwak.png")
imageakwa = image3.subsample(3, 3)

listbox = tk.Listbox(fenetre)
listbox.pack()

class Pokemon:
    def __init__ (self, nom, type , capacites, attaques, talent, image):
        self.nom = nom
        self.type = type
        self.capacites = capacites
        self.attaques= attaques
        self.talent= talent
        self.image= image
        

# Données
Abo = Pokemon("Abo", "poison", "Sa mâchoire peut se désarticuler. Il est ainsi en mesure d’avaler de larges proies, mais ce faisant, il devient trop lourd pour bouger.", "Morsure", "Mue, intidmidation", imageabo) 
Abra = Pokemon("Abra","Psy","Le contenu de ses rêves influe sur les pouvoirs psychiques qu’il utilise dans son sommeil.","Charbourg","Synchro, Attention",imageabra)
Akwakwak = Pokemon("Akwakwak", "Eau", "Quand il nage à vitesse maximale grâce à ses pattes palmées, son front se met à luire pour une raison inconnue.", "Pistolet à 0 et Hydrocanon", "Ciel gris, Moiteur", imageakwa)

Pokedex = [Abo, Abra, Akwakwak]



for p in Pokedex:
    listbox.insert(tk.END, p.nom)


def user():
    try:
        if not listbox.curselection():
         return
        

        index = listbox.curselection()[0]
        selection = listbox.get(index)
        for p in Pokedex:

            if p.nom== selection:
                label_nom.config(text= f"Nom: {p.nom}")
                label_type.config(text= f"Type: {p.type}")
                label_capacites.config(text= f"Capacité: {p.capacites}")
                label_attaques.config(text= f"Attaque: {p.attaques}")
                label_description.config(text= f"Description: {p.talent}")
                
                label_image.config(image=p.image)
    except ValueError:
            print("Aucun pokemon n'a été trouvé")


label_nom= tk.Label(fenetre, text = "Nom:")
label_nom.pack()

label_type= tk.Label(fenetre, text = "Type:")
label_type.pack()

label_capacites= tk.Label(fenetre, text = "Capacité:")
label_capacites.pack()

label_attaques= tk.Label(fenetre, text = "Attaque:")
label_attaques.pack()

label_description= tk.Label(fenetre, text = "Description:")
label_description.pack()

label_image = tk.Label(fenetre)
label_image.pack(pady=10)


bouton = tk.Button(fenetre, text="Voir le pokémon", command= user)
bouton.pack()


fenetre.geometry("1024x768")
fenetre.mainloop()

