import tkinter as tk

window = tk.Tk()
window.title("Hello - Selly")
salam = tk.Label(text="Apa Kabar", fg="black", bg="pink") 
WButton = tk.Button( 
    text = "Klik Saya!", 
    width = 20, 
    height = 10, 
    bg = "magenta", 
    fg = "white" 
) 
salam.pack()
WButton.pack()

window.mainloop()