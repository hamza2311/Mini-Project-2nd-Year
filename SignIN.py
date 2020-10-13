from tkinter import *
from tkinter import messagebox

import MySQLdb
from PIL import ImageTk


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1250x640+0+0")
        self.root.config(bg='white')
        self.root.wm_iconbitmap('abesit.ico')

        # All Images
        self.bg_icon = ImageTk.PhotoImage(file='bg_image.jpg')
        self.abesit_logo = PhotoImage(file='ABESIT.png')

        bg_label = Label(self.root, image=self.bg_icon)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        abesit_logo = Label(self.root, image=self.abesit_logo, bd=0, bg='white')
        abesit_logo.place(x=120, y=120, width=400, height=400)

        # Login Frame
        login_frame = Frame(self.root, bg='white')
        login_frame.place(x=520, y=120, width=600, height=400)
        login_frame.propagate(0)

        title = Label(login_frame, text='SIGN IN HERE', font=('Times New Roman', 30), bg='white', fg='blue')
        title.place(x=60, y=30)

        email = Label(login_frame, text='E-mail ID', font=('Times New Roman', 15), bg='white')
        email.place(x=60, y=100)
        self.email_entry = Entry(login_frame, font=('', 10), bg='lightgrey')
        self.email_entry.place(x=60, y=130, width=280)

        password = Label(login_frame, text='Password', font=('Times New Roman', 15), bg='white')
        password.place(x=60, y=180)
        self.password_entry = Entry(login_frame, font=('', 10), bg='lightgrey', show='*')
        self.password_entry.place(x=60, y=210, width=280)

        register = Button(login_frame, text='New? Register Now', bd=0, font=('Arial', 10, 'underline'), bg='white',
                          fg='red', cursor='hand2', command=self.sign_up_window,
                          activebackground='white', activeforeground='purple')
        register.place(x=68, y=300)

        self.si_btn_image = PhotoImage(file='signin.png')
        sign_in_button = Button(login_frame, image=self.si_btn_image, bg='white', bd=0, cursor='hand2',
                                command=self.sign_in)
        sign_in_button.place(x=60, y=330)

    def clear(self):
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def email_validations(self):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex, self.email_entry.get()):
            return True

    def password_validation(self):
        if len(self.password_entry.get()) not in range(8, 20):
            return True
        elif not re.search('[A-Z]', self.password_entry.get()):
            return True
        elif not re.search('[a-z]', self.password_entry.get()):
            return True
        elif not re.search('[0-9]', self.password_entry.get()):
            return True
        elif not re.search('[_@$]', self.password_entry.get()):
            return True
        elif re.search('[ ]', self.password_entry.get()):
            return True

    def sign_up_window(self):
        self.root.destroy()
        import SignUP

    def sign_in(self):
        if self.email_entry.get() == '':
            messagebox.showerror('Empty Field', 'Please input the E-mail ID !!', parent=self.root)
        elif self.email_validations():
            messagebox.showerror('Invalid Format', 'Please enter a valid E-mail Id', parent=self.root)
        elif self.password_entry.get() == '':
            messagebox.showerror('Empty Field', 'Password field is empty !!', parent=self.root)
        elif self.password_validation():
            messagebox.showerror('Invalid Format', 'Password did not match the validations', parent=self.root)
        else:
            try:
                con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
                cur = con.cursor()
                cur.execute("SELECT * FROM SignUp WHERE `E-mail ID` = '" + str(self.email_entry.get()) + "' "
                            + "AND Password = '" + str(self.password_entry.get()) + "';")
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror('Invalid Credentials', 'Invalid E-mail ID or Password !!', parent=self.root)
                else:
                    messagebox.showinfo('Success', 'Welcome to ABESIT !!')
                    self.root.destroy()
                    import Student_Management_System
                    self.clear()
                con.close()
            finally:
                self.root.destroy()


login = Tk()
obj = LoginSystem(login)
login.mainloop()
