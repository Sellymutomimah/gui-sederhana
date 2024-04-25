import tkinter as tk

window = tk.Tk()
window.title("Hello - Selly")
salam = tk.Label(text="Apa Kabar", fg="black", bg="pink") 
logo = tk.PhotoImage(file="songkang.gif") 
WLableImage = tk.Label(image=logo)
salam.pack()
WLableImage.pack()

window.mainloop()