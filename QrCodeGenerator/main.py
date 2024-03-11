from tkinter import *
from tkinter import messagebox

import qrcode 

def submit():
    url=input_url.get()
    file_name = input_name.get()
    create_qr(url,file_name)
    

def create_qr(url,name):
    obj = qrcode.make(url)
    obj.save(name+".png")
    end_msg()

def end_msg():
    end_lab = Label(frame,
                text="Qr created successfully, check your folder",font=('Roman',25),
                background='#82929e',foreground='white')
    end_lab.place(x=0,y=270)

wn = Tk()
wn.title("QR code Generator")
wn.resizable(False,False)
wn.geometry('600x600')

#wn.eval('tk::PlaceWindow . center')

frame = Frame(wn,height=600,width=600,background='#82929e')
frame.place(x=0,y=0)


top_lab=Label(frame,
          text="Hi,Enter the link below",font=('Roman',40),
          background='#82929e',foreground='white'
          )
top_lab.place(x=10,y=10)

input_url = Entry(frame,width=50)
input_url.place(x=10,y=90)


mid_lab = Label(frame,
                text="Enter filename below",font=('Roman',40),
                background='#82929e',foreground='white')
mid_lab.place(x=10,y=120)

input_name = Entry(frame,width=50)
input_name.place(x=10,y=180)

okbtn = Button(frame,text="Ok",command=submit,height=2,width=10)
okbtn.place(x=100,y=220)




wn.mainloop()