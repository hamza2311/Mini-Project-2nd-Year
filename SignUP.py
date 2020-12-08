from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk
import re
from tkinter import messagebox
import MySQLdb


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1265x645+0+0")
        self.root.config(bg='white')
        self.root.wm_iconbitmap('abesit.ico')

        # All Images
        self.bg_icon = ImageTk.PhotoImage(file='bg_image.jpg')
        self.abesit_logo = PhotoImage(file='ABESIT.png')

        bg_label = Label(self.root, image=self.bg_icon)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        abesit_logo = Label(self.root, image=self.abesit_logo, bd=0, bg='white')
        abesit_logo.place(x=70, y=70, width=400, height=500)

        # Login Frame
        login_frame = Frame(self.root, bg='white')
        login_frame.place(x=470, y=70, width=700, height=500)
        login_frame.propagate(0)

        title = Label(login_frame, text='SIGN UP HERE', font=('Times New Roman', 30), bg='white', fg='green')
        title.place(x=50, y=30)

        first_name = Label(login_frame, text='First Name', font=('Times New Roman', 15), bg='white')
        first_name.place(x=50, y=100)
        self.first_name_entry = Entry(login_frame, font=('', 10), bg='lightgrey')
        self.first_name_entry.place(x=50, y=130, width=250)

        last_name = Label(login_frame, text='Last Name', font=('Times New Roman', 15), bg='white')
        last_name.place(x=370, y=100)
        self.last_name_entry = Entry(login_frame, font=('', 10), bg='lightgrey')
        self.last_name_entry.place(x=370, y=130, width=250)

        contact = Label(login_frame, text='Contact No.', font=('Times New Roman', 15), bg='white')
        contact.place(x=50, y=170)
        self.contact_entry = Entry(login_frame, font=('', 10), bg='lightgrey')
        self.contact_entry.place(x=50, y=200, width=250)

        email = Label(login_frame, text='E-mail ID', font=('Times New Roman', 15), bg='white')
        email.place(x=370, y=170)
        self.email_entry = Entry(login_frame, font=('', 10), bg='lightgrey')
        self.email_entry.place(x=370, y=200, width=250)

        security_question = Label(login_frame, text='Security Question', font=('Times New Roman', 15), bg='white')
        security_question.place(x=50, y=240)
        self.security_question_combo = ttk.Combobox(login_frame, font=('Times New Roman', 12), state='readonly',
                                                    justify=CENTER)
        self.security_question_combo['values'] = (
            '----SELECT----',
            'What is your mother\'s first name?',
            'What is your birth month?',
            'What is your first pet\'s name?'
        )
        self.security_question_combo.place(x=50, y=270, width=250)
        self.security_question_combo.current(0)
        answer = Label(login_frame, text='Answer', font=('Times New Roman', 15), bg='white')
        answer.place(x=370, y=240)
        self.answer_entry = Entry(login_frame, font=('', 10), bg='lightgrey')
        self.answer_entry.place(x=370, y=270, width=250)

        password = Label(login_frame, text='Password', font=('Times New Roman', 15), bg='white')
        password.place(x=50, y=310)
        self.password_entry = Entry(login_frame, font=('', 10), bg='lightgrey', show='*')
        self.password_entry.place(x=50, y=340, width=250)

        confirm_password = Label(login_frame, text='Confirm Password', font=('Times New Roman', 15), bg='white')
        confirm_password.place(x=370, y=310)
        self.confirm_password_entry = Entry(login_frame, font=('', 10), bg='lightgrey', show='*')
        self.confirm_password_entry.place(x=370, y=340, width=250)

        image_name = Label(login_frame, text='*Please rename your file as your first name ', font=('Arial', 10, 'italic'),
                           bg='white', fg='grey')
        image_name.place(x=50, y=402)

        self.su_btn_image = PhotoImage(file='signup.png')
        sign_up_button = Button(login_frame, image=self.su_btn_image, bg='white', bd=0, cursor='hand2',
                                command=self.sign_up)
        sign_up_button.place(x=285, y=450)

        self.si_btn_image = PhotoImage(file='signin.png')
        sign_in_button = Button(self.root, image=self.si_btn_image, bg='white', bd=0, cursor='hand2',
                                command=self.sign_in_window)
        sign_in_button.place(x=210, y=480)

    def sign_in_window(self):
        self.root.destroy()
        import SignIN

    def clear(self):
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.security_question_combo.current(0)
        self.answer_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.confirm_password_entry.delete(0, END)

    def first_name_validation(self):
        if len(self.first_name_entry.get()) < 3:
            return True
        elif (
                re.search('[0-9]', self.first_name_entry.get()) or
                re.search('[!@#$%^&*"({})_|/,.<>;:\']', self.first_name_entry.get()) or
                re.search('[ ]', self.first_name_entry.get())
        ):
            return True

    def last_name_validation(self):
        if len(self.first_name_entry.get()) < 3:
            return True
        elif (
                re.search('[0-9]', self.last_name_entry.get()) or
                re.search('[!@#$%^&*"({})_|/,.<>;:\']', self.last_name_entry.get()) or
                re.search('[ ]', self.last_name_entry.get())
        ):
            return True

    def contact_validation(self):
        if (
                len(self.contact_entry.get()) != 10 or
                re.search('[A-Z]', self.contact_entry.get()) or
                re.search('[a-z]', self.contact_entry.get()) or
                re.search('[!@#$%^&*"({})_|/,.<>;:\']', self.contact_entry.get())
        ):
            return True

    def email_validations(self):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex, self.email_entry.get()):
            return True

    def password_validation(self):
        if not re.search('[A-Z]', self.password_entry.get()):
            return True
        elif not re.search('[a-z]', self.password_entry.get()):
            return True
        elif not re.search('[0-9]', self.password_entry.get()):
            return True
        elif not re.search('[_@$]', self.password_entry.get()):
            return True
        elif re.search('[ ]', self.password_entry.get()):
            return True

    def sign_up(self):
        error_title = 'Error'
        types_of_errors = [
         'First Name is required !!',                                                    # 0
         'Please enter a valid name !!',                                                 # 1
         'Last name is required !!',                                                     # 2
         'Contact number is required !!',                                                # 3
         'Please enter a valid contact number !!',                                       # 4
         'E-mail ID is required !!',                                                     # 5
         'Please enter a valid E-mail address !!',                                       # 6
         'Please select a security question !!',                                         # 7
         'Please answer the security question !!',                                       # 8
         'Either password field is empty !!',                                            # 9
         'Password must be minimum of 8 characters and less than 20 characters !!',      # 10
         '''Password must contain one upper, one lower case character, one numeric character and one special character.
         \nIt must not contain any white spaces !!''',                                   # 11
         'Password did not match !!',                                                    # 12
         'Please upload an image for Face ID !!'                                         # 13
        ]
        if self.first_name_entry.get() == '':
            messagebox.showerror(error_title, types_of_errors[0], parent=self.root)
        elif self.last_name_entry.get() == '':
            messagebox.showerror(error_title, types_of_errors[2], parent=self.root)
        elif self.first_name_validation():
            messagebox.showerror(error_title, types_of_errors[1], parent=self.root)
        elif self.last_name_validation():
            messagebox.showerror(error_title, types_of_errors[1], parent=self.root)
        elif self.contact_entry.get() == '':
            messagebox.showerror(error_title, types_of_errors[3], parent=self.root)
        elif self.contact_validation():
            messagebox.showerror(error_title, types_of_errors[4], parent=self.root)
        elif self.email_entry.get() == '':
            messagebox.showerror(error_title, types_of_errors[5], parent=self.root)
        elif self.email_validations():
            messagebox.showerror(error_title, types_of_errors[6], parent=self.root)
        elif self.security_question_combo.get() == '----SELECT----':
            messagebox.showerror(error_title, types_of_errors[7], parent=self.root)
        elif self.answer_entry.get() == '':
            messagebox.showerror(error_title, types_of_errors[8], parent=self.root)
        elif self.password_entry.get() == '' or self.confirm_password_entry.get() == '':
            messagebox.showerror(error_title, types_of_errors[9], parent=self.root)
        elif len(self.password_entry.get()) not in range(8, 20):
            messagebox.showerror(error_title, types_of_errors[10], parent=self.root)
        elif self.password_validation():
            messagebox.showerror(error_title, types_of_errors[11], parent=self.root)
        elif self.password_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror(error_title, types_of_errors[12], parent=self.root)
        else:
            try:
                con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
                cur = con.cursor()
                cur.execute("SELECT * FROM SignUP WHERE `E-mail ID` = '"+str(self.email_entry.get())+"';")
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror('User Already Exists', 'This E-mail ID is already taken !!')
                elif row is None:
                    file_upload = filedialog.askopenfilename(initialdir='/', title='Upload an image for Face ID',
                                                             filetype=(('JPG', '*.jpg'), ('PNG', '*.png'), ('JPEG', '*.jpeg')))
                    if file_upload == '':
                        messagebox.showerror('Error', 'Please select a file to upload !!', parent=self.root)
                    elif file_upload != '':
                        messagebox.showinfo('Success', 'File has been uploaded successfully !!', parent=self.root)
                        cur.execute(
                            'INSERT INTO SignUp (`First Name`, `Last Name`, `Contact No.`, `E-mail ID`, `Security Question`, `Answer`, `Password`, `Face Image`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);',
                            (self.first_name_entry.get(),
                             self.last_name_entry.get(),
                             self.contact_entry.get(),
                             self.email_entry.get(),
                             self.security_question_combo.get(),
                             self.answer_entry.get(),
                             self.password_entry.get(),
                             str(file_upload))
                        )
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success', 'Welcome! {}\nPlease Sign IN into your account'
                                            .format(self.first_name_entry.get()), parent=self.root)
                        self.root.destroy()
                        import SignIN
                        self.clear()
            except Exception as es:
                messagebox.showerror('Error', 'Error due to: {}'.format(str(es)), parent=self.root)


login = Tk()
obj = LoginSystem(login)
login.mainloop()
