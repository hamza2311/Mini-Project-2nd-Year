from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import MySQLdb
import cv2
import face_recognition
from PIL import ImageTk


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

        self.face_id_image = PhotoImage(file='Face ID.png')
        face_id_button = Button(login_frame, image=self.face_id_image, bg='white', bd=0, cursor='hand2',
                                command=self.face_id)
        face_id_button.place(x=420, y=120)

        register = Button(login_frame, text='New? Register Now', bd=0, font=('Arial', 10, 'underline'), bg='white',
                          fg='red', cursor='hand2', command=self.sign_up_window,
                          activebackground='white', activeforeground='purple')
        register.place(x=68, y=280)

        self.si_btn_image = PhotoImage(file='signin.png')
        sign_in_button = Button(login_frame, image=self.si_btn_image, bg='white', bd=0, cursor='hand2',
                                command=self.sign_in)
        sign_in_button.place(x=60, y=310)

        forget_password = Button(login_frame, text='Forget Password ?', bd=0, font=('Arial', 10, 'underline'),
                                 bg='white', fg='red', cursor='hand2', command=self.forget_password_window,
                                 activebackground='white', activeforeground='purple')
        forget_password.place(x=68, y=360)

        self.faculty_login_image = ImageTk.PhotoImage(file='Faculty_Login.jpg')
        faculty_login = Button(login_frame, image=self.faculty_login_image, bg='white', bd=0, cursor='hand2',
                               command=self.faculty_login)
        faculty_login.place(x=220, y=310)

        # Face ID Dataset
        # self.images = []
        # self.class_names = []
        # self.my_list = os.listdir(self.path)
        # self.progress_bar = ttk.Progressbar(self.root, orient=HORIZONTAL, length=200, mode='determinate')
        # self.encode_list = []

    def clear(self):
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def reset(self):
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.security_question_combo.current(0)
        self.security_answer_entry.delete(0, END)
        self.new_password_entry.delete(0, END)

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

    def new_password_validation(self):
        if len(self.new_password_entry.get()) not in range(8, 20):
            return True
        elif not re.search('[A-Z]', self.new_password_entry.get()):
            return True
        elif not re.search('[a-z]', self.new_password_entry.get()):
            return True
        elif not re.search('[0-9]', self.new_password_entry.get()):
            return True
        elif not re.search('[_@$]', self.new_password_entry.get()):
            return True
        elif re.search('[ ]', self.new_password_entry.get()):
            return True

    def sign_up_window(self):
        self.root.destroy()
        import SignUP

    def forget_password_window(self):
        if self.email_entry.get() == '':
            messagebox.showerror('Error', 'Please enter your email address to change password !!', parent=self.root)
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
            cur = con.cursor()
            cur.execute(f"""SELECT * FROM SignUP WHERE `E-mail ID` = '{self.email_entry.get()}';""")
            row = cur.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Sorry, we can not find the e-mail address you have entered.\nPlease register first to sign in.')
            else:
                con.close()
                self.forget = Toplevel()
                self.forget.title('Forget Password')
                self.forget.geometry('400x400+432+132')
                self.forget.focus_force()
                self.forget.grab_set()
                self.forget.config(bg='lightblue')
                self.forget.wm_iconbitmap('abesit.ico')
                security_question = Label(self.forget, text='Security Question', font=('Times New Roman', 15), bg='lightblue')
                security_question.place(x=75, y=90)
                self.security_question_combo = ttk.Combobox(self.forget, font=('Times New Roman', 12), state='readonly',
                                                            justify=CENTER)
                self.security_question_combo['values'] = (
                    '----SELECT----',
                    'What is your mother\'s first name?',
                    'What is your birth month?',
                    'What is your first pet\'s name?'
                )
                self.security_question_combo.place(x=75, y=120, width=250)
                self.security_question_combo.current(0)
                security_answer = Label(self.forget, text='Answer', font=('Times New Roman', 15), bg='lightblue')
                security_answer.place(x=75, y=170)
                self.security_answer_entry = Entry(self.forget, font=('', 10))
                self.security_answer_entry.place(x=75, y=200, width=250)
                new_password = Label(self.forget, text='New Password', font=('Times New Roman', 15), bg='lightblue')
                new_password.place(x=75, y=250)
                self.new_password_entry = Entry(self.forget, font=('', 10), show='*')
                self.new_password_entry.place(x=75, y=280, width=250)
                change_password = Button(self.forget, text='Change Password', font=('Arial', 10, 'bold'), bg='blue',
                                         fg='white', relief=RAISED, command=self.change_password, activeforeground='purple')
                change_password.place(x=130, y=350, width=140, height=30)

    def change_password(self):
        if self.security_question_combo.get() == '----SELECT----':
            messagebox.showerror('Error', 'Please select a security question !!', parent=self.forget)
        elif self.security_answer_entry.get() == '':
            messagebox.showerror('Error', 'Please answer the security question !!', parent=self.forget)
        elif self.new_password_entry.get() == '':
            messagebox.showerror('Error', 'Please enter a password !!', parent=self.forget)
        elif self.new_password_validation():
            messagebox.showerror('Error', 'Password must contain a number, an uppercase letter, a lowercase letter, a special character and must of length between 8 and 20 !!')
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
            cur = con.cursor()
            cur.execute(f'''SELECT * FROM SignUP WHERE `Security Question` = "{self.security_question_combo.get()}"
                            AND Answer = "{self.security_answer_entry.get()}"
                            AND `E-mail ID` = "{self.email_entry.get()}";''')
            row = cur.fetchone()
            if row is None:
                messagebox.showerror('Invalid Credentials', 'Security Question and Password did not match !!')
            else:
                cur.execute(f"""UPDATE SignUP SET Password = '{self.new_password_entry.get()}'
                                WHERE `E-mail ID` = '{self.email_entry.get()}';""")
                messagebox.showinfo('Success', 'Password has been updated successfully !!')
                self.reset()
                self.forget.destroy()
            con.commit()
            con.close()

    def face_id(self):
        face_list = []
        images = []
        encode_list = []
        names = []
        con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
        cur = con.cursor()
        cur.execute('SELECT `Face Image`, `First Name` FROM SignUp;')
        records = cur.fetchall()
        print(records)
        for record in records:
            face_id = record[0]
            face_id = face_id.decode()
            name = record[1]
            face_list.append(face_id)
            names.append(name)
        print(face_list)
        print(names)

        for file in face_list:
            current_image = cv2.imread(file)
            images.append(current_image)

        def find_encodings(faces):
            for img in faces:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encode_list.append(encode)
            return encode_list

        encode_list_known = find_encodings(images)
        cap = cv2.VideoCapture(0)

        while True:
            success, image = cap.read()
            image_resize = cv2.resize(image, (0, 0), None, 0.25, 0.25)
            image_resize = cv2.cvtColor(image_resize, cv2.COLOR_BGR2RGB)

            faces_current_frame = face_recognition.face_locations(image_resize)
            encode_current_frame = face_recognition.face_encodings(image_resize, faces_current_frame)

            for encode_face, face_location in zip(encode_current_frame, faces_current_frame):
                matches = face_recognition.compare_faces(encode_list_known, encode_face)
                distances = face_recognition.face_distance(encode_list_known, encode_face)
                match_index = int(np.argmin(distances))

                if matches[match_index]:
                    cap.release()
                    messagebox.showinfo('Success', f'Welcome to ABESIT {names[match_index]}!')
                    self.root.destroy()
                    import Student_Management_System
                else:
                    cap.release()
                    messagebox.showerror('Access Denied', 'Unauthorised user !!')

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
            con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
            cur = con.cursor()
            cur.execute("SELECT * FROM SignUp WHERE `E-mail ID` = '" + str(self.email_entry.get()) + "' "
                        + "AND Password = '" + str(self.password_entry.get()) + "';")
            row = cur.fetchone()
            if row is None:
                messagebox.showerror('Invalid Credentials', 'Invalid E-mail ID or Password !!', parent=self.root)
            else:
                messagebox.showinfo('Success', 'Welcome to ABESIT !!')
                self.clear()
                self.root.destroy()
                import Student_Management_System
            con.close()

    def faculty_login(self):
        if self.email_entry.get() == '':
            messagebox.showerror('Empty Field', 'Please input the E-mail ID !!', parent=self.root)
        elif self.email_validations():
            messagebox.showerror('Invalid Format', 'Please enter a valid E-mail Id', parent=self.root)
        elif self.password_entry.get() == '':
            messagebox.showerror('Empty Field', 'Password field is empty !!', parent=self.root)
        elif self.password_validation():
            messagebox.showerror('Invalid Format', 'Password did not match the validations', parent=self.root)
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
            cur = con.cursor()
            cur.execute("SELECT * FROM SignUp WHERE `E-mail ID` = '" + str(self.email_entry.get()) + "' "
                        + "AND Password = '" + str(self.password_entry.get()) + "';")
            row = cur.fetchone()
            if row is None:
                messagebox.showerror('Invalid Credentials', 'Invalid E-mail ID or Password !!', parent=self.root)
            else:
                messagebox.showinfo('Success', 'Welcome to ABESIT !!')
                self.clear()
                self.root.destroy()
                import Student_Academics
            con.close()


login = Tk()
obj = LoginSystem(login)
login.mainloop()
