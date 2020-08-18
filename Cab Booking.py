

from tkinter import *
from tkinter import Menu
import tkinter.messagebox
class demo:
    def __init__(self):
        
        root=Tk()
        root.configure(background='light green')
        root.title('project')
        x=Label(root,text="CAB BOOKING SYSTEM",fg="blue",bg="black",font="Verdana 50 bold")
        x.pack()
        menu=Menu(root)
        new_item=Menu(menu)
        new_item.add_command(label='NEW')
        new_item.add_command(label='UPDATE',command=self.update)
        menu.add_cascade(label='HOME',menu=new_item)
        root.config(menu=menu)
        new=Menu(menu)
        new.add_command(label='ABOUT US',command=self.about)
        menu.add_cascade(label='ABOUT',menu=new)
        root.config(menu=menu)
        new1=Menu(menu)
        new1.add_command(label='24*7 SUPPORT',command=self.support)
        new1.add_command(label='Web Support',command=self.web)
        menu.add_cascade(label='HELP',menu=new1)
        root.config(menu=menu)
        a=Label(root,text="_____________")
        a.pack()
        y=Label(root,text="FOR LOGIN",fg="blue",font="Verdana 20 bold")
        y.pack()
        lb1=Label(root,text="USER ID")
        lb1.pack()
        entry=Entry(root,width=20)
        entry.pack()
        entry.get()
        lb2=Label(root,text="PASSWORD")
        lb2.pack()
        entry1=Entry(root,width=10)
        entry1.insert(0,'enter ur password')
        entry1.config(show='*')
        entry1.pack()
        entry1.get()
        button=Button(root,text="login",command=self.processbutton)
        button.pack()
        c=Label(root,text="_____________")
        c.pack()
        lb3=Label(root,text="FOR CREATING NEW ACCOUNT",fg="blue",font="Verdana 20 bold")
        lb3.pack()
  
         #for sinup 
        frame = Frame(root) 
        frame.pack() 
        bottomframe = Frame(root) 
        bottomframe.pack( side = BOTTOM ) 
        redbutton = Button(frame, text = 'SINUP', fg ='blue',command=self.processButton) 
        redbutton.pack( side = LEFT)  
        root.mainloop()

#end of first-------------------------------------------------------------------------
        
    def processButton(self):
        print("Page open for creating new account")
        class yy:
            def __init__(self):
                root=Tk()
                m=Label(root,text="CREATING NEW ACCOUNT",fg="green")
                m.pack()
                frame1=Frame(root)
                frame1.pack()
                label=Label(frame1,text="NAME",fg='blue')
                name=Entry(frame1,width=20)

                label.grid(row=1,column=1)
                name.grid(row=1,column=2)

                frame2=Frame(root)
                frame2.pack()
                label1=Label(frame2,text="PHONE.NO:",fg='blue')
                phone=Entry(frame2,width=10)
                label1.grid(row=1,column=1)
                phone.grid(row=1,column=2)
        
                frame3=Frame(root)
                frame3.pack()
                label2=Label(frame3,text="E-MAIL",fg='blue')
                mail=Entry(frame3,width=25)
                label2.grid(row=1,column=1)
                mail.grid(row=1,column=2)

                frame4=Frame(root)
                frame4.pack()
                label3=Label(frame4,text="PASSWORD",fg='blue')
                password=Entry(frame4,width=10)
                password.config(show='*')
                label3.grid(row=1,column=1)
                password.grid(row=1,column=2)

                frame5=Frame(root)
                frame5.pack()
                create=Button(frame5,text="create",fg='red',bg='gray',command=self.crea)
                create.pack()
        #-----------------------------------------------------------
                buttonstop = Button(root, text='BACK', width=25, command=root.destroy) 
                buttonstop.pack()
            def crea(self):
                print("Account is created")
                root=Tk()
                root.configure(background="light green")
                message=Message(root,text="Your account is created .Please login ...",fg="blue")
                message.pack()
                cancle=Button(root,text="OK",command=root.destroy)
                cancle.pack()
        yy()
        
        #root.mainloop()

        #_____________________________________________________________________________________________________
    def processbutton(self):
        
        class xx:
            def __init__(self):
                
                print("creating booking")
        
                root=Tk()
                root.config(background='light green')
    
    # Create a welcome to distance time calculator label 
                headlabel = Label(root, text = 'Booking details', 
                            fg = 'black', bg = "red")
                headlabel.pack()
      
    # Create a Source: label
                frame=Frame(root)
                frame.pack()
                label1 = Label(frame, text = "Source:", 
                     fg = 'black', bg = 'blue')
                sourcename=Entry(frame,width=20)
                label1.grid(row=1,column=1)
                sourcename.grid(row=1,column=2)
  
    # Create a Destination: label
                frame1=Frame(root)
                frame1.pack()  
                label2 = Label(frame1, text = "Destination:", 
                   fg = 'black', bg = 'blue')
                destname=Entry(frame1,width=20)
                label2.grid(row=1,column=1)
                destname.grid(row=1,column=2)
 #creating button for booking
                frame2=Frame(root)
                frame2.pack()
                book=Button(frame2,text="BOOK",command=self.p)
                check=Button(frame2,text="CHECK PRICE")
                book.grid(row=1,column=1)
                check.grid(row=1,column=5)
#for cancle ride

                frame3=Frame(root)
                frame3.pack()
                cancle=Button(frame3,text="CANCLE",command=root.destroy)
                cancle.pack()
                root.mainloop()
            def p(sef):
                print("confirmed booking")
                root=Tk()
                root.configure(background="light green")
                message=Message(root,text="Your Booking is confirmed.We reach at your location soon",fg="blue")
                message.pack()
                cancle=Button(root,text="OK",command=root.destroy)
                cancle.pack()
        xx()
    def about(self):
        root=Tk()
        root.configure(background="light green")
        message=Message(root,text="This program is made on purpose to help to book easily cab to reach near by you faster."+
                        "Our idea and moto is to fullfil the customer need and provide them a faster drop")
        message.pack()
        cancle=Button(root,text="OK",command=root.destroy)
        cancle.pack()
    def support(self):
        root=Tk()
        root.configure(background="light green")
        message=Message(root,text="OUR TOLEFREE NUMBER ARE:\nTelephone no=12345-8765434,12345-98765\nPhone no=9988877665,9977886543")
                        
        message.pack()
        cancle=Button(root,text="OK",command=root.destroy)
        cancle.pack()
    def web(self):
        root=Tk()
        root.configure(background="light green")
        message=Message(root,text="If you have any problem you can mail us at:\nOur E-mail ID=kkkkttt@gmail.com")
                        
        message.pack()
        cancle=Button(root,text="OK",command=root.destroy)
        cancle.pack()
    def update(self):
        root=Tk()
        root.configure(background="light green")
        message=Message(root,text="checking for update........")
                        
        message.pack()
        cancle=Button(root,text="CANCLE",command=root.destroy)
        cancle.pack()

#demo()

demo()

        
