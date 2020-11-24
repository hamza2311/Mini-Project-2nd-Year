from tkinter import *
from tkinter import messagebox, filedialog

import MySQLdb
from PIL import ImageTk, Image


class StudentAcademics:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Academics Detail")
        self.root.geometry("1265x645+0+0")
        self.root.wm_iconbitmap('abesit.ico')
        self.bg_icon = ImageTk.PhotoImage(file='bg_image.jpg')
        bg_label = Label(self.root, image=self.bg_icon)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Student Information Frame
        student_frame = Frame(self.root, bg='white')
        student_frame.place(x=25, y=25, width=430, height=595)

        self.student_image = ImageTk.PhotoImage(file='Student.png')
        self.student_profile = Label(student_frame, anchor=CENTER, image=self.student_image, bg='lightblue',
                                     bd=5, relief=GROOVE)
        self.student_profile.place(x=10, y=10, height=300, width=410)

        student_admission = Label(student_frame, text="Admission No.", font=('Times New Roman', 13), bg='white')
        student_admission.place(x=20, y=350)
        self.admission = Entry(student_frame, font=('Arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.admission.place(x=190, y=350, width=220, height=22)

        student_name = Label(student_frame, text="Student's Name", font=('Times New Roman', 13), bg='white')
        student_name.place(x=20, y=380)
        self.name = Label(student_frame, font=('Arial', 10), bg='lightgrey', bd=1, relief=RIDGE)
        self.name.place(x=190, y=380, width=220, height=22)

        student_branch = Label(student_frame, text="Branch", font=('Times New Roman', 13), bg='white')
        student_branch.place(x=20, y=410)
        self.branch = Label(student_frame, font=('Arial', 10), bg='lightgrey', bd=1, relief=RIDGE)
        self.branch.place(x=190, y=410, width=220, height=22)

        student_email = Label(student_frame, text="E-mail ID", font=('Times New Roman', 13), bg='white')
        student_email.place(x=20, y=440)
        self.email = Label(student_frame, font=('Arial', 10), bg='lightgrey', bd=1, relief=RIDGE)
        self.email.place(x=190, y=440, width=220, height=22)

        student_contact = Label(student_frame, text="Contact No.", font=('Times New Roman', 13), bg='white')
        student_contact.place(x=20, y=470)
        self.contact = Label(student_frame, font=('Arial', 10), bg='lightgrey', bd=1, relief=RIDGE)
        self.contact.place(x=190, y=470, width=220, height=22)

        self.select_image = PhotoImage(file='Select.png')
        select = Button(student_frame, image=self.select_image, bd=0, cursor='hand2', bg='white',
                        command=self.database_connection)
        select.place(x=165, y=550)

        update_image = Button(student_frame, text='Update Photo ?', font=('', 10, 'underline'), bg='white', bd=0,
                              fg='red', activeforeground='purple', activebackground='white', cursor='hand2',
                              command=self.update_photo)
        update_image.place(x=20, y=520)

        # Student Academics Frame
        academics_frame = Frame(self.root, bg="white")
        academics_frame.place(x=480, y=25, width=760, height=595)

        self.logout_image = ImageTk.PhotoImage(file='logout.png')
        logout = Button(academics_frame, image=self.logout_image, bd=0, cursor='hand2', bg='white', command=self.log_out)
        logout.place(x=630, y=20, width=90, height=32)

        student_admission_no = Label(academics_frame, text="Admission No.", font=('Times New Roman', 13), bg='white')
        student_admission_no.place(x=20, y=20)
        self.admission_no = Label(academics_frame, font=('Arial', 10), bg='lightgrey', bd=1, relief=RIDGE)
        self.admission_no.place(x=200, y=20, width=220, height=22)

        subject = Label(academics_frame, text='SUBJECT', bg='white', font=('Times New Roman', 15, 'bold'), anchor=CENTER, bd=1, relief=RIDGE)
        subject.place(x=20, y=100, width=160, height=80)
        coa = Label(academics_frame, text='Computer Organisation\nand Architecture', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        coa.place(x=20, y=180, width=160, height=50)
        uhv = Label(academics_frame, text='Universal Human Values\nand Professional Ethics', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        uhv.place(x=20, y=230, width=160, height=50)
        ds = Label(academics_frame, text='Data Structure', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        ds.place(x=20, y=280, width=160, height=50)
        dstl = Label(academics_frame, text='Discrete Structures\nand Theory of Logic', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        dstl.place(x=20, y=330, width=160, height=50)
        maths = Label(academics_frame, text='Mathematics IV', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        maths.place(x=20, y=380, width=160, height=50)
        python = Label(academics_frame, text='Python', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        python.place(x=20, y=430, width=160, height=50)
        percentage = Label(academics_frame, text='PERCENTAGE', font=('Times New Roman', 10, 'bold'), bg='white', anchor=CENTER, relief=RIDGE)
        percentage.place(x=20, y=480, width=160, height=50)

        marks = Label(academics_frame, text='MARKS', bg='white', font=('Times New Roman', 15, 'bold'), anchor=CENTER, bd=1, relief=RIDGE)
        marks.place(x=180, y=100, width=560, height=30)
        ct1_marks = Label(academics_frame, text='Class Test 1\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        ct1_marks.place(x=180, y=130, width=112, height=50)
        self.ct1_percentage = Label(academics_frame, font=('arial', 10), bg='white', justify='center', relief=RIDGE)
        self.ct1_percentage.place(x=180, y=480, width=112, height=50)
        ct2_marks = Label(academics_frame, text='Class Test 2\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        ct2_marks.place(x=292, y=130, width=112, height=50)
        self.ct2_percentage = Label(academics_frame, font=('arial', 10), bg='white', justify='center', relief=RIDGE)
        self.ct2_percentage.place(x=292, y=480, width=112, height=50)
        st1_marks = Label(academics_frame, text='Sessional Test 1\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        st1_marks.place(x=404, y=130, width=112, height=50)
        self.st1_percentage = Label(academics_frame, font=('arial', 10), bg='white', justify='center', relief=RIDGE)
        self.st1_percentage.place(x=404, y=480, width=112, height=50)
        ct3_marks = Label(academics_frame, text='Class Test 3\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        ct3_marks.place(x=516, y=130, width=112, height=50)
        self.ct3_percentage = Label(academics_frame, font=('arial', 10), bg='white', justify='center', relief=RIDGE)
        self.ct3_percentage.place(x=516, y=480, width=112, height=50)
        st2_marks = Label(academics_frame, text='Sessional Test 2\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        st2_marks.place(x=628, y=130, width=112, height=50)
        self.st2_percentage = Label(academics_frame, font=('arial', 10), bg='white', justify='center', relief=RIDGE)
        self.st2_percentage.place(x=628, y=480, width=112, height=50)

        self.coa_ct1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.coa_ct1_marks.place(x=180, y=180, width=112, height=50)
        self.coa_ct2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.coa_ct2_marks.place(x=292, y=180, width=112, height=50)
        self.coa_st1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.coa_st1_marks.place(x=404, y=180, width=112, height=50)
        self.coa_ct3_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.coa_ct3_marks.place(x=516, y=180, width=112, height=50)
        self.coa_st2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.coa_st2_marks.place(x=628, y=180, width=112, height=50)
        self.uhv_ct1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.uhv_ct1_marks.place(x=180, y=230, width=112, height=50)
        self.uhv_ct2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.uhv_ct2_marks.place(x=292, y=230, width=112, height=50)
        self.uhv_st1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.uhv_st1_marks.place(x=404, y=230, width=112, height=50)
        self.uhv_ct3_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.uhv_ct3_marks.place(x=516, y=230, width=112, height=50)
        self.uhv_st2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.uhv_st2_marks.place(x=628, y=230, width=112, height=50)
        self.ds_ct1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.ds_ct1_marks.place(x=180, y=280, width=112, height=50)
        self.ds_ct2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.ds_ct2_marks.place(x=292, y=280, width=112, height=50)
        self.ds_st1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.ds_st1_marks.place(x=404, y=280, width=112, height=50)
        self.ds_ct3_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.ds_ct3_marks.place(x=516, y=280, width=112, height=50)
        self.ds_st2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.ds_st2_marks.place(x=628, y=280, width=112, height=50)
        self.dstl_ct1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.dstl_ct1_marks.place(x=180, y=330, width=112, height=50)
        self.dstl_ct2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.dstl_ct2_marks.place(x=292, y=330, width=112, height=50)
        self.dstl_st1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.dstl_st1_marks.place(x=404, y=330, width=112, height=50)
        self.dstl_ct3_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.dstl_ct3_marks.place(x=516, y=330, width=112, height=50)
        self.dstl_st2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.dstl_st2_marks.place(x=628, y=330, width=112, height=50)
        self.maths_ct1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.maths_ct1_marks.place(x=180, y=380, width=112, height=50)
        self.maths_ct2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.maths_ct2_marks.place(x=292, y=380, width=112, height=50)
        self.maths_st1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.maths_st1_marks.place(x=404, y=380, width=112, height=50)
        self.maths_ct3_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.maths_ct3_marks.place(x=516, y=380, width=112, height=50)
        self.maths_st2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.maths_st2_marks.place(x=628, y=380, width=112, height=50)
        self.python_ct1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.python_ct1_marks.place(x=180, y=430, width=112, height=50)
        self.python_ct2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.python_ct2_marks.place(x=292, y=430, width=112, height=50)
        self.python_st1_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.python_st1_marks.place(x=404, y=430, width=112, height=50)
        self.python_ct3_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.python_ct3_marks.place(x=516, y=430, width=112, height=50)
        self.python_st2_marks = Label(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1, relief=RIDGE)
        self.python_st2_marks.place(x=628, y=430, width=112, height=50)

    def reset(self):
        self.student_profile.config(image=self.student_image)

    def database_connection(self):
        con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
        cur1 = con.cursor()
        cur1.execute(f"""SELECT `Student's Name`, `Branch`, `E-mail ID`, `Contact No.`, `Face Image`
                         FROM Student WHERE `Admission No.` = '{self.admission.get()}';""")
        cur2 = con.cursor()
        cur2.execute(f"""SELECT coa_ct1, coa_ct2, coa_st1, coa_ct3, coa_st2, uhv_ct1, uhv_ct2, uhv_st1, uhv_ct3,
                         uhv_st2, ds_ct1, ds_ct2, ds_st1, ds_ct3, ds_st2, dstl_ct1, dstl_ct2, dstl_st1, dstl_ct3,
                         dstl_st2, maths_ct1, maths_ct2, maths_st1, maths_ct3, maths_st2, python_ct1, python_ct2,
                         python_st1, python_ct3, python_st2
                         FROM Academics WHERE admission_no = '{self.admission.get()}';""")
        if self.admission.get() == '':
            messagebox.showerror('Empty Field', 'Please enter the Admission No. !!', parent=self.root)
        else:
            record = cur1.fetchone()
            if record is None:
                messagebox.showerror('Empty Record', 'Record not found !!', parent=self.root)
            else:
                self.admission_no.config(text=self.admission.get())
                self.name.config(text=record[0])
                self.branch.config(text=record[1])
                self.email.config(text=record[2])
                self.contact.config(text=record[3])
                self.student_image = ImageTk.PhotoImage(Image.open(record[4]))
                # self.student_image = resizeimage.resize_height(self.student_image, 300)
                self.student_profile.configure(image=self.student_image)
            row = cur2.fetchone()
            if row is not None:
                self.coa_ct1_marks.config(text=row[0])
                self.coa_ct2_marks.config(text=row[1])
                self.coa_st1_marks.config(text=row[2])
                self.coa_ct3_marks.config(text=row[3])
                self.coa_st2_marks.config(text=row[4])
                self.uhv_ct1_marks.config(text=row[5])
                self.uhv_ct2_marks.config(text=row[6])
                self.uhv_st1_marks.config(text=row[7])
                self.uhv_ct3_marks.config(text=row[8])
                self.uhv_st2_marks.config(text=row[9])
                self.ds_ct1_marks.config(text=row[10])
                self.ds_ct2_marks.config(text=row[11])
                self.ds_st1_marks.config(text=row[12])
                self.ds_ct3_marks.config(text=row[13])
                self.ds_st2_marks.config(text=row[14])
                self.dstl_ct1_marks.config(text=row[15])
                self.dstl_ct2_marks.config(text=row[16])
                self.dstl_st1_marks.config(text=row[17])
                self.dstl_ct3_marks.config(text=row[18])
                self.dstl_st2_marks.config(text=row[19])
                self.maths_ct1_marks.config(text=row[20])
                self.maths_ct2_marks.config(text=row[21])
                self.maths_st1_marks.config(text=row[22])
                self.maths_ct3_marks.config(text=row[23])
                self.maths_st2_marks.config(text=row[24])
                self.python_ct1_marks.config(text=row[25])
                self.python_ct2_marks.config(text=row[26])
                self.python_st1_marks.config(text=row[27])
                self.python_ct3_marks.config(text=row[28])
                self.python_st2_marks.config(text=row[29])
                self.percentage_calculate()
        con.commit()
        con.close()

    def percentage_calculate(self):
        ct1_percent = ((self.coa_ct1_marks.cget('text') + self.uhv_ct1_marks.cget('text') + self.ds_ct1_marks.cget('text')
                       + self.dstl_ct1_marks.cget('text') + self.maths_ct1_marks.cget('text') + self.python_ct1_marks.cget('text')) / 120) * 100
        self.ct1_percentage.config(text='{:.2f} %'.format(ct1_percent))
        ct2_percent = ((self.coa_ct2_marks.cget('text') + self.uhv_ct2_marks.cget('text') + self.ds_ct2_marks.cget('text')
                        + self.dstl_ct2_marks.cget('text') + self.maths_ct2_marks.cget('text') + self.python_ct2_marks.cget('text')) / 120) * 100
        self.ct2_percentage.config(text='{:.2f} %'.format(ct2_percent))
        st1_percent = ((self.coa_st1_marks.cget('text') + self.uhv_st1_marks.cget('text') + self.ds_st1_marks.cget('text')
                        + self.dstl_st1_marks.cget('text') + self.maths_st1_marks.cget('text') + self.python_st1_marks.cget('text')) / 600) * 100
        self.st1_percentage.config(text='{:.2f} %'.format(st1_percent))
        ct3_percent = ((self.coa_ct3_marks.cget('text') + self.uhv_ct3_marks.cget('text') + self.ds_ct3_marks.cget('text')
                        + self.dstl_ct3_marks.cget('text') + self.maths_ct3_marks.cget('text') + self.python_ct3_marks.cget('text')) / 120) * 100
        self.ct3_percentage.config(text='{:.2f} %'.format(ct3_percent))
        st2_percent = ((self.coa_st2_marks.cget('text') + self.uhv_st2_marks.cget('text') + self.ds_st2_marks.cget('text')
                        + self.dstl_st2_marks.cget('text') + self.maths_st2_marks.cget('text') + self.python_st2_marks.cget('text')) / 600) * 100
        self.st2_percentage.config(text='{:.2f} %'.format(st2_percent))

    def log_out(self):
        self.root.destroy()
        import SignIN

    def update_photo(self):
        file_upload = filedialog.askopenfilename(initialdir='/', title='Update image for Face ID',
                                                 filetype=(('JPG', '*.jpg'), ('PNG', '*.png'), ('JPEG', '*.jpeg')))
        if file_upload == '':
            messagebox.showerror('Error', 'Please select a file to upload !!', parent=self.root)
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
            cur = con.cursor()
            cur.execute(f"""UPDATE Student SET `Face Image` = '{file_upload}'
                            WHERE `E-mail ID` = '{self.email.cget("text")}';""")
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'File has been uploaded successfully !!', parent=self.root)
            self.reset()


academics = Tk()
obj = StudentAcademics(academics)
academics.mainloop()
