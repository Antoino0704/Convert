import tkinter as tk
import tkinter.filedialog
from PIL import Image





class Immaggine:
    def __init__(self, win):
        #creazione menu
        menu = tk.Menu(win)
        sottomenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='options', menu=sottomenu)
        sottomenu.add_command(label='Apri', command=self.Apri)
        sottomenu.add_command(label='Converti', command=self.Converti)
        win.configure(menu=menu, bg='black')

        #creazione label di informazione dello stato
        self.stato = tk.StringVar()
        self.stato.set('Nessun file aperto')
        confirm = tk.Label(win, textvariable=self.stato, fg='red', font=("", 35))
        confirm.grid(row=0,column=0,sticky="NW")
        confirm.grid_propagate(0)

        #apri il file
    def Apri(self):
        a = tkinter.filedialog.askopenfilename(defaultextension='.png', filetypes=[('file png', '*.png'), ('file jpg', '*.jpg'), ('file bitmap', '*.bmp'), ('tutti i file', '*.*')])
        self.img = Image.open(a)
        self.stato.set('File aperto')
        
    #converti il file
    def Converti(self):
        im = self.img.convert('L')
        save = tkinter.filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('file png', '*.png'), ('file jpg', '*.jpg'), ('file bitmap', '*.bmp'), ('tutti i file', '*.*')])
        im.save(save)
        self.stato.set('File convertito con successo')



#parte principale
win = tk.Tk()
win.geometry('600x600')
win.grid_columnconfigure(0, weight=1)
win.iconbitmap("Icon.ico")
c = Immaggine(win)
win.mainloop()
