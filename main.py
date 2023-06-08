import tkinter as tk
from tkinter import  ttk, messagebox
import  psycopg2 as pg
from  logger_base import log
import sys


class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('780x480')
        self.config(bg="white")
        self.title('BD')

        #Credentials Database
        self._con = None
        self._cur = None
        self._DATABASE = 'clients_2023'
        self._USERNAME = 'postgres'
        self._PASSWORD = 'ADMIN'
        self._DB_PORT = '5432'
        self._HOST = 'localhost'

        #SQL statements
        self._SELECT = 'SELECT * FROM clients WHERE identification =%s '
        self._ACTUALIZAR = 'UPDATE person SET nombre =%s, apellido =%s, email =%s,edad = %s  WHERE id_persona =%s '
        self._ELIMINAR = 'DELETE FROM person WHERE id_persona = %s'


        # Initialize style
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('TFrame', background='green')
        s.configure('Frame1.TFrame', background='white')
        s.configure('Frame2.TFrame',background = 'black')

        #left frame
        self.frame1 = ttk.Frame(self, style='Frame1.TFrame' )
        self.frame1.place(x=0, y=0, width=540, relheight=1)

        #right frame
        self.frame2 = ttk.Frame(self,style='Frame2.TFrame')
        self.frame2.place(x=540, y=0, relwidth=1, relheight=1)

        #buttons
        self.b_add = ttk.Button(self.frame2,text='Add Client',cursor='hand2', command=self.addClient).place(x=68,y=60,width=100)
        self.b_show_clients = ttk.Button(self.frame2, text='Show Clients', cursor='hand2',command=self.showClient).place(x=68, y=120, width=100)
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

        self.identification = ttk.Label(self.frame1, text='Identification').place(x=40, y=240)
        self.entry_identificaction = ttk.Entry(self.frame1).place(x=40, y=270)

        self.image = tk.PhotoImage(file='bt.png')
        self.b_send = ttk.Button(self.frame1,image=self.image,cursor="hand2").place(x=200,y=320)

    #Show the info of the client from your phone number

    def showClient(self):
        self.ClearScreen()
        self.get_info = ttk.Label(self.frame1,text='Type the client\'s id to watch the onformation').place(x=120,y=70)
        self.enty_get_info = ttk.Entry(self.frame1)
        self.enty_get_info.place(x=163, y=110, width=200, height=30)
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1,image=self.image,cursor="hand2",command=self.checkContactView).place(x=200,y=320)


    def updateClient(self):
        self.ClearScreen()

        self.getInfo = ttk.Label(self.frame1, text="Enter client's ID to update").place(x=160, y=70)
        self.getInfo_entry = ttk.Entry(self.frame1).place(x=163, y=110, width=200, height=30)
        self.getInfo_entry
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1, image=self.image, cursor="hand2").place(x=220, y=150)

    def deleteClient(self):
        self.ClearScreen()

        self.getInfo = ttk.Label(self.frame1, text="Enter client's ID to DELETE").place(x=160, y=70)
        self.getInfo_entry = ttk.Entry(self.frame1).place(x=163, y=110, width=200, height=30)
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1, image=self.image, cursor="hand2").place(x=220, y=150)

    def exit(self):
        self.destroy()
        sys.exit()

    #Add the functions of the buttoms
    def getConextion(self):
        if self._con is None:
            try:
                self._con = pg.connect(host=self._HOST, user=self._USERNAME, password=self._PASSWORD, database=self._DATABASE,
                                 port=self._DB_PORT)
                log.info('Succesfull conexion')
                return  self._con
            except Exception as E:
                log.error('Has ocurred an excepction during the conextion')
        else:
            return self._con

    def getCursor(self):
        if self._cur is None:
            try:
                self._cur = self.getConextion().cursor()
                log.info('The cursor was executed correctly')
                return  self._cur
            except Exception as e:
                log.error('Has ocurred an excepction during the creation the cursor')
        else:
            return self._cur


    def checkContactView(self):
        if self.enty_get_info.get() == "":
            messagebox.showerror('Error !', 'Please put your phone number')
        else:
            try:
                with self.getConextion() as conn:
                    with conn.cursor() as cur:
                        cur.execute(self._SELECT,(self.enty_get_info.get(),))
                        row = cur.fetchone()
                        if row == None:
                            messagebox.showerror("Error!", "Contact number doesn't exists", parent=self)

                        else:
                            self.getDetailsClient(row)
            except Exception as e:
                messagebox.showerror('Error!', f'Error: {str(e)}',parent=self)














    '''Remove all widgets from the frame 1'''

    def ClearScreen(self,):
        for widget in self.frame1.winfo_children():
            widget.destroy()
    def getDetailsClient(self,row):
        self.ClearScreen()
        name = ttk.Label(self.frame1, text='First Name').place(x=40,y=30)
        name_data = ttk.Label(self.frame1,text=row[1]).place(x=40, y=60)

        last_name = ttk.Label(self.frame1, text='Last Name').place(x=300,y=30)
        last_name_data = ttk.Label(self.frame1,text=row[2]).place(x=300, y=60)

        age = ttk.Label(self.frame1, text='Age').place(x=40, y=100)
        age_data = ttk.Label(self.frame1, text=row[3]).place(x=40, y=130)

        email = ttk.Label(self.frame1, text='Email').place(x=300, y=100)
        email_data = ttk.Label(self.frame1, text=row[4]).place(x=300, y=130)

        birth = ttk.Label(self.frame1, text='Bithday').place(x=40, y=170)
        birth_data = ttk.Label(self.frame1, text=row[5]).place(x=40, y=200)

        gender = ttk.Label(self.frame1, text='Gender').place(x=300, y=170)
        gender_data = ttk.Label(self.frame1, text=row[6]).place(x=300, y=200)

        iden = ttk.Label(self.frame1, text='Identification').place(x=40, y=240)
        iden_data = ttk.Label(self.frame1, text=row[7]).place(x=40, y=270)







if __name__ == '__main__':
    v = ventana()
    v.mainloop()



