from ast import Str
from multiprocessing.synchronize import Lock
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor, color
from tkcalendar import *
import tkinter

from tkcalendar import Calendar



# Create window object 
app = Tk()

# Port
part_text = StringVar()
part_label = Label(app, text='Port', font=('bold', 11), pady=20,)
part_label.grid(row=0, column=0, sticky= W)
part_entry= Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=10)

def test_func():
    print("CLICk")


# Baudrate
course=["300","600","1200","2400","4800","9600","19200","36800"]
l1=Label(app, text="Baudrate", font=("bold", 11), pady=23)
l1.grid(row=0, column=25, sticky=W)
cmb=ttk.Combobox(app,value=course,width=15)
cmb.grid(row=0, column=30)
cmb.current(5)


# DataBits
databits_text = StringVar()
databits_label = Label(app, text='DataBits', font=('bold', 11), pady=20)
databits_label.grid(row=1, column=0, sticky=W)
databits_entry= Entry(app, textvariable=databits_text)
databits_entry.grid(row=1, column=10)

# Parity
parity_text = StringVar()
parity_label = Label(app, text='Parity', font=('bold', 11), pady=20)
parity_label.grid(row=1, column=25, sticky=W)
parity_entry= Entry(app, textvariable=parity_text)
parity_entry.grid(row=1,column=30)

# Logical name referencing cb
CheckVar1 = IntVar()
C1 = Checkbutton(app, text = "Logical Name Referencing", font=("bold", 11), pady=20, variable = CheckVar1, )
C1.grid(row=2, column=10)

# Client Address
ca_text = StringVar()
ca_label = Label(app, text='Client Address', font=('bold', 11), pady=20,)
ca_label.grid(row=3, column=0, sticky= W)
ca_entry= Entry(app, textvariable=ca_text)
ca_entry.grid(row=3,column=10)

# Server Address
sa_text = StringVar()
sa_label = Label(app, text='Server Address', font=('bold', 11), pady=20,)
sa_label.grid(row=3, column=25, sticky= W)
sa_entry= Entry(app, textvariable=sa_text)
sa_entry.grid(row=3,column=30)

# Auth Level
course=["None", "Low", "High", "Hihg_MD5", "High_SHA1"]
l1=Label(app, text="Auth", font=("bold", 11), pady=20)
l1.grid(row=4, column=0, sticky=W)
cmb=ttk.Combobox(app,value=course,width=15)
cmb.grid(row=4, column=10)
cmb.current(4)

# Password
password_text = StringVar()
password_label = Label(app, text='Password', font=('bold', 11), pady=20,)
password_label.grid(row=4, column=25, sticky= W)
password_entry= Entry(app, textvariable=password_text)
password_entry.grid(row=4,column=30)

# Interface Protocol
course=["HDLC", "HDLC_MODE_E", "WRAPPER"]
l1=Label(app, text="Interface Protocol", font=("bold", 11), pady=20)
l1.grid(row=5, column=0, sticky=W)
cmb=ttk.Combobox(app,value=course,width=15, postcommand=test_func)
cmb.grid(row=5, column=10)
cmb.current(1)

# Cache file
cf_text = StringVar()
cf_label = Label(app, text='Cache file', font=('bold', 11), pady=20)
cf_label.grid(row=7, column=0, sticky=W)
cf_entry= Entry(app, textvariable=cf_text)
cf_entry.grid(row=8, column=0)

# XSLX Output File
xslx_text= StringVar()
xslx_label= Label(app, text='XSLX Output File', font=('bold', 11), pady=20)
xslx_label.grid(row=7,column=15)
xslx_entry= Entry(app, textvariable=xslx_text)
xslx_entry.grid(row=8, column=15)

# Date From
cal_text = StringVar()
cal_label= Label(app, text='Date From', font=('bold', 11), pady=20)
cal_label.grid(row=0, column= 70, sticky=W)
cal=DateEntry(app,selectmode='d/m/yy')
cal.grid(row=0,column=71)

# Date To

cal_text = StringVar()
cal_label= Label(app, text='Date to', font=('bold', 11), pady=20)
cal_label.grid(row=0, column= 72, sticky=W)
cal=DateEntry(app,selectmode='d/m/yy', sticky=W)
cal.grid(row=0,column=73)

#trace

trace_text=  StringVar()
trace_label= Label(app,text='Trace', font=('bold', 11), pady=20)
trace_label.grid(row=4, column=70, sticky=W) 
trace_entry= Entry(state='readonly', background='white')
trace_entry.grid(row=4, column=71, columnspan=5, padx=45, pady=20, ipadx=200, ipady=140, )

app.title('Zatial to je jedno')
app.geometry('1650x625')

# Start program 
app.mainloop()