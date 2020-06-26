from tkinter import *
import csv
from tkinter import messagebox
def accept():                         #accept for login
   parent = Tk()
   global uid,pasw
   
   v=StringVar()
   w=StringVar()  
   name = Label(parent,text = "User ID").grid(row = 0, column = 0)      #user id=admin
   e1 = Entry(parent,textvariable=v)
     
   password = Label(parent,text = "Password").grid(row = 1, column = 0)  #password=Admin@123
   e2 = Entry(parent,textvariable=w)
   e1.grid(row = 0, column = 1)
   e2.grid(row = 1, column = 1)  
   submit = Button(parent, text = "Submit",comman=parent.destroy).grid(row = 4, column = 0)  
   parent.mainloop()
   uid=str(v.get())
   pasw=str(w.get())
   

def check():                              #check whether user id and pasword are correct or not for further functioning of program
    print(uid)
    print(pasw)
    if((uid=='admin') and (pasw=='Admin@123')):
       return 1                                   #if match return 1
       parent=Tk()
       parent.geometry("0x0")
       messagebox.showinfo("Login", "Login Successful !!")
       parent.destroy      
       
    else:
       parent=Tk()
       parent.geometry("0x0")
       messagebox.showinfo("Invalid", "User-ID password not matching !!")    #not match show error message
       parent.destroy

def findData():                                 #this is for accepting user id from samplesubmission and shows the amount
   global showAmount
   root=Tk()
   userVar=StringVar()
   Label(root,text="User-ID").grid(row=0,column=0)
   Entry(root,textvariable=userVar).grid(row=0,column=1)
   Button(root, text = "Submit",comman=root.destroy).grid(row=2,column=0)
   root.mainloop()
   
   uidFromCsv=int(userVar.get())
   #print("uidFromCsv: ",uidFromCsv) 
   
   with open('tanishq.csv') as f:
            data = [row for row in csv.reader(f)]
            showAmount=((data[(uidFromCsv % 23000)+1][1]))
   print("amount:",showAmount)
   parent=Tk()
   Label(parent,text="Amount:"+showAmount).pack(anchor=W)
   Button(parent, text = "exit",comman=parent.destroy).pack(anchor=NE)
   parent.mainloop()
       
accept()
i=check()
if i==1:
  findData()