import tkinter as tk
from tkinter import ttk, messagebox
from functools import partial
import psycopg2 as pg
from logger_base import log
import sys


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('780x480')
        self.config(bg="white")
        self.title('BD')

        # Credentials Database
        self._con = None
        self._cur = None
        self._DATABASE = 'clients_2023'
        self._USERNAME = 'postgres'
        self._PASSWORD = 'ADMIN'
        self._DB_PORT = '5432'
        self._HOST = 'localhost'

        # SQL statements
        self._SELECT = 'SELECT * FROM clients WHERE identification =%s '
        self._ADD = 'INSERT INTO clients(name,last_name,age,email,birthday,gender,identification) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        self._UPDATE = 'UPDATE clients SET name =%s, last_name =%s, age =%s,email = %s, birthday = %s, gender = %s WHERE identification=%s '
        self._DELETE = 'DELETE FROM clients WHERE identification = %s'

        # Initialize style
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('TFrame', background='green')
        s.configure('Frame1.TFrame', background='white')
        s.configure('Frame2.TFrame', background='black')

        # left frame
        self.frame1 = ttk.Frame(self, style='Frame1.TFrame')
        self.frame1.place(x=0, y=0, width=540, relheight=1)

        # right frame
        self.frame2 = ttk.Frame(self, style='Frame2.TFrame')
        self.frame2.place(x=540, y=0, relwidth=1, relheight=1)

        # buttons
        self.b_add = ttk.Button(self.frame2, text='Add Client', cursor='hand2', command=self.addClient).place(x=68,y=60,width=100)
        self.b_show_clients = ttk.Button(self.frame2, text='Show Clients', cursor='hand2',command=self.showClient).place(x=68, y=120, width=100)
        self.b_update_clients = ttk.Button(self.frame2, text='Update Client', cursor='hand2',command=self.updateClient).place(x=68, y=180, width=100)
        self.b_delete_client = ttk.Button(self.frame2, text='Delete Client', cursor='hand2',command=self.deleteClient).place(x=68, y=240, width=100)
        self.b_clearbd = ttk.Button(self.frame2, text='Clear DB', cursor='hand2', command=self.clearScreen).place(x=68,
                                                                                                                  y=300,                                                                                                                 width=100)
        self.b_exit = ttk.Button(self.frame2, text='Exit', cursor='hand2', command=exit).place(x=68, y=360, width=100)

        # Components to add data

        # Add componeents to view addClient

        """
        This function creates a form for adding a new client with various fields and a button to submit
        the form.
        """

    def addClient(self):

        self.clearScreen()
        self.name = ttk.Label(self.frame1, text='Name', ).place(x=40, y=30)
        self.entry_name = ttk.Entry(self.frame1)
        self.entry_name.place(x=40, y=60, width=130)

        self.last_name = ttk.Label(self.frame1, text='Last name', ).place(x=300, y=30)
        self.entry_last_name = ttk.Entry(self.frame1)
        self.entry_last_name.place(x=300, y=60, width=130)

        self.age = ttk.Label(self.frame1, text='Age').place(x=40, y=100)
        self.entry_age = ttk.Entry(self.frame1)
        self.entry_age.place(x=40, y=130)

        self.email = ttk.Label(self.frame1, text='Email').place(x=300, y=100)
        self.entry_email = ttk.Entry(self.frame1)
        self.entry_email.place(x=300, y=130)

        self.birth = ttk.Label(self.frame1, text='Bithday').place(x=40, y=170)
        self.entry_birth = ttk.Entry(self.frame1)
        self.entry_birth.place(x=40, y=200)

        self.gender = ttk.Label(self.frame1, text='Gender').place(x=300, y=170)
        self.entry_gender = ttk.Entry(self.frame1)
        self.entry_gender.place(x=300, y=200)

        self.identification = ttk.Label(self.frame1, text='Identification').place(x=40, y=240)
        self.entry_identificaction = ttk.Entry(self.frame1)
        self.entry_identificaction.place(x=40, y=270)

        self.image = tk.PhotoImage(file='bt.png')
        self.b_send = ttk.Button(self.frame1, image=self.image, cursor="hand2", command=self.addNewClient).place(x=200,y=320)

    # Show the info of the client from your id

    def showClient(self):

        self.clearScreen()
        self.get_info = ttk.Label(self.frame1, text='Type the client\'s id to watch the onformation').place(x=120, y=70)
        self.enty_get_info = ttk.Entry(self.frame1)
        self.enty_get_info.place(x=163, y=110, width=200, height=30)
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1, image=self.image, cursor="hand2", command=self.checkContactView).place(x=200, y=320)

    # Update a client from is, this function call other function which allow check the give id

    def updateClient(self):
        self.clearScreen()
        self.getInfo = ttk.Label(self.frame1, text="Enter client's ID to update").place(x=160, y=70)
        self.getInfo_entry = ttk.Entry(self.frame1)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1, image=self.image, cursor="hand2", command=self.checkContactUpdate).place(x=220, y=150)

    """
        This function creates a GUI interface to prompt the user to enter a client's ID to be deleted
        and calls another function to delete the client from the database.
        """

    def deleteClient(self):

        self.clearScreen()

        self.getInfo = ttk.Label(self.frame1, text="Enter client's ID to DELETE").place(x=160, y=70)
        self.getInfo_entry = ttk.Entry(self.frame1)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.image = tk.PhotoImage(file='bt.png')
        self.b_send2 = ttk.Button(self.frame1, image=self.image, cursor="hand2", command=self.deleteClientDb).place(x=220, y=150)

    # the above function exits the program and destroys the current instance.

    def exit(self):

        self.destroy()
        sys.exit()

    # Get the conexion and cursor with the PostgresSql using with operator

    def getConextion(self):
        if self._con is None:
            try:
                self._con = pg.connect(host=self._HOST, user=self._USERNAME, password=self._PASSWORD,
                                       database=self._DATABASE,
                                       port=self._DB_PORT)
                log.info('Succesfull conexion')
                return self._con
            except Exception as E:
                log.error('Has ocurred an excepction during the conextion')
        else:
            return self._con

    def getCursor(self):
        if self._cur is None:
            try:
                self._cur = self.getConextion().cursor()
                log.info('The cursor was executed correctly')
                return self._cur
            except Exception as e:
                log.error('Has ocurred an excepction during the creation the cursor')
        else:
            return self._cur

        """
        This function checks if an ID exists in a database and displays the details of the client if it
        does. If the ID is not provided or does not exist, an error message is displayed.
        """

    def checkContactView(self):

        if self.enty_get_info.get() == "":
            messagebox.showerror('Error !', 'Please put your ID')
        else:
            try:
                with self.getConextion() as conn:
                    with conn.cursor() as cur:
                        cur.execute(self._SELECT, (self.enty_get_info.get(),))
                        row = cur.fetchone()
                        if row == None:
                            messagebox.showerror("Error!", "ID doesn't exists", parent=self)

                        else:
                            self.getDetailsClient(row)
            except Exception as e:
                messagebox.showerror('Error!', f'Error: {str(e)}', parent=self)

    # Remove all widgets from the frame 1

    def clearScreen(self, ):
        for widget in self.frame1.winfo_children():
            widget.destroy()

    """
        This function displays client details on a GUI using tkinter.

        :param row: The parameter "row" is likely a list or tuple containing information about a client,
        such as their first name, last name, age, email, birthday, gender, and identification number.
        The function "getDetailsClient" uses this information to create labels displaying the client's
        details on a graphical user
    """

    def getDetailsClient(self, row):

        self.clearScreen()
        name = ttk.Label(self.frame1, text='First Name').place(x=40, y=30)
        name_data = ttk.Label(self.frame1, text=row[1]).place(x=40, y=60)

        last_name = ttk.Label(self.frame1, text='Last Name').place(x=300, y=30)
        last_name_data = ttk.Label(self.frame1, text=row[2]).place(x=300, y=60)

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

    """
        This function adds a new client to a database if all required fields are filled, otherwise it
        displays an error message.
    """

    def addNewClient(self):
        if self.entry_name.get() == "" or self.entry_last_name.get() == "" or self.entry_age.get() == "" or self.entry_email.get() == "" or self.entry_birth.get() == "" or self.entry_gender.get() == "" or self.entry_identificaction.get() == "":
            messagebox.showerror('Error !', 'Sorry! But you must complete al fields', parent=self)
        else:
            try:
                with self.getConextion() as con:
                    with con.cursor() as cur:
                        cur.execute(self._SELECT, (self.entry_identificaction.get(),))
                        row = cur.fetchone()

                        if row == None:
                            cur.execute(self._ADD, (
                                self.entry_name.get(),
                                self.entry_last_name.get(),
                                self.entry_age.get(),
                                self.entry_email.get(),
                                self.entry_birth.get(),
                                self.entry_gender.get(),
                                self.entry_identificaction.get()
                            ))
                            messagebox.showinfo('Donde', 'The data has been submited to DB')
                            self.resetValues()
                        else:
                            messagebox.showinfo('Error !', 'This id is alredy exists, try again with other  number',
                                                parent=self)
            except Exception as e:
                messagebox.showerror("Error !", f"Error: {str(e)}", parent=self)

    # The function resets the values of several entry fields in a GUI.

    def resetValues(self):

        self.entry_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_birth.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)
        self.entry_identificaction.delete(0, tk.END)

    """
        This function checks if a contact's information needs to be updated and displays an error
        message if necessary.
    """

    def checkContactUpdate(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror('Error !', 'Please put your id')
        else:
            try:
                with self.getConextion() as con:
                    with con.cursor() as cur:
                        cur.execute(self._SELECT, (self.getInfo_entry.get(),))
                        row = cur.fetchone()
                        if row == None:
                            messagebox.showerror("Error!", "ID doesn't exists", parent=self)
                        else:
                            self.getUpdateDetails(row)
            except Exception as e:
                messagebox.showerror('Error!!', f'Error: {str(e)}', parent=self)

    """
        This function creates a form with pre-filled entries for updating user details and a button to
        submit the changes.

        :param row: The parameter "row" is likely a list or tuple containing data for a single row of a
        table or database. The data in the row is used to pre-fill the entry fields in the graphical
        user interface created by this function. The function is likely part of a larger program that
        allows the user to
    """

    def getUpdateDetails(self, row):

        self.clearScreen()
        self.name = ttk.Label(self.frame1, text='Name', ).place(x=40, y=30)
        self.entry_name = ttk.Entry(self.frame1)
        self.entry_name.insert(0, row[1])
        self.entry_name.place(x=40, y=60, width=130)

        self.last_name = ttk.Label(self.frame1, text='Last name', ).place(x=300, y=30)
        self.entry_last_name = ttk.Entry(self.frame1)
        self.entry_last_name.insert(0, row[2])
        self.entry_last_name.place(x=300, y=60, width=130)

        self.age = ttk.Label(self.frame1, text='Age').place(x=40, y=100)
        self.entry_age = ttk.Entry(self.frame1)
        self.entry_age.insert(0, row[3])
        self.entry_age.place(x=40, y=130)

        self.email = ttk.Label(self.frame1, text='Email').place(x=300, y=100)
        self.entry_email = ttk.Entry(self.frame1)
        self.entry_email.insert(0, row[4])
        self.entry_email.place(x=300, y=130)

        self.birth = ttk.Label(self.frame1, text='Bithday').place(x=40, y=170)
        self.entry_birth = ttk.Entry(self.frame1)
        self.entry_birth.insert(0, row[5])
        self.entry_birth.place(x=40, y=200)

        self.gender = ttk.Label(self.frame1, text='Gender').place(x=300, y=170)
        self.entry_gender = ttk.Entry(self.frame1)
        self.entry_gender.insert(0, row[6])
        self.entry_gender.place(x=300, y=200)

        id = ttk.Label(self.frame1, text='Identification').place(x=40, y=240)
        id_data = ttk.Label(self.frame1, text=row[7]).place(x=40, y=270)

        self.image = tk.PhotoImage(file='bt.png')
        self.b_send = ttk.Button(self.frame1, image=self.image, cursor="hand2"command=partial(self.updateDetails, row)).place(x=200, y=320)

    """
        This function updates contact details in a database and displays error messages if required
        fields are not filled or if the contact number does not exist.

        :param row: The parameter "row" is a tuple that contains the data of a specific contact in the
        database. It is used to identify the contact that needs to be updated
    """

    def updateDetails(self, row):

        if self.entry_name.get() == "" or self.entry_last_name.get() == "" or self.entry_age.get() == "" or self.entry_email.get() == "" or self.entry_birth.get() == "" or self.entry_gender.get() == "":
            messagebox.showerror('Error !', 'Sorry! But you must complete al fields', parent=self)
        else:
            try:
                with self.getConextion() as con:
                    with con.cursor() as cur:
                        cur.execute(self._SELECT, (row[7],))
                        row = cur.fetchone()
                        if row == None:
                            messagebox.showerror("Error!", "Contact number doesn't exists", parent=self)
                        else:
                            cur.execute(self._UPDATE, (
                                self.entry_name.get(),
                                self.entry_last_name.get(),
                                self.entry_age.get(),
                                self.entry_email.get(),
                                self.entry_birth.get(),
                                self.entry_gender.get(),
                                row[7]
                            ))
                            messagebox.showinfo('Done!', "The data has been updated")
                            self.clearScreen()
            except Exception as e:
                messagebox.showerror('Error!!', f'Error to update: {str(e)}', parent=self)

    """
        This function deletes a client's data from a database based on their ID, and displays error
        messages if necessary.
    """

    def deleteClientDb(self):

        if self.getInfo_entry.get() == "":
            messagebox.showerror('Error !', 'Please put your id')
        else:
            try:
                with self.getConextion() as con:
                    with con.cursor() as cur:
                        cur.execute(self._SELECT, (self.getInfo_entry.get(),))
                        row = cur.fetchone()
                        if row == None:
                            messagebox.showerror("Error!", "Contact number doesn't exists", parent=self)
                        else:
                            cur.execute(self._DELETE, (self.getInfo_entry.get(),))
                            messagebox.showinfo('Done!', "The data has been deleted")
                            self.clearScreen()
            except Exception as e:
                messagebox.showerror("Error !", f"Error: {str(e)}", parent=self)

'''
    The above code is creating an instance of a class called `Window` and running its `mainloop()`
    method. The `if __name__ == '__main__':` statement ensures that the code inside it only runs if the
    script is being run directly and not being imported as a module.
'''

if __name__ == '__main__':
    v = Window()
    v.mainloop()







