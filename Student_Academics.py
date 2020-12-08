from tkinter import *
from tkinter import messagebox

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

        # Academics Table
        self.coa_ct1 = IntVar()
        self.coa_ct2 = IntVar()
        self.coa_st1 = IntVar()
        self.coa_ct3 = IntVar()
        self.coa_st2 = IntVar()
        self.uhv_ct1 = IntVar()
        self.uhv_ct2 = IntVar()
        self.uhv_st1 = IntVar()
        self.uhv_ct3 = IntVar()
        self.uhv_st2 = IntVar()
        self.ds_ct1 = IntVar()
        self.ds_ct2 = IntVar()
        self.ds_st1 = IntVar()
        self.ds_ct3 = IntVar()
        self.ds_st2 = IntVar()
        self.dstl_ct1 = IntVar()
        self.dstl_ct2 = IntVar()
        self.dstl_st1 = IntVar()
        self.dstl_ct3 = IntVar()
        self.dstl_st2 = IntVar()
        self.maths_ct1 = IntVar()
        self.maths_ct2 = IntVar()
        self.maths_st1 = IntVar()
        self.maths_ct3 = IntVar()
        self.maths_st2 = IntVar()
        self.python_ct1 = IntVar()
        self.python_ct2 = IntVar()
        self.python_st1 = IntVar()
        self.python_ct3 = IntVar()
        self.python_st2 = IntVar()

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

        marks = Label(academics_frame, text='MARKS', bg='white', font=('Times New Roman', 15, 'bold'), anchor=CENTER, bd=1, relief=RIDGE)
        marks.place(x=180, y=100, width=560, height=30)
        ct1_marks = Label(academics_frame, text='Class Test 1\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        ct1_marks.place(x=180, y=130, width=112, height=50)
        ct2_marks = Label(academics_frame, text='Class Test 2\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        ct2_marks.place(x=292, y=130, width=112, height=50)
        st1_marks = Label(academics_frame, text='Sessional Test 1\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        st1_marks.place(x=404, y=130, width=112, height=50)
        ct3_marks = Label(academics_frame, text='Class Test 3\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        ct3_marks.place(x=516, y=130, width=112, height=50)
        st2_marks = Label(academics_frame, text='Sessional Test 2\nMarks', bg='white', font=('Times New Roman', 12), anchor=CENTER, bd=1, relief=RIDGE)
        st2_marks.place(x=628, y=130, width=112, height=50)

        coa_ct1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.coa_ct1, relief=RIDGE)
        coa_ct1_marks.place(x=180, y=180, width=112, height=50)
        coa_ct2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.coa_ct2, relief=RIDGE)
        coa_ct2_marks.place(x=292, y=180, width=112, height=50)
        coa_st1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.coa_st1, relief=RIDGE)
        coa_st1_marks.place(x=404, y=180, width=112, height=50)
        coa_ct3_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.coa_ct3, relief=RIDGE)
        coa_ct3_marks.place(x=516, y=180, width=112, height=50)
        coa_st2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.coa_st2, relief=RIDGE)
        coa_st2_marks.place(x=628, y=180, width=112, height=50)

        uhv_ct1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.uhv_ct1, relief=RIDGE)
        uhv_ct1_marks.place(x=180, y=230, width=112, height=50)
        uhv_ct2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.uhv_ct2, relief=RIDGE)
        uhv_ct2_marks.place(x=292, y=230, width=112, height=50)
        uhv_st1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.uhv_st1, relief=RIDGE)
        uhv_st1_marks.place(x=404, y=230, width=112, height=50)
        uhv_ct3_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.uhv_ct3, relief=RIDGE)
        uhv_ct3_marks.place(x=516, y=230, width=112, height=50)
        uhv_st2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                              textvariable=self.uhv_st2, relief=RIDGE)
        uhv_st2_marks.place(x=628, y=230, width=112, height=50)

        ds_ct1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                             textvariable=self.ds_ct1, relief=RIDGE)
        ds_ct1_marks.place(x=180, y=280, width=112, height=50)
        ds_ct2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                             textvariable=self.ds_ct2, relief=RIDGE)
        ds_ct2_marks.place(x=292, y=280, width=112, height=50)
        ds_st1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                             textvariable=self.ds_st1, relief=RIDGE)
        ds_st1_marks.place(x=404, y=280, width=112, height=50)
        ds_ct3_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                             textvariable=self.ds_ct3, relief=RIDGE)
        ds_ct3_marks.place(x=516, y=280, width=112, height=50)
        ds_st2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                             textvariable=self.ds_st2, relief=RIDGE)
        ds_st2_marks.place(x=628, y=280, width=112, height=50)

        dstl_ct1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                               textvariable=self.dstl_ct1, relief=RIDGE)
        dstl_ct1_marks.place(x=180, y=330, width=112, height=50)
        dstl_ct2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                               textvariable=self.dstl_ct2, relief=RIDGE)
        dstl_ct2_marks.place(x=292, y=330, width=112, height=50)
        dstl_st1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                               textvariable=self.dstl_st1, relief=RIDGE)
        dstl_st1_marks.place(x=404, y=330, width=112, height=50)
        dstl_ct3_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                               textvariable=self.dstl_ct3, relief=RIDGE)
        dstl_ct3_marks.place(x=516, y=330, width=112, height=50)
        dstl_st2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                               textvariable=self.dstl_st2, relief=RIDGE)
        dstl_st2_marks.place(x=628, y=330, width=112, height=50)

        maths_ct1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                textvariable=self.maths_ct1, relief=RIDGE)
        maths_ct1_marks.place(x=180, y=380, width=112, height=50)
        maths_ct2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                textvariable=self.maths_ct2, relief=RIDGE)
        maths_ct2_marks.place(x=292, y=380, width=112, height=50)
        maths_st1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                textvariable=self.maths_st1, relief=RIDGE)
        maths_st1_marks.place(x=404, y=380, width=112, height=50)
        maths_ct3_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                textvariable=self.maths_ct3, relief=RIDGE)
        maths_ct3_marks.place(x=516, y=380, width=112, height=50)
        maths_st2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                textvariable=self.maths_st2, relief=RIDGE)
        maths_st2_marks.place(x=628, y=380, width=112, height=50)

        python_ct1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                 textvariable=self.python_ct1, relief=RIDGE)
        python_ct1_marks.place(x=180, y=430, width=112, height=50)
        python_ct2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                 textvariable=self.python_ct2, relief=RIDGE)
        python_ct2_marks.place(x=292, y=430, width=112, height=50)
        python_st1_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                 textvariable=self.python_st1, relief=RIDGE)
        python_st1_marks.place(x=404, y=430, width=112, height=50)
        python_ct3_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                 textvariable=self.python_ct3, relief=RIDGE)
        python_ct3_marks.place(x=516, y=430, width=112, height=50)
        python_st2_marks = Entry(academics_frame, font=('arial', 10), bg='lightgrey', justify='center', bd=1,
                                 textvariable=self.python_st2, relief=RIDGE)
        python_st2_marks.place(x=628, y=430, width=112, height=50)

        self.update_image = PhotoImage(file='update.png')
        update = Button(academics_frame, image=self.update_image, bg='white', bd=0, cursor='hand2', command=self.update_marks)
        update.place(x=335, y=550, width=90, height=32)

    def ct_marks_validation(self):
        if self.coa_ct1.get() not in range(21):
            return True
        elif self.coa_ct2.get() not in range(21):
            return True
        elif self.coa_ct3.get() not in range(21):
            return True
        elif self.uhv_ct1.get() not in range(21):
            return True
        elif self.uhv_ct2.get() not in range(21):
            return True
        elif self.uhv_ct3.get() not in range(21):
            return True
        elif self.ds_ct1.get() not in range(21):
            return True
        elif self.ds_ct2.get() not in range(21):
            return True
        elif self.ds_ct3.get() not in range(21):
            return True
        elif self.dstl_ct1.get() not in range(21):
            return True
        elif self.dstl_ct2.get() not in range(21):
            return True
        elif self.dstl_ct3.get() not in range(21):
            return True
        elif self.maths_ct1.get() not in range(21):
            return True
        elif self.maths_ct2.get() not in range(21):
            return True
        elif self.maths_ct3.get() not in range(21):
            return True
        elif self.python_ct1.get() not in range(21):
            return True
        elif self.python_ct2.get() not in range(21):
            return True
        elif self.python_ct3.get() not in range(21):
            return True

    def st_marks_validation(self):
        if self.coa_st1.get() not in range(101):
            return True
        elif self.coa_st2.get() not in range(101):
            return True
        elif self.uhv_st1.get() not in range(101):
            return True
        elif self.uhv_st2.get() not in range(101):
            return True
        elif self.ds_st1.get() not in range(101):
            return True
        elif self.ds_st2.get() not in range(101):
            return True
        elif self.dstl_st1.get() not in range(101):
            return True
        elif self.dstl_st2.get() not in range(101):
            return True
        elif self.maths_st1.get() not in range(101):
            return True
        elif self.maths_st2.get() not in range(101):
            return True
        elif self.python_st1.get() not in range(101):
            return True
        elif self.python_st2.get() not in range(101):
            return True

    def database_connection(self):
        con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
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
                self.coa_ct1.set(row[0])
                self.coa_ct2.set(row[1])
                self.coa_st1.set(row[2])
                self.coa_ct3.set(row[3])
                self.coa_st2.set(row[4])
                self.uhv_ct1.set(row[5])
                self.uhv_ct2.set(row[6])
                self.uhv_st1.set(row[7])
                self.uhv_ct3.set(row[8])
                self.uhv_st2.set(row[9])
                self.ds_ct1.set(row[10])
                self.ds_ct2.set(row[11])
                self.ds_st1.set(row[12])
                self.ds_ct3.set(row[13])
                self.ds_st2.set(row[14])
                self.dstl_ct1.set(row[15])
                self.dstl_ct2.set(row[16])
                self.dstl_st1.set(row[17])
                self.dstl_ct3.set(row[18])
                self.dstl_st2.set(row[19])
                self.maths_ct1.set(row[20])
                self.maths_ct2.set(row[21])
                self.maths_st1.set(row[22])
                self.maths_ct3.set(row[23])
                self.maths_st2.set(row[24])
                self.python_ct1.set(row[25])
                self.python_ct2.set(row[26])
                self.python_st1.set(row[27])
                self.python_ct3.set(row[28])
                self.python_st2.set(row[29])
        con.commit()
        con.close()

    def update_marks(self):
        if self.admission_no.cget('text') == '':
            messagebox.showerror('Error', 'Please select a student to update the marks !!')
        elif self.ct_marks_validation():
            messagebox.showerror('Out of Range', 'Class test marks should be less than or equal to 20 !!')
        elif self.st_marks_validation():
            messagebox.showerror('Out of Range', 'Sessional test marks should be less than or equal to 100 !!')
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='1234', database='Sign_Up')
            cur = con.cursor()
            cur.execute(f"""UPDATE Academics SET coa_ct1 = {self.coa_ct1.get()}, coa_ct2 = {self.coa_ct2.get()},
                        coa_st1 = {self.coa_st1.get()}, coa_ct3 = {self.coa_ct3.get()},
                        coa_st2 = {self.coa_st2.get()}, uhv_ct1 = {self.uhv_ct1.get()},
                        uhv_ct2 = {self.uhv_ct2.get()}, uhv_st1 = {self.uhv_st1.get()},
                        uhv_ct3 = {self.uhv_ct3.get()}, uhv_st2 = {self.uhv_st2.get()},
                        ds_ct1 = {self.ds_ct1.get()}, ds_ct2 = {self.ds_ct2.get()},
                        ds_st1 = {self.ds_st1.get()}, ds_ct3 = {self.ds_ct3.get()},
                        ds_st2 = {self.ds_st2.get()}, dstl_ct1 = {self.dstl_ct1.get()},
                        dstl_ct2 = {self.dstl_ct2.get()}, dstl_st1 = {self.dstl_st1.get()},
                        dstl_ct3 = {self.dstl_ct3.get()}, dstl_st2 = {self.dstl_st2.get()},
                        maths_ct1 = {self.maths_ct1.get()}, maths_ct2 = {self.maths_ct2.get()},
                        maths_st1 = {self.maths_st1.get()}, maths_ct3 = {self.maths_ct3.get()},
                        maths_st2 = {self.maths_st2.get()}, python_ct1 = {self.python_ct1.get()},
                        python_ct2 = {self.python_ct2.get()}, python_st1 = {self.python_st1.get()},
                        python_ct3 = {self.python_ct3.get()}, python_st2 = {self.python_st2.get()}
                        WHERE admission_no = '{self.admission_no.cget('text')}'""")
            con.commit()
            con.close()
            messagebox.showinfo('Success', f'Marks of student {self.name.cget("text")} has been updated successfully !!')

    def log_out(self):
        self.root.destroy()
        import SignIN


academics = Tk()
obj = StudentAcademics(academics)
academics.mainloop()
