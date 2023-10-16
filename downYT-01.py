#Programa para bajar archivos de Youtube con barra de progreso
#practica de Python y Tkinter
#Octubre 2023
import tkinter as tk
from tkinter import HORIZONTAL, Label, ttk
from tkinter.ttk import Progressbar
from tkinter.messagebox import showinfo
from pytube import YouTube
import pytube.request
import time
import base64
from base64 import b64decode
import os
from tkinter import filedialog

#pytube.request.default_range_size = 9437184  # 9MB chunk size

def carpeta():
    #limpiar linea de mensaje de directorio. Los espacios en blanco son mas chicos que los caracteres
    labeldir = ttk.Label(root, text=" ".ljust(90))
    labeldir.grid(row=6, column=1, padx=15, pady=0,sticky="w")

    directorio=filedialog.askdirectory()
        
    if directorio!="":
        os.chdir(directorio)
        #texto=str(os.getcwd())
    else:
        directorio=" "
        
    texto=directorio
    
    #Si el path es muy largo se deforma la pantalla>>recortar solo pintura
    if (len(directorio))>45:
        texto=".."+directorio[-43:]
    
    labeldir = ttk.Label(root, text=texto)
    labeldir.grid(row=6, column=1, padx=15, pady=0,sticky="w")

def update_progress_label():
    #print(pb['value'])
    return f"Avance: {pb['value']}%"
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    
    pb['value'] = int(percentage_of_completion)
    value_label['text'] = update_progress_label()
    root.update() #actualiza la pantalla

def DownloadYT(url):
    try:
        youtubeObject = YouTube(url)
    # Then register the callback
        youtubeObject.register_on_progress_callback(on_progress)
        youtubeObject = youtubeObject.streams.get_highest_resolution() 
    #try:
        youtubeObject.download()
        showinfo(message='!Trabajo completado!')
        #print("Title:", youtubeObject.title)
        #print("=== Download is completed successfully ===\n")
    except:
        #print("An error has occurred") 
        showinfo(message='!An error has occurred!')

def iniciar():
    pb['value']=0
    entry.delete(0, tk.END)
    entry.insert(0, "Copie aqui la URL del video de Youtube")
 
def limpiar_button():
    iniciar()
    value_label['text'] = update_progress_label() 

root = tk.Tk()
#root.geometry("500x300")
root.geometry("450x250")
#root.config(width=1000, height=300)
root.title('DownYT V01.1')
# Cargar imagen logo

raw_image = "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"
image = tk.PhotoImage(data=b64decode(raw_image))
label = ttk.Label(image=image)
label.grid(row=5, column=2,pady=5,sticky="w")

l1 = ttk.Label(root, text="URL")
l1.grid(row=0, column=0, padx=20, pady=0)

# Crear caja de texto de entrada.
entry = ttk.Entry(root)
entry.grid(row=0, column=1,ipadx=90,pady=20)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=305
)
# place the progressbar
#pb.grid(row=2,column=1,columnspan=20, padx=0, pady=0)
pb.grid(row=2,column=1,padx=0, pady=0)

# Boton de Bajar video
button = ttk.Button(text="Bajar video",command=lambda: DownloadYT(entry.get()))
button.grid(row=3,column=1,padx=15, pady=20,sticky="w")

#iniciar variables
iniciar()
# clean button
clean_button = ttk.Button(
    root,
    text='Limpiar',
    command=limpiar_button
)
clean_button.grid(row=3,column=1,padx=15, pady=20,sticky="e")

# progressbar tomado de https://www.pythontutorial.net/tkinter/tkinter-progressbar/
# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(row=2,column=1,padx=80)


directorio = ttk.Button(
    root,
    text = 'Cambiar Directorio',
    command = carpeta
)
directorio.grid(row=5,column=1,padx=15, pady=0,sticky="w")
#ldirectorio = os.getcwd()
#labeldir = ttk.Label(root, text=os.getcwd())
#labeldir.grid(row=6, column=1, padx=15, pady=0,sticky="w")

root.mainloop()