import tkinter as tk

class Output:
    
    def output_window(self,value):
        Height=700
        Width = 800
        root = tk.Toplevel()
        string=""
        if value==0:
            string="The person is unlikely to be our depositor"
        elif value==1:
            string="The person is a potential depositor"
        else:
            string=value
        canvas1 = tk.Canvas(root, height=Height, width=Width)
        canvas1.pack()
        framex = tk.Frame(root, bg='#2E0854', bd=5)
        framex.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.4, anchor='n')
    
        labelx = tk.Label(framex,text=string, font=20,bd=4,bg="#FF8C00")
        labelx.place(relwidth=1, relheight=1)
    
        root.mainloop()

