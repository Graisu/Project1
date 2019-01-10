from tkinter import *
import cx_Oracle
import datetime import *
root = Tk()
con=cx_Oracle.connect("System/system123")
	cur=con.Cursor()
def c_create():
	
	cur.Execute(""" Create table reminder (msg varchar2(20),date date ,time time)""")
        value1 = (num1.get())
        value2 = (num2.get())
	value3=(num3.get())
	cur.Execute(' insert into reminder values(:1,:2,:3)',(value1,value2,value3))
    var = StringVar()
	a = Message( root, textvariable=var, relief=RAISED )
	var.set("Successfully created and inserted")
	a.pack()
    return
	
def c_view():
	
	cur.Execute(""" select  * from reminder""")
	print(cur.fetchall())
    return
 
 def c_update():
	
	cur.Execute(" update reminder set msg=:1,date=:2,time=:3 where date=:2",(value1,value2,value3))
	print(cur.fetchall())
    return

root.geometry('500x500')
root.title('Reminder') 
 
num1 = StringVar()
num2 = StringVar()
num3=StringVar()
labelTitle = Label(root, text="Enter the reminder")
labelTitle.place(x=125,y=50) 
labelNum1 = Label(root, text="Enter the date")
labelNum1.place(x=50,y=100)
labelNum2 = Label(root, text="Enter the  time") 
labelNum2.place(x=50,y=150)
entryNum1 = Entry(root, textvariable=num1)
entryNum1.place(x=200,y=100)
entryNum2 = Entry(root, textvariable=num2)
entryNum2.place(x=200,y=150)
entryNum2 = Entry(root, textvariable=num3)
entryNum2.place(x=200,y=150)
label_result= Label(root)
label_result.place(x=200,y=250)
buttonCal = Button(root, text="Create", command=c_create)
buttonCal.place(x=100,y=200)
buttonCal = Button(root, text="View", command=c_view)
buttonCal.place(x=200,y=300)
buttonCal = Button(root, text="Update", command=c_update)
buttonCal.place(x=300,y=400)
root.mainloop()