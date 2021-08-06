from os import close
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

#------------------------------db_delete1------------------------

def db_delete1():
    f1.grid_forget()
    f3.grid(row=0,column=0)

#------------------------------db_delete------------------------

def db_delete():
    err_msg = ''
    try:    
        db = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'py_database')
        cursor = db.cursor()
        query = "delete from contact_info where Ph_Number =%s"%(ent_dlt.get())
        cursor.execute(query)
        db.commit()
        messagebox.showinfo("Sucess", "Record Deleted!")
        db.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            err_msg = "Access Denied!"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            err_msg = "Database Not Found!"
        else:
            err_msg = err
        if err_msg != '':
            messagebox.showerror("Error", err_msg)
        
#------------------------------db_insert------------------------
    
def db_insert():

    #----------------------------------Authentication   -------------------------------
    g = ""
    i = ""
    error = ''
    if ent_name.get() == "":
        error += "\nName cannot be Blank!"
    if ent_contact.get() == '' or ent_contact.get().isdigit() == False:
        error += "\nContact Number Needed"
    if ch1.get() == 0 and ch2.get() == 0 and ch3.get() == 0 and ch4.get() == 0:
        error += "\nNerd Select any one "

    if error == '':
        if var.get() == 1:
            g = "Male"
        elif var.get() == 2:
            g = "Female"
        elif var.get() == 3:
            g = "Other"
        else:
            g = "Not Mentioned"

        if ch1.get() == 1:
            i = "Python"
            i1.deselect()
        if ch2.get() == 1:
            i = i + ', ' + "Java"
            i2.deselect()
        if ch3.get() == 1:
            i = i + ', ' + "C"
            i3.deselect()
        if ch4.get() == 1:
            i = i + ', ' + "Web"
            i4.deselect()
        name_db = ent_name.get()
        contact_db = ent_contact.get()
    
    elif error != '':
        messagebox.showerror("Blank Index", error)


    #----------------------------------Database queries-------------------------------
    try:
        db = mysql.connector.connect(user = 'root' , password = '', host = '127.0.0.1', database = "py_database")
        cursor = db.cursor()
        query = "insert into contact_info(Name, Ph_number, Gender, Interest) values (%s,%s,%s,%s)"
        values= (name_db, contact_db, g, i)
        cursor.execute(query,values)
        db.commit()
        messagebox.showinfo("Sucess!" , "Data Saved")

    except mysql.connector.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access Denied! wrong credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            messagebox.showerror("404 Error", "Database Not Found")
        else:
            messagebox.showerror("Error", err)
    else:
            db.close()

#------------------------------db_show------------------------

def db_show():

    f1.grid_forget()
    f2.grid(row=0,column=0)
    err_msg1 = ''
    try:
        db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='py_database')
                                                            #host=Ip of server
    
        cursor = db.cursor()#reference to database
        query= "select * from contact_info"#SQL query written'''
        cursor.execute(query)#query to run
        res = cursor.fetchall()#get the result in res in form of list of tuples

        if cursor.rowcount<1:#0 means no records
            lbl_see1.config(text = "No record found")

        else:
            database1 = ''
            for record in res:#iterating over res
                database1 = database1 + "\nName:" + record[0] + "\tContact:" + str(record[1]) + "\tGender:" + record[2] + "\tIntrests:" + record[3]
            lbl_see1.config(text = database1)
            
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            err_msg1 = "Acess denied/wrong  user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            err_msg1 = "Database does not exists"
        else:
            err_msg1 = err
        if err_msg1 != '':
            messagebox.showerror("Error", err_msg1)
    else:
        db.close()

#------------------------------db_hide------------------------

def hide():
    f2.grid_forget()
    f1.grid(row = 0, column =0)

#------------------------------db_hide1------------------------

def hide1():
    f3.grid_forget()
    f1.grid(row = 0, column =0)

#---------------------------Frames---------------------

root = Tk()
root.title("Database Handle")
f1 = Frame(root)
f1.grid(row = 0, column = 0 )
f2 = Frame(root)
f3 = Frame(root)

#---------------------------Variable Decelaration---------------------

var = IntVar()
ch1 = IntVar()
ch2 = IntVar()
ch3 = IntVar()
ch4 = IntVar()

#---------------------------Elements of "f1"---------------------

lbl_name = Label(f1, text = "Name ")
ent_name = Entry(f1)

lbl_contact = Label(f1, text = "Contact ")
ent_contact = Entry(f1)

lbl_gender = Label(f1 , text = "Gender")
g1 = Radiobutton(f1 , text = "Male" , variable = var , value = 1)
g2 = Radiobutton(f1 , text = "Female" , variable = var , value = 2)
g3 = Radiobutton(f1 , text = "Other" , variable = var , value = 3)

lbl_intrest = Label(f1 , text = "Interests")
i1 = Checkbutton(f1 , text = "Python" , variable = ch1 , onvalue = 1 , offvalue = 0)
i2 = Checkbutton(f1 , text = "Java" , variable = ch2 , onvalue = 1 , offvalue = 0)
i3 = Checkbutton(f1 , text = "C" , variable = ch3 , onvalue = 1 , offvalue = 0)
i4 = Checkbutton(f1 , text = "Web" , variable = ch4 , onvalue = 1 , offvalue = 0)

b = Button(f1 , text = "Submit" , command = db_insert)
b_show = Button(f1, text = "Show Database", command = db_show)
b_dlt = Button(f1, text = "delete entry", command = db_delete1)

#---------------------------Elements of "f2"---------------------

lbl_see = Label(f2 , text = "Database:")
lbl_see1 = Label(f2)
b_hide = Button(f2, text = "Back" , command = hide)

#---------------------------Elements of "f3"---------------------

lbl_dlt = Label(f3, text = "Enter the Phone Number:")
ent_dlt = Entry(f3)
b_dlt1 = Button(f3, text = "Submit", command = db_delete )
b_hide1 = Button(f3, text = "Back" , command = hide1)

#---------------------------Grid of Frame "f1"---------------------

lbl_name.grid(row = 0, column = 0)
ent_name.grid(row = 0, column = 2)

lbl_contact.grid(row = 1, column = 0)
ent_contact.grid(row = 1, column = 2)

lbl_gender.grid(row = 2 , column = 0)
g1.grid(row = 2, column = 1)
g2.grid(row = 2, column = 2)
g3.grid(row = 2, column = 3)

lbl_intrest.grid(row = 3, column = 0)
i1.grid(row = 3, column = 1)
i2.grid(row = 3, column = 2)
i3.grid(row = 3, column = 3)
i4.grid(row = 3, column = 4)

b.grid(row = 4, column = 2)
b_show.grid(row = 5, column = 2)
b_dlt.grid(row = 6, column = 2)

#---------------------------Grid of Frame "f2"---------------------

lbl_see1.grid(row = 1, column = 1, columnspan = 4 )
b_hide.grid(row = 2 , column = 0, columnspan = 4 )

#---------------------------Grid of Frame "f3"---------------------

lbl_dlt.grid(row = 1, column = 2)
ent_dlt.grid(row = 2, column = 2, columnspan = 4)
b_dlt1.grid(row = 3, column =2)
b_hide1.grid(row = 4, column = 2)

#--------------------------------end!-----------------------------

root.mainloop()
