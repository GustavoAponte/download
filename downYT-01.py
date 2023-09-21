#Programa para bajar archivos de Youtube con barra de progreso
#practica de Python y Tkinter
#Septiembre 2023
import tkinter as tk
from tkinter import HORIZONTAL, Label, ttk
from tkinter.ttk import Progressbar
from tkinter.messagebox import showinfo

from pytube import YouTube
import time

def update_progress_label():
    print(pb['value'])
    return f"Progreso actual: {pb['value']}%"
    

#def progress():
#    if pb['value'] < 100:
#        pb['value'] += 20
#        value_label['text'] = update_progress_label()
#    else:
#        showinfo(message='The progress completed!')


#def stop():
#    pb.stop()
#    value_label['text'] = update_progress_label()


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    
    pb['value'] = int(percentage_of_completion)
    value_label['text'] = update_progress_label()
    root.update_idletasks() #actualiza la pantalla
 
def DownloadYT(url):
    youtubeObject = YouTube(url)
    # Then register the callback
    youtubeObject.register_on_progress_callback(on_progress)
    youtubeObject = new_func(youtubeObject)
    try:
      youtubeObject.download()
      print("Title:", youtubeObject.title)
      print("=== Download is completed successfully ===\n")
    except:
        print("An error has occurred") 

def new_func(youtubeObject):
    return youtubeObject.streams.get_highest_resolution()

def limpiar_button():
    #entry = ttk.Entry(width=60)
# Posicionarla en la ventana.
    #entry.place(x=100, y=50)
    entry.insert(0, "Copie aqui la URL del video de Youtube")
 
root = tk.Tk()
root.geometry("500x300")
#root.config(width=1000, height=300)
root.title('DownYT B01.0')
# Crear caja de texto de entrada.
entry = ttk.Entry(width=60)
# Posicionarla en la ventana.
entry.place(x=100, y=50)


# clean button
clean_button = ttk.Button(
    root,
    text='Limpiar',
    command=limpiar_button()
)
clean_button.grid(column=1, row=150, padx=10, pady=2, sticky=tk.E)


#entry.insert(0, "Copie aqui la URL del video de Youtube")

button = ttk.Button(text="Bajar video", command=lambda: DownloadYT(entry.get()))
button.place(x=10, y=50)

# progressbar tomado de https://www.pythontutorial.net/tkinter/tkinter-progressbar/
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=480
)
# place the progressbar
pb.grid(column=5, row=150, columnspan=2, padx=1, pady=100)

# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=151, columnspan=52)


#stop_button = ttk.Button(
#    root,
#    text='Stop',
#    command=stop
#)
#stop_button.grid(column=0, row=150, padx=10, pady=10, sticky=tk.W)

root.mainloop()