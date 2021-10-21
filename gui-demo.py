#!/usr/bin/env python3

# importing the required module(s)
from tkinter import *
import sqlite3

# Function that is called when Submit button is pressed.
def createRecord():
    #Get all values from the fields
    name1=Fullname.get()
    email=Email.get()

    #Input validation - without this - code below will create blank records
    if len(name1) > 0 and len(email) > 0:

        #Setup the connection (If the .db file is missing it will create one)
        conn = sqlite3.connect('Form.db')
        with conn:

            #Create a cursor attached to the current connection
            cursor=conn.cursor()

            #Create the db table if not already present
            cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender \
                            TEXT,country TEXT,Programming TEXT)')
            
            #Insert a student record 
            cursor.execute('INSERT INTO Student (FullName,Email) \
                            VALUES(?,?)',(name1,email,))

            #Commit the changes to the db
            conn.commit()

            # Inform the user of success
            label_messages["text"] = "Record created successfully"

            # Reset the form values.  
            # The Entry widgets don't have a dedicated set method, so we have to delete from the start (0) to the end
            entry_1.delete(0,"end")
            entry_2.delete(0,"end")
            entry_1.focus()

    else:
        # Inform the user of what the problem is
        if len(name1) == 0:
            label_messages["text"] = "Please enter your name."
        elif len(email) == 0:
            label_messages["text"] = "Please enter an email address."


#Initial window setup including its size.
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

# Variable setup for what we intend on capturing
Fullname=StringVar()
Email=StringVar()

#Add a heading label to the window
label_0 = Label(root, text="Registration Form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

#Add the fullname label and entry field.
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240,y=130)

# For usability, we use the .focus() method to place the cursor in the first field
entry_1.focus()

#Add the email label and entry field.
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=240,y=180)

#Add the Submit button
Button(root, text='Submit',width=20,bg='brown',fg='black',command=createRecord).place(x=180,y=380)

#Add a label used to send messages to the user
label_messages = Label(root, text="",width=20,font=("bold", 10))
label_messages.place(x=180,y=420)

# Display the window.
root.mainloop()

