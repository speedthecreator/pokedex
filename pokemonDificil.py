import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

janela = tk.Tk()
janela.geometry("600x500")
janela.title("Pokedex")
janela.config(padx=10, pady=10)

title_label = tk.Label(janela, text="NeuralNine Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(janela)
pokemon_image.config(font=("Arial", 40))
pokemon_image.pack()

pokemon_information = tk.Label(janela)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_type = tk.Label(janela)
pokemon_type.config(font=("Arial", 20))
pokemon_type.pack(padx=10, pady=10)

# Funções
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_type.config(text=" - ".join([t for t in pokemon.types]).title())

label_id_name = tk.Label(janela, text="ID ou Nome")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(janela, heigh=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(janela, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

janela.mainloop()