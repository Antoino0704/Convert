import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageTk





class Immaggine:
    def __init__(self, win):
        #creazione menu
        menu = tk.Menu(win)
        sottomenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='options', menu=sottomenu)
        sottomenu.add_command(label='Apri', command=self.Apri)
        sottomenu.add_command(label='Converti', command=self.Converti)
        sottomenu.add_command(label='Info', command=self.Information)
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
        img2 = Image.open(a)
        imgRez = img2.resize((200, 200), Image.ANTIALIAS)
        self.imageTk = ImageTk.PhotoImage(imgRez)
        self.l1 = tk.Label(win, image=self.imageTk)
        self.l1.grid(row=10,column=0, pady=100)
        self.stato.set('File aperto')
        
    #converti il file
    def Converti(self):
        im = self.img.convert('L')
        save = tkinter.filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('file png', '*.png'), ('file jpg', '*.jpg'), ('file bitmap', '*.bmp'), ('tutti i file', '*.*')])
        im.save(save)
        self.stato.set('File convertito con successo')

    #information for program
    def Information(self):
        tkinter.messagebox.showinfo('Info Convert', 'version: 1.2.1\nAuthor: Antonino Buscarino')


#parte principale
win = tk.Tk()
win.title('Convert')
win.geometry('600x600')
win.grid_columnconfigure(0, weight=1)
win.iconbitmap("Icon.ico")
c = Immaggine(win)
win.mainloop()
