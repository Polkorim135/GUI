from tkinter import *

# Create window object 
app = Tk()

# Port
part_text = StringVar()
part_label = Label(app, text='Port', font=('bold', 11), pady=20,)
part_label.grid(row=0, column=0, sticky=N)
part_entry= Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)

# Baudrate
baudrate_text = StringVar()
baudrate_label = Label(app, text='Baudrate', font=('bold', 11), pady=25)
baudrate_label.grid(row=1, column=0, sticky=N)
baudrate_entry= Entry(app, textvariable=baudrate_text)
baudrate_entry.grid(row=1,column=1)

# DataBits
part_text = StringVar()
part_label = Label(app, text='Port', font=('bold', 11), pady=20,)
part_label.grid(row=0, column=0, sticky=N)
part_entry= Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Parity
part_text = StringVar()
part_label = Label(app, text='Port', font=('bold', 11), pady=20,)
part_label.grid(row=0, column=0, sticky=N)
part_entry= Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)


app.title('Zatial to je jedno')
app.geometry('1250x625')

# Start program 
app.mainloop()