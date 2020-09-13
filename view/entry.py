import tkinter as tk
import pickle
import numpy as np


Height=700
Width = 800
root = tk.Toplevel()
root.title("Bank Management System")


def output_window(value):
    
    root1 = tk.Toplevel()
    string=""
    if value==0:
        string="The person is unlikely to be our depositor"
    elif value==1:
        string="The person is a potential depositor"
    else:
        string=value
    canvas1 = tk.Canvas(root1, height=Height, width=Width)
    canvas1.pack()
    framex = tk.Frame(root1, bg='#2E0854', bd=5)
    framex.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.4, anchor='n')

    labelx = tk.Label(framex,text=string, font=20,bd=4,bg="#FF8C00")
    labelx.place(relwidth=1, relheight=1)

    root1.mainloop()



def data_model_builder(listx):
    final_list=[]
    listx=listx.reshape(1,11)
    string="E:/Bracu/semester 8/CSE 470 Software Engineering/Final_project/model/"
    #saved_knn_model
    loaded_model1=pickle.load(open(string+'file_knn1.sav', 'rb'))
    final_list.append(loaded_model1.predict(listx)) 
    #saved model random forest
    loaded_model2=pickle.load(open(string+'file_rf1.sav', 'rb'))
    final_list.append(loaded_model2.predict(listx))
    #saved decision tree
    loaded_model3=pickle.load(open(string+'file_dt1.sav', 'rb'))
    final_list.append(loaded_model3.predict(listx))
    #saved naive bayes
    loaded_model4=pickle.load(open(string+'file_nb1.sav', 'rb'))
    final_list.append(loaded_model4.predict(listx))    
    #saved support vector machine
    loaded_model5=pickle.load(open(string+'file_svm1.sav', 'rb'))
    final_list.append(loaded_model5.predict(listx))
    #saved bagging
    loaded_model6=pickle.load(open(string+'file_bg1.sav', 'rb'))
    final_list.append(loaded_model6.predict(listx))
    #saved extra tree
    loaded_model7=pickle.load(open(string+'file_et1.sav', 'rb'))
    final_list.append(loaded_model7.predict(listx))
    #saved ada boost
    loaded_model8=pickle.load(open(string+'file_adb1.sav', 'rb'))
    final_list.append(loaded_model8.predict(listx))    
    #saved gradient boost
    loaded_model9=pickle.load(open(string+'file_gb1.sav', 'rb'))
    final_list.append(loaded_model9.predict(listx))
    
    return final_list
    
def model_checker(list1):
    finals=np.array(list1)
    listx=data_model_builder(finals)
    listx=np.array(listx)
    listx=listx.reshape(1,9)
    loaded_model=pickle.load(open('E:/Bracu/semester 8/CSE 470 Software Engineering/Final_project/model/file_final.sav', 'rb'))
    result = loaded_model.predict(listx)
    print(result)
    if result[0]==0:
        output_window(0)
    else:
        output_window(1)



def check_fields():

    
    list1=[]
    
    #entry1
    try:
        each= int(entry1.get())
        list1.append(each)
    except ValueError:
        output_window("You should have entered number only")
    
    #entry2

    each= entry2.get().lower().strip()
    if entry2.get().lower().strip()=='single':
        list1.append(int(0))
    else:
        list1.append(int(1))
    
    #entry3
    each=entry3.get().lower().strip()
    if each == "unknown" or each=="primary":
        list1.append(int(0))
    elif each =="seondary":
        list1.append(int(1))
    else:
        list1.append(int(2))

  
    #entry4
    each=entry4.get().lower().strip()
    if each=='yes':
        list1.append(int(0))
    else:
        list1.append(int(1))
    
    
    #entry5
    try:
        each= int(entry5.get())
        list1.append(each)
    except ValueError:
        output_window("You should have entered number only")   
        
        
    #entry6
    each=entry6.get().lower().strip()
    if each=='yes':
        list1.append(int(0))
    else:
        list1.append(int(1))        

    #entry7
    each=entry7.get().lower().strip()
    if each=='yes':
        list1.append(int(0))
    else:
        list1.append(int(1))        

    #entry8
    try:
        each= int(entry8.get())
        list1.append(each)
    except ValueError:
        output_window("You should have entered number only") 



    #entry9
    try:
        each= int(entry9.get())
        list1.append(each)
    except ValueError:
        output_window("You should have entered number only") 



    #entry10
    try:
        each= int(entry10.get())
        list1.append(each)
    except ValueError:
        output_window("You should have entered number only") 


    #entry11
    try:
        each= int(entry11.get())
        list1.append(each)
    except ValueError:
        output_window("You should have entered number only") 
    
    
    model_checker(list1)



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

entry1 = tk.Entry(frame1, font=40,bd=4,bg="#EED2EE")
entry1.place(relwidth=0.8, relheight=1, relx=0.52)


#marital status frame
frame2 = tk.Frame(root, bg='#2E0854', bd=5)
frame2.place(relx=0.5, rely=0.16, relwidth=0.75, relheight=0.05, anchor='n')

label2 = tk.Label(frame2,text="Marital Status", font=10,bd=4,bg="#FF8C00")
label2.place(relwidth=0.5, relheight=1,relx=0)

entry2 = tk.Entry(frame2, font=40,bd=4,bg="#EED2EE")
entry2.place(relwidth=0.8, relheight=1, relx=0.52)



