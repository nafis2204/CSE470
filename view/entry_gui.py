import tkinter as tk
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))
from control.input_output_handler import Input_output_handler
from view.output import Output



class Entry_gui:
    
    def __init__(self):
        self.handler = Input_output_handler()
        self.output_handler=Output()
        
    def receive_input(self):
        

        list1=[]
        list1.append(self.entry1.get())
        list1.append(self.entry2.get())
        list1.append(self.entry3.get())
        list1.append(self.entry4.get())
        list1.append(self.entry5.get())
        list1.append(self.entry6.get())
        list1.append(self.entry7.get())
        list1.append(self.entry8.get())
        list1.append(self.entry9.get())
        list1.append(self.entry10.get())
        list1.append(self.entry10.get())
        
        
        output=self.handler.input_handler(list1)
        self.output_handler.output_window(output)
        
        
        
    
        
  
    def gui(self,root):

        canvas = tk.Canvas(root, height=Height, width=Width)
        canvas.pack()
        
        background_image = tk.PhotoImage(file='rsz_helping-hand.png')
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)
        
        #age frame
        frame1 = tk.Frame(root, bg='#2E0854', bd=5)
        frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor='n')
        
        label1 = tk.Label(frame1,text="Age", font=10,bd=4,bg="#FF8C00")
        label1.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry1 = tk.Entry(frame1, font=40,bd=4,bg="#EED2EE")
        self.entry1.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        #marital status frame
        frame2 = tk.Frame(root, bg='#2E0854', bd=5)
        frame2.place(relx=0.5, rely=0.16, relwidth=0.75, relheight=0.05, anchor='n')
        
        label2 = tk.Label(frame2,text="Marital Status", font=10,bd=4,bg="#FF8C00")
        label2.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry2 = tk.Entry(frame2, font=40,bd=4,bg="#EED2EE")
        self.entry2.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        
        #education frame
        frame3 = tk.Frame(root, bg='#2E0854', bd=5)
        frame3.place(relx=0.5, rely=0.22, relwidth=0.75, relheight=0.05, anchor='n')
        
        label3 = tk.Label(frame3,text="Education", font=10,bd=4,bg="#FF8C00")
        label3.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry3 = tk.Entry(frame3, font=40,bd=4,bg="#EED2EE")
        self.entry3.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        #default credit frame
        frame4 = tk.Frame(root, bg='#2E0854', bd=5)
        frame4.place(relx=0.5, rely=0.29, relwidth=0.75, relheight=0.05, anchor='n')
        
        label4 = tk.Label(frame4,text="Do you have any credit?", font=10,bd=4,bg="#FF8C00")
        label4.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry4 = tk.Entry(frame4, font=40,bd=4,bg="#EED2EE")
        self.entry4.place(relwidth=0.8, relheight=1, relx=0.52)

        
        
        #yearly balance frame
        frame5 = tk.Frame(root, bg='#2E0854', bd=5)
        frame5.place(relx=0.5, rely=0.36, relwidth=0.75, relheight=0.05, anchor='n')
        
        label5 = tk.Label(frame5,text="What is the yearly balance?", font=10,bd=4,bg="#FF8C00")
        label5.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry5 = tk.Entry(frame5, font=40,bd=4,bg="#EED2EE")
        self.entry5.place(relwidth=0.8, relheight=1, relx=0.52)

        
        
        #any housing loan frame
        frame6 = tk.Frame(root, bg='#2E0854', bd=5)
        frame6.place(relx=0.5, rely=0.43, relwidth=0.75, relheight=0.05, anchor='n')
        
        label6 = tk.Label(frame6,text="Any housing loans?", font=10,bd=4,bg="#FF8C00")
        label6.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry6 = tk.Entry(frame6, font=40,bd=4,bg="#EED2EE")
        self.entry6.place(relwidth=0.8, relheight=1, relx=0.52)

        
        
        
        #loan frame
        frame7 = tk.Frame(root, bg='#2E0854', bd=5)
        frame7.place(relx=0.5, rely=0.50, relwidth=0.75, relheight=0.05, anchor='n')
        
        label7 = tk.Label(frame7,text="Any personal loan?", font=10,bd=4,bg="#FF8C00")
        label7.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry7 = tk.Entry(frame7, font=40,bd=4,bg="#EED2EE")
        self.entry7.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        #date(last contact)frame
        frame8 = tk.Frame(root, bg='#2E0854', bd=5)
        frame8.place(relx=0.5, rely=0.57, relwidth=0.75, relheight=0.05, anchor='n')
        
        label8 = tk.Label(frame8,text="The day of last contact", font=10,bd=4,bg="#FF8C00")
        label8.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry8 = tk.Entry(frame8, font=40,bd=4,bg="#EED2EE")
        self.entry8.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        #campaign( number of contacts performed during this campaign and for this client) frame
        frame9 = tk.Frame(root, bg='#2E0854', bd=5)
        frame9.place(relx=0.5, rely=0.64, relwidth=0.75, relheight=0.05, anchor='n')
        
        label9 = tk.Label(frame9,text="No. of Campaigns", font=10,bd=4,bg="#FF8C00")
        label9.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry9 = tk.Entry(frame9, font=40,bd=4,bg="#EED2EE")
        self.entry9.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        
        #pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
        frame10 = tk.Frame(root, bg='#2E0854', bd=5)
        frame10.place(relx=0.5, rely=0.71, relwidth=0.75, relheight=0.05, anchor='n')
        
        label10 = tk.Label(frame10,text="Days passed?", font=10,bd=4,bg="#FF8C00")
        label10.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry10 = tk.Entry(frame10, font=40,bd=4,bg="#EED2EE")
        self.entry10.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        #previous: number of contacts performed before this campaign and for this client (numeric)
        frame11 = tk.Frame(root, bg='#2E0854', bd=5)
        frame11.place(relx=0.5, rely=0.78, relwidth=0.75, relheight=0.05, anchor='n')
        
        label11 = tk.Label(frame11, text="Previous contracts?", font=10,bd=4,bg="#FF8C00")
        label11.place(relwidth=0.5, relheight=1,relx=0)
        
        self.entry11 = tk.Entry(frame11, font=40,bd=4,bg="#EED2EE")
        self.entry11.place(relwidth=0.8, relheight=1, relx=0.52)
        
        
        
        
        
        
        
        frame12 = tk.Frame(root, bg='#2E0854', bd=5)
        frame12.place(relx=0.5, rely=0.89, relwidth=0.75, relheight=0.05, anchor='n')
        button = tk.Button(frame12, text="Check", font=40, command=self.receive_input)
        button.place(relheight=1, relwidth=0.3)
        
        root.mainloop()        
        
        


        
        
Height=700
Width = 800
root = tk.Toplevel()
root.title("Bank Management System")

application=Entry_gui()
application.gui(root)

