from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import re
import MySQLdb
from tkinter import messagebox


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information")
        self.root.geometry("1265x645+0+0")
        self.root.wm_iconbitmap('abesit.ico')
        self.bg_icon = ImageTk.PhotoImage(file='bg_image.jpg')
        bg_label = Label(self.root, image=self.bg_icon)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Manage Frame
        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=25, y=25, width=430, height=595)

        m_title = Label(manage_frame, text="Student Information", bg="white", fg="dark blue",
                        font=("Times New Roman", 30, "bold"))
        m_title.place(x=39, y=10)

        admission_number = Label(manage_frame, text="Admission No.", bg='white', font=("times new roman", 15))
        admission_number.place(x=20, y=100)
        self.admission_number_entry = Entry(manage_frame, font=('', 10), bg='lightgrey')
        self.admission_number_entry.place(x=200, y=102, width=200)

        student_name = Label(manage_frame, text="Student's Name", bg="white", font=("times new roman", 15))
        student_name.place(x=20, y=142)
        self.student_name_entry = Entry(manage_frame, font=('', 10), bg='lightgrey')
        self.student_name_entry.place(x=200, y=144, width=200)

        gender = Label(manage_frame, text="Gender", bg="white", font=("times new roman", 15))
        gender.place(x=20, y=184)
        self.gender_check = StringVar()
        self.gender_male = Radiobutton(manage_frame, text='Male', bg='white', font=('', 10), value='Male',
                                       cursor='hand2', activebackground='white', activeforeground='red',
                                       variable=self.gender_check)
        self.gender_male.place(x=150, y=187)
        self.gender_female = Radiobutton(manage_frame, text='Female', bg='white', font=('', 10,), value='Female',
                                         cursor='hand2', activebackground='white', activeforeground='red',
                                         variable=self.gender_check)
        self.gender_female.place(x=300, y=187)

        father_name = Label(manage_frame, text="Father's Name", bg="white", font=("times new roman", 15))
        father_name.place(x=20, y=227)
        self.father_name_entry = Entry(manage_frame, font=('', 10), bg='lightgrey')
        self.father_name_entry.place(x=200, y=229, width=200)

        mother_name = Label(manage_frame, text="Mother's Name", bg="white", font=("times new roman", 15))
        mother_name.place(x=20, y=269)
        self.mother_name_entry = Entry(manage_frame, font=('', 10), bg='lightgrey')
        self.mother_name_entry.place(x=200, y=271, width=200)

        father_contact = Label(manage_frame, text="Father's Contact No.", bg="white", font=("times new roman", 15))
        father_contact.place(x=20, y=311)
        self.father_contact_entry = Entry(manage_frame, font=('', 10), bg='lightgrey')
        self.father_contact_entry.place(x=200, y=313, width=200)

        branch_opted = Label(manage_frame, text='Branch Opted', font=('Times New Roman', 15), bg='white')
        branch_opted.place(x=20, y=353)
        self.branch_opted_combo = ttk.Combobox(manage_frame, font=('', 9), state='readonly', justify=CENTER)
        self.branch_opted_combo['values'] = (
            '----SELECT----',
            'Computer Science and Engineering',
            'Information Technology',
            'Electronics and Communication Engineering',
            'Mechanical Engineering'
        )
        self.branch_opted_combo.place(x=200, y=353, width=200)
        self.branch_opted_combo.current(0)

        dob = Label(manage_frame, text="Date of Birth", bg='white', font=("times new roman", 15))
        dob.place(x=20, y=394)
        self.dob_day = ttk.Combobox(manage_frame, font=('', 10), state='readonly', justify=CENTER)
        self.dob_day['values'] = (
            'DAY', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
            24, 25, 26, 27, 28, 29, 30, 31)
        self.dob_day.place(x=200, y=396, width=50)
        self.dob_day.current(0)
        self.dob_month = ttk.Combobox(manage_frame, font=('', 10), state='readonly', justify=CENTER)
        self.dob_month['values'] = ('MONTH', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                    'September', 'October', 'November', 'December')
        self.dob_month.place(x=253, y=396, width=85)
        self.dob_month.current(0)
        self.dob_year = ttk.Combobox(manage_frame, font=('', 10), state='readonly', justify=CENTER)
        self.dob_year['values'] = ('YEAR', 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
                                   2003, 2004, 2005, 2006, 2007, 2008, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
                                   2018, 2019, 2020)
        self.dob_year.place(x=341, y=396, width=60)
        self.dob_year.current(0)

        address = Label(manage_frame, text=" Residential Address", bg='white', font=('Times New Roman', 15))
        address.place(x=15, y=436)

        self.address_entry = Text(manage_frame, font=('', 10), bg='lightgrey')
        self.address_entry.place(x=200, y=436, width=200, height=80)

        # Buttons
        add = Button(manage_frame, text="Add", cursor='hand2', bg='blue', fg='white', bd=2, font=('', 10),
                     command=self.add_students)
        add.place(x=20, y=550, width=80)

        update = Button(manage_frame, text="Update", cursor='hand2', bg='blue', fg='white', bd=2, font=('', 10),
                        command=self.update_data)
        update.place(x=120, y=550, width=80)

        delete = Button(manage_frame, text="Delete", cursor='hand2', bg='blue', fg='white', bd=2, font=('', 10),
                        command=self.delete_data)
        delete.place(x=220, y=550, width=80)

        clear = Button(manage_frame, text="Clear", cursor='hand2', bg='blue', fg='white', bd=2, font=('', 10),
                       command=self.clear)
        clear.place(x=320, y=550, width=80)

        # Detail Frame
        detail_frame = Frame(self.root, bg="white")
        detail_frame.place(x=480, y=25, width=760, height=595)

        search = Label(detail_frame, text="Search By", bg='white', font=("times new roman", 15))
        search.place(x=20, y=20)
        self.search_combo = ttk.Combobox(detail_frame, font=('Times New Roman', 13), state='readonly', justify=CENTER)
        self.search_combo['values'] = ('---SELECT---', 'Admission No.', 'Student\'s Name', 'E-mail ID')
        self.search_combo.place(x=110, y=20, width=150)
        self.search_combo.current(0)
        self.search_entry = Entry(detail_frame, font=('', 10), bg='lightgrey')
        self.search_entry.place(x=270, y=22, width=200)

        search = Button(detail_frame, text="Search", cursor='hand2', bg='blue', fg='white', bd=2, font=('', 10),
                        command=self.search_data)
        search.place(x=520, y=20, width=80)

        show_all = Button(detail_frame, text="Show All", cursor='hand2', bg='blue', fg='white', bd=2, font=('', 10),
                          command=self.fetch_data)
        show_all.place(x=620, y=20, width=80)

        # Table Frame
        table_frame = Frame(detail_frame, bd=4, relief='groove', bg="light blue")
        table_frame.place(x=20, y=70, width=720, height=510)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                          columns=(
                                              'Admission No.',
                                              'Student\'s Name',
                                              # 'Contact No.',
                                              'Gender',
                                              'Father\'s Name',
                                              'Mother\'s Name',
                                              'Father\'s Contact No.',
                                              'Branch',
                                              'Date of Birth',
                                              'Address',
                                              'E-mail ID'
                                          ),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('Admission No.', text='Admission No.')
        self.student_table.heading('Student\'s Name', text='Student\'s Name')
        # self.student_table.heading('Contact No.', text='Contact No.')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Father\'s Name', text='Father\'s Name')
        self.student_table.heading('Mother\'s Name', text='Mother\'s Name')
        self.student_table.heading('Father\'s Contact No.', text='Father\'s Contact No.')
        self.student_table.heading('Branch', text='Branch')
        self.student_table.heading('Date of Birth', text='Date of Birth')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('E-mail ID', text='E-mail ID')
        self.student_table['show'] = 'headings'
        self.student_table.column('Admission No.', width=150, anchor=CENTER)
        self.student_table.column('Student\'s Name', width=150, anchor=CENTER)
        # self.student_table.column('Contact No.', width=80, anchor=CENTER)
        self.student_table.column('Gender', width=80, anchor=CENTER)
        self.student_table.column('Father\'s Name', width=150, anchor=CENTER)
        self.student_table.column('Mother\'s Name', width=150, anchor=CENTER)
        self.student_table.column('Father\'s Contact No.', width=150, anchor=CENTER)
        self.student_table.column('Branch', width=250, anchor=CENTER)
        self.student_table.column('Date of Birth', width=150, anchor=CENTER)
        self.student_table.column('Address', width=500, anchor=CENTER)
        self.student_table.column('E-mail ID', width=200, anchor=CENTER)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_data)
        self.fetch_data()

    def admission_no_validation(self):
        if len(self.admission_number_entry.get()) != 9:
            return True

    def name_validation(self):
        if len(self.student_name_entry.get()) < 3:
            return True
        elif (
                re.search('[0-9]', self.student_name_entry.get()) or
                re.search('[!@#$%^&*"({})_|/,<>;:\']', self.student_name_entry.get())
        ):
            return True
        elif (
                re.search('[0-9]', self.father_name_entry.get()) or
                re.search('[!@#$%^&*"({})_|/,<>;:\']', self.father_name_entry.get())
        ):
            return True
        elif (
                re.search('[0-9]', self.mother_name_entry.get()) or
                re.search('[!@#$%^&*"({})_|/,<>;:\']', self.mother_name_entry.get())
        ):
            return True

    def contact_validation(self):
        if (
                len(self.father_contact_entry.get()) != 10 or
                re.search('[A-Z]', self.father_contact_entry.get()) or
                re.search('[a-z]', self.father_contact_entry.get()) or
                re.search('[!@#$%^&*"({})_|/,.<>;:\']', self.father_contact_entry.get())
        ):
            return True

    def add_students(self):
        d_o_b = self.dob_day.get() + ' ' + self.dob_month.get() + ' ' + self.dob_year.get()
        if self.admission_number_entry.get() == '':
            messagebox.showerror("Required Field", "Admission Number is required !!")
        elif self.admission_no_validation():
            messagebox.showerror('Error', 'Admission No. should be of format <AdmissionYear><Branch><S.No.>\n'
                                 + 'e.g., 2019CS148')
        elif self.student_name_entry.get() == '':
            messagebox.showerror('Required Field', "Student's Name is required !!")
        elif self.gender_check.get() == '':
            messagebox.showerror('Required Field', 'Please select the gender', parent=self.root)
        elif self.father_name_entry.get() == '':
            messagebox.showerror('Required Field', "Father's Name is required !!")
        elif self.mother_name_entry.get() == '':
            messagebox.showerror('Required Field', "Mother's Name is required !!")
        elif self.name_validation():
            messagebox.showerror('Error', "Please enter a valid name !!")
        elif self.father_contact_entry.get() == '':
            messagebox.showerror('Required Field', "Father's contact number is required !!")
        elif self.contact_validation():
            messagebox.showerror('Error', 'Please enter a valid contact number !!')
        elif self.branch_opted_combo.get() == '----SELECT----':
            messagebox.showerror('Required Field', 'Please select the branch !!')
        elif self.dob_day.get() == 'DAY':
            messagebox.showerror('Required Field', 'Please select the birth date !!')
        elif self.dob_month.get() == 'MONTH':
            messagebox.showerror('Required Field', 'Please select the birth month !!')
        elif self.dob_year.get() == 'YEAR':
            messagebox.showerror('Required Field', 'Please select the birth year !!')
        elif self.address_entry.get(1.0) == '':
            messagebox.showerror('Required Field', 'Please provide a reachable address !!')
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
            cur = con.cursor()
            cur.execute("SELECT * FROM Student WHERE `Admission No.` = '"+str(self.admission_number_entry.get())+"';")
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror('Already added', 'Information corresponding to this admission no. is already added !!')
            else:
                con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO Student (`Admission No.`, `Student's Name`, Gender, `Father's Name`, `Mother's Name`, `Father's Contact No.`, Branch, `Date of Birth`, `Residential Address`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (
                        self.admission_number_entry.get(),
                        self.student_name_entry.get(),
                        self.gender_check.get(),
                        self.father_name_entry.get(),
                        self.mother_name_entry.get(),
                        self.father_contact_entry.get(),
                        self.branch_opted_combo.get(),
                        str(d_o_b),
                        self.address_entry.get(1.0, END)
                    ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo('Success', 'Record has been added successfully !!')

    def fetch_data(self):
        con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
        cur = con.cursor()
        cur.execute("SELECT * FROM Student;")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.admission_number_entry.delete(0, END)
        self.student_name_entry.delete(0, END)
        self.gender_check.set('')
        self.father_name_entry.delete(0, END)
        self.mother_name_entry.delete(0, END)
        self.father_contact_entry.delete(0, END)
        self.branch_opted_combo.current(0)
        self.dob_day.current(0)
        self.dob_month.current(0)
        self.dob_year.current(0)
        self.address_entry.delete(1.0, END)

    def get_data(self, event):
        row_data = self.student_table.selection()
        for i in row_data:
            self.admission_number_entry.insert(0, self.student_table.item(i, 'values')[0])
            self.student_name_entry.insert(1, self.student_table.item(i, 'values')[1])
            self.gender_check.set(self.student_table.item(i, 'values')[2])
            self.father_name_entry.insert(3, self.student_table.item(i, 'values')[3])
            self.mother_name_entry.insert(4, self.student_table.item(i, 'values')[4])
            self.father_contact_entry.insert(5, self.student_table.item(i, 'values')[5])
            self.branch_opted_combo.set(self.student_table.item(i, 'values')[6])
            self.address_entry.insert(8.0, self.student_table.item(i, 'values')[8])
            date_of_birth = self.student_table.item(i, 'values')[7]
            dob = list(date_of_birth.split(' '))
            self.dob_day.set(dob[0])
            self.dob_month.set(dob[1])
            self.dob_year.set(dob[2])

    def update_data(self):
        d_o_b = self.dob_day.get() + ' ' + self.dob_month.get() + ' ' + self.dob_year.get()
        con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
        cur = con.cursor()
        cur.execute(
            "UPDATE Student SET `Student's Name` = %s, Gender = %s, `Father's Name` = %s, `Mother's Name` = %s, `Father's Contact No.` = %s, Branch = %s, `Date of Birth` = %s, `Residential Address` = %s WHERE `Admission No.` = %s;",
            (
                self.student_name_entry.get(),
                self.gender_check.get(),
                self.father_name_entry.get(),
                self.mother_name_entry.get(),
                self.father_contact_entry.get(),
                self.branch_opted_combo.get(),
                str(d_o_b),
                self.address_entry.get(1.0, END),
                self.admission_number_entry.get()
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo('Success', 'Record has been updated successfully !!')

    def delete_data(self):
        if self.admission_number_entry.get() == '':
            messagebox.showerror('Empty Field', 'Data can\'t be deleted since admission number is not provided!!')
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
            cur = con.cursor()
            sql_query = "DELETE FROM Student WHERE `Admission No.` = '%s';"
            args = (self.admission_number_entry.get())
            cur.execute(sql_query % args)
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()

    def search_data(self):
        if self.search_combo.get() == '---SELECT---':
            messagebox.showerror('Error', 'Please select the search by constraint !!', parent=self.root)
        elif self.search_combo.get() == 'Admission No.' and self.search_entry.get() == '':
            messagebox.showerror('Required Field', 'Please enter the Admission No. !!', parent=self.root)
        elif self.search_combo.get() == "Student's Name" and self.search_entry.get() == '':
            messagebox.showerror('Required Field', 'Please enter the Student\'s Name !!', parent=self.root)
        elif self.search_combo.get() == 'E-mail ID' and self.search_entry.get() == '':
            messagebox.showerror('Required Field', 'Please enter the E-mail ID !!', parent=self.root)
        else:
            con = MySQLdb.connect(host='localhost', user='root', password='', database='Sign_Up')
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM Student WHERE `" + self.search_combo.get() + "` = '" + self.search_entry.get() + "';")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('', END, values=row)
                con.commit()
            else:
                messagebox.showerror('Error', 'No record found !!')
            con.close()


student = Tk()
obj = StudentManagementSystem(student)
student.mainloop()