#education frame
frame3 = tk.Frame(root, bg='#2E0854', bd=5)
frame3.place(relx=0.5, rely=0.22, relwidth=0.75, relheight=0.05, anchor='n')

label3 = tk.Label(frame3,text="Education", font=10,bd=4,bg="#FF8C00")
label3.place(relwidth=0.5, relheight=1,relx=0)

entry3 = tk.Entry(frame3, font=40,bd=4,bg="#EED2EE")
entry3.place(relwidth=0.8, relheight=1, relx=0.52)

#default credit frame
frame4 = tk.Frame(root, bg='#2E0854', bd=5)
frame4.place(relx=0.5, rely=0.29, relwidth=0.75, relheight=0.05, anchor='n')

label4 = tk.Label(frame4,text="Do you have any credit?", font=10,bd=4,bg="#FF8C00")
label4.place(relwidth=0.5, relheight=1,relx=0)

entry4 = tk.Entry(frame4, font=40,bd=4,bg="#EED2EE")
entry4.place(relwidth=0.8, relheight=1, relx=0.52)


#yearly balance frame
frame5 = tk.Frame(root, bg='#2E0854', bd=5)
frame5.place(relx=0.5, rely=0.36, relwidth=0.75, relheight=0.05, anchor='n')

label5 = tk.Label(frame5,text="What is the yearly balance?", font=10,bd=4,bg="#FF8C00")
label5.place(relwidth=0.5, relheight=1,relx=0)

entry5 = tk.Entry(frame5, font=40,bd=4,bg="#EED2EE")
entry5.place(relwidth=0.8, relheight=1, relx=0.52)



#any housing loan frame
frame6 = tk.Frame(root, bg='#2E0854', bd=5)
frame6.place(relx=0.5, rely=0.43, relwidth=0.75, relheight=0.05, anchor='n')

label6 = tk.Label(frame6,text="Any housing loans?", font=10,bd=4,bg="#FF8C00")
label6.place(relwidth=0.5, relheight=1,relx=0)

entry6 = tk.Entry(frame6, font=40,bd=4,bg="#EED2EE")
entry6.place(relwidth=0.8, relheight=1, relx=0.52)



#loan frame
frame7 = tk.Frame(root, bg='#2E0854', bd=5)
frame7.place(relx=0.5, rely=0.50, relwidth=0.75, relheight=0.05, anchor='n')

label7 = tk.Label(frame7,text="Any personal loan?", font=10,bd=4,bg="#FF8C00")
label7.place(relwidth=0.5, relheight=1,relx=0)

entry7 = tk.Entry(frame7, font=40,bd=4,bg="#EED2EE")
entry7.place(relwidth=0.8, relheight=1, relx=0.52)



#date(last contact)frame
frame8 = tk.Frame(root, bg='#2E0854', bd=5)
frame8.place(relx=0.5, rely=0.57, relwidth=0.75, relheight=0.05, anchor='n')

label8 = tk.Label(frame8,text="The day of last contact", font=10,bd=4,bg="#FF8C00")
label8.place(relwidth=0.5, relheight=1,relx=0)

entry8 = tk.Entry(frame8, font=40,bd=4,bg="#EED2EE")
entry8.place(relwidth=0.8, relheight=1, relx=0.52)


#campaign( number of contacts performed during this campaign and for this client) frame
frame9 = tk.Frame(root, bg='#2E0854', bd=5)
frame9.place(relx=0.5, rely=0.64, relwidth=0.75, relheight=0.05, anchor='n')

label9 = tk.Label(frame9,text="No. of Campaigns", font=10,bd=4,bg="#FF8C00")
label9.place(relwidth=0.5, relheight=1,relx=0)

entry9 = tk.Entry(frame9, font=40,bd=4,bg="#EED2EE")
entry9.place(relwidth=0.8, relheight=1, relx=0.52)


#pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
frame10 = tk.Frame(root, bg='#2E0854', bd=5)
frame10.place(relx=0.5, rely=0.71, relwidth=0.75, relheight=0.05, anchor='n')

label10 = tk.Label(frame10,text="Days passed?", font=10,bd=4,bg="#FF8C00")
label10.place(relwidth=0.5, relheight=1,relx=0)

entry10 = tk.Entry(frame10, font=40,bd=4,bg="#EED2EE")
entry10.place(relwidth=0.8, relheight=1, relx=0.52)


#previous: number of contacts performed before this campaign and for this client (numeric)
frame11 = tk.Frame(root, bg='#2E0854', bd=5)
frame11.place(relx=0.5, rely=0.78, relwidth=0.75, relheight=0.05, anchor='n')

label11 = tk.Label(frame11, text="Previous contracts?", font=10,bd=4,bg="#FF8C00")
label11.place(relwidth=0.5, relheight=1,relx=0)

entry11 = tk.Entry(frame11, font=40,bd=4,bg="#EED2EE")
entry11.place(relwidth=0.8, relheight=1, relx=0.52)


frame12 = tk.Frame(root, bg='#2E0854', bd=5)
frame12.place(relx=0.5, rely=0.89, relwidth=0.75, relheight=0.05, anchor='n')
button = tk.Button(frame12, text="Check", font=40, command=check_fields)
button.place(relheight=1, relwidth=0.3)

root.mainloop()

