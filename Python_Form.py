import tkinter 
from tkinter import ttk
from tkinter import messagebox

def enter_data():
     accepted=accept_var.get()
     if accepted=="accepted":

        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title=title_combobox.get()
            age=age_spinbox.get()
            nationality=nationality_combobox.get()
            numcourses=numcourses_spinbox.get()
            numsemesters=numsemesters_spinbox.get()
            registration_status=reg_status_var.get()
        

            print("first name:",firstname,"lastname:",lastname)
            print("Title:",title,"Age:",age,"Nationality:",nationality)
            print("registration status:",registration_status)
            print("#courses:",numcourses,"#Semesters",numsemesters)
            print("------------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error",message="please insert Firstname and lastname")

     else:
       tkinter.messagebox.showwarning(title="Error",message="Please accept with agreement")

window=tkinter.Tk()
window.title("Data Entry Form")

frame =tkinter.Frame(window)
frame.pack()

#saving User Info
user_info_frame=tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0 ,column=0,padx=20,pady=10)

first_name_lable=tkinter.Label(user_info_frame ,text="First Name")
first_name_lable.grid(row=0,column=0)

last_name_lable=tkinter.Label(user_info_frame,text="Last Name")
last_name_lable.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)

first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)


title_lable=tkinter.Label(user_info_frame,text="Title")
title_combobox= ttk.Combobox(user_info_frame,values=["","Mr.","Ms.","Dr."])
title_lable.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_lable=tkinter.Label(user_info_frame,text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame)
age_lable.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_lable = tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox= ttk.Combobox(user_info_frame,values=["Africa","Asia","Europe"])
nationality_lable.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

courses_frame=tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_lable=tkinter.Label(courses_frame,text="Registration Status")
reg_status_var=tkinter.StringVar(value="Not Registered")
registered_check=tkinter.Checkbutton(courses_frame,text="currently Registered",variable=reg_status_var,
onvalue="Registered" ,offvalue="Not Registered")

registered_lable.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_lable=tkinter.Label(courses_frame,text="# Completed Cources")
numcourses_spinbox=tkinter.Spinbox(courses_frame,from_=0,to='infinity')
numcourses_lable.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_lable=tkinter.Label(courses_frame,text="# Semesters")
numsemesters_spinbox=tkinter.Spinbox(courses_frame,from_=0,to='infinity')
numsemesters_lable.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

terms_frame=tkinter.LabelFrame(frame,text="Terms & Condition")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)    

accept_var=tkinter.StringVar(value="Not accepted")
terms_check=tkinter.Checkbutton(terms_frame,text="I accept the terms and condition.",
variable=accept_var,onvalue="accepted",offvalue="not accepted")
terms_check.grid(row=0,column=0)

#Button
button=tkinter.Button(frame,text="Enter data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)

window.mainloop()
