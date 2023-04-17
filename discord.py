from tkinter import *
from math import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os



root = tkinter.Tk()
root.config(bg="black")
root.title("Discord")
root.geometry("600x500")
#print(os.getcwd())

frame_image=Frame(root, bg="black")
frame_image.pack(side=TOP, fill=X)


# # charger l'image
image_son = Image.open("image/image1 discord.png")


# # redimensionner l'image à une taille de 480x300
image_son = image_son.resize((200, 150), Image.LANCZOS)

# # créer un objet PhotoImage à partir de l'image redimensionnée
photo = ImageTk.PhotoImage(image_son)

# # créer un label et lui assigner l'image
label_image = Label(frame_image, image=photo, bg="black")
label_image.pack(side=TOP, pady=30, padx=50)


def inscription():
    # global root
    # root = tkinter.Toplevel()
 
    # root.config(bg="black")
    # root.title("Discord")
    # root.geometry("600x500")
    root.withdraw()

    # Créer une nouvelle fenêtre pour l'inscription
    top = Toplevel()
    top.config(bg="black")
    top.title("Inscription")
    top.geometry("600x500")
    
    
    zone_texte=Label(top, text="Nom", font=("Ariel", 10), bg="black", fg="white")
    zone_texte.place( x=60, y=30)
    
    entre_nom=Entry(top, width=30, font=("Ariel", 10), bg="white", fg="white")
    entre_nom.place(x=200, y=30)
    
    zone_lastname=Label(top, text="Prenom", font=("Ariel", 10), bg="black", fg="white")
    zone_lastname.place( x=60, y=100)
    
    entre_lastename=Entry(top, width=30, font=("Ariel", 10), bg="white", fg="white")
    entre_lastename.place(x=200, y=100)
    
    zone_email=Label(top, text="Email", font=("Ariel", 10), bg="black", fg="white")
    zone_email.place( x=60, y=170)
    
    entre_email=Entry(top, width=30, font=("Ariel", 10), bg="white", fg="white")
    entre_email.place(x=200, y=170)
    
    zone_password=Label(top, text="Mot de passe", font=("Ariel", 10), bg="black", fg="white")
    zone_password.place( x=60, y=240)
    
    entre_password=Entry(top, width=30, font=("Ariel", 10), bg="white", fg="white")
    entre_password.place(x=200, y=240)
    
    btn_inscription=Button(top, text="S'inscrire", font=("Ariel", 10), bg="blue", fg="white")
    btn_inscription.place(x=250, y=300)
    
    def on_close():
      top.destroy()
      root.deiconify()

    top.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
  

btn_inscription=Button(root, text="S'inscrire", font=("Ariel", 10), bg="blue", fg="white", command=inscription)
btn_inscription.pack(pady=20, padx=50)

def se_connecter():
  root.withdraw()
  fen = Toplevel()
  fen.config(bg="black")
  fen.title("Se connecter")
  fen.geometry("600x500")
  
  zone_mail=Label(fen, text="Email", font=("Ariel", 10), bg="black", fg="white")
  zone_mail.place( x=60, y=170)
  
  entre_mail=Entry(fen, width=30, font=("Ariel", 10), bg="white", fg="white")
  entre_mail.place(x=200, y=170)
  
  zone_motPasse=Label(fen, text="Mot de passe", font=("Ariel", 10), bg="black", fg="white")
  zone_motPasse.place( x=60, y=240)
  
  entre_passer=Entry(fen, width=30, font=("Ariel", 10), bg="white", fg="white")
  entre_passer.place(x=200, y=240)
  
  btn_connecter=Button(fen, text="Se connecter", font=("Ariel", 10), bg="blue", fg="white")
  btn_connecter.place(x=250, y=300)
  
  def close():
    fen.destroy()
    root.deiconify()
  
    fen.protocol("WM_DELETE_WINDOW", close)
    root.mainloop()
btn_connect=Button(root, text="Se connecter", font=("Ariel", 10), bg="blue", fg="white", command=se_connecter)
btn_connect.pack(pady=20, padx=50)

def chatInterface():
  root.withdraw()
  porte = Toplevel()
  porte.config(bg="black")
  porte.title("Chat")
  porte.geometry("600x500")
  
    
root.mainloop()


