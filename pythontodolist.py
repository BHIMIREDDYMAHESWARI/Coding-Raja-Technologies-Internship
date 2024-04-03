# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 09:30:55 2024

@author: mahes
"""

#import the module
from tkinter import *
from tkinter import messagebox 
#create the function
def newTask():
    task=my_entry.get()
    if task != " ":
        lb.insert(END,task)
        my_entry.delete(0,'end')
    else:
        messagebox.showarning('warning','please enter some task.')
def deleteTask():
    lb.delete(ANCHOR)
#configure and create main window
ws =Tk()
ws.geometry('500x450+500+200')
ws.title('python guides')
ws.configure(bg="#223441")
ws.resizable(width=False,height=False)
#create widges
frame=Frame(ws)
frame.pack(pady=10)
lb=Listbox(frame,width=25,height=8,font=('Times,18'),bd=0,fg='#464646',highlightthickness=0,selectbackground="#a6a6a6",activestyle='none')
lb.pack(side=LEFT,fill=BOTH)
task_list=['wake up at 5am','brush your teeth','go to bath','have the breakfast','go to school','learn something']
for item in task_list:
    lb.insert(END,item)
sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
my_entry=Entry(ws,font=('times',24))
my_entry.pack(pady=20)
button_frame=Frame(ws)
button_frame.pack(pady=20)
addTask_btn=Button(button_frame,text='add Task',font=('times14'),bg='#c5f776',padx=20,pady=10,command=newTask)
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)
delTask_btn=Button(button_frame,text='Delete Task',font=('times 14'),bg="#ff8b61",padx=20,pady=10,command=deleteTask)
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)
ws.mainloop()
