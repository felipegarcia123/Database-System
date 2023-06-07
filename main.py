import tkinter as tk
from tkinter import  ttk
import sys


class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('780x480')
        self.config(bg="white")
        self.title('BD')

        # Initialize style
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('TFrame', background='green')
        s.configure('Frame1.TFrame', background='blue')
        s.configure('Frame2.TFrame',background = 'black')

        #left frame
        self.frame1 = ttk.Frame(self, style='Frame1.TFrame' )
        self.frame1.place(x=0, y=0, width=540, relheight=1)

        #right frame
        self.frame2 = ttk.Frame(self,style='Frame2.TFrame')
        self.frame2.place(x=540, y=0, relwidth=1, relheight=1)

        #buttons
        self.b_add = ttk.Button(self.frame2,text='Add Client',cursor='hand2', command=self.addClient).place(x=68,y=60,width=100)
        self.b_show_clients = ttk.Button(self.frame2, text='Show Clients', cursor='hand2',command=self.showClients).place(x=68, y=120, width=100)
        self.b_update_clients = ttk.Button(self.frame2, text='Update Client', cursor='hand2',command=self.updateClient).place(x=68, y=180, width=100)
        self.b_delete_client= ttk.Button(self.frame2, text='Delete Client', cursor='hand2',command=self.deleteClient).place(x=68, y=240, width=100)
        self.b_clearbd = ttk.Button(self.frame2, text='Clear DB', cursor='hand2',command=self.ClearScreen).place(x=68, y=300, width=100)
        self.b_exit = ttk.Button(self.frame2, text='Exit', cursor='hand2',command=exit).place(x=68, y=360, width=100)

        #Components to add data

        #Add componeents to view addClient

    def addClient(self):
        self.ClearScreen()
        self.name = ttk.Label(self.frame1,text='Name',).place(x=40,y = 30)
        self.entry_name = ttk.Entry(self.frame1).place(x=40,y=60,width=130)

        self.last_name = ttk.Label(self.frame1, text='Last name', ).place(x=300, y=30)
        self.entry_last_name = ttk.Entry(self.frame1).place(x=300, y=60, width=130)

        self.age = ttk.Label(self.frame1,text='Age').place(x=40, y= 100)
        self.entry_age = ttk.Entry(self.frame1).place(x = 40, y = 130)

        self.email = ttk.Label(self.frame1, text='Email').place(x=300, y=100)
        self.entry_email = ttk.Entry(self.frame1).place(x=300, y=130)

        self.birth = ttk.Label(self.frame1, text='Bithday').place(x=40, y=170)
        self.entry_birth = ttk.Entry(self.frame1).place(x=40, y=200)

        self.gender = ttk.Label(self.frame1, text='Gender').place(x=300, y=170)
        self.entry_gender = ttk.Entry(self.frame1).place(x=300, y=200)

        self.image = tk.PhotoImage(file='bt.png')
        self.b_send = ttk.Button(self.frame1,image=self.image,cursor="hand2").place(x=200,y=320)

    #Show the info of the client from your phone number

    def showClients(self):
        self.ClearScreen()
        self.get_info = ttk.Label(self.frame1,text='Type the client\'s number to watch the onformation').place(x=120,y=70)
        self.enty_get_info = ttk.Entry(self.frame1).place(x=163, y=110, width=200, height=30)
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1,image=self.image,cursor="hand2").place(x=200,y=320)

    def updateClient(self):
        self.ClearScreen()

        self.getInfo = ttk.Label(self.frame1, text="Enter Phone Number's client to update").place(x=160, y=70)
        self.getInfo_entry = ttk.Entry(self.frame1).place(x=163, y=110, width=200, height=30)
        self.getInfo_entry
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1, image=self.image, cursor="hand2").place(x=220, y=150)

    def deleteClient(self):
        self.ClearScreen()

        self.getInfo = ttk.Label(self.frame1, text="Enter Phone Number's client to DELETE").place(x=160, y=70)
        self.getInfo_entry = ttk.Entry(self.frame1).place(x=163, y=110, width=200, height=30)
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1, image=self.image, cursor="hand2").place(x=220, y=150)

    def exit(self):
        self.destroy()
        sys.exit()









    '''Remove all widgets from the frame 1'''

    def ClearScreen(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()







if __name__ == '__main__':
    v = ventana()
    v.mainloop()



