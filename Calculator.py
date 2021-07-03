from tkinter import *
import tkinter.messagebox as msg
root=Tk()
root.geometry("460x470") 
root.maxsize(460,470)   
root.title("Calculates Everything")
root.configure(background="red")

def click(event):
    global inpu
    text=event.widget.cget("text")
    print(text)
    if text =="=":
        if inpu.get().isdigit():
            value=int(inpu.get())

        else:
            try:
                value=eval(inpu.get())
            
            except Exception as e:
                value=""
                msg.showerror("ERROR",e)

        inpu.set(value)
    
    elif text == "C": 
        inpu.set("")
  

    else:
        inpu.set(inpu.get()+text)
        

inpu=StringVar()
inpu.set("")
inp=Entry(root,textvariable=inpu,fg="black",font=("Algerian  40 bold")).pack(fill=X,ipady=23)



l1=["7","8","9","*","4","5","6","-","1","2","3","+","C","0",".","=","7","8","9"]

for i in range(0,4):
    f=Frame(root,bg="pink")
    if i==0:
        for j in range(0,4):
            b=Button(f,text=l1[j],padx=34,pady=12,bg="#80dfff",fg="black",font=("Algerian  25 bold"))
            b.pack(side=LEFT)
            b.bind("<Button-1>",click)
            f.pack()
    elif i==1:
        for j in range(4,8):
            b=Button(f,text=l1[j],padx=34,pady=20,bg="#80dfff",fg="black",font=("Algerian  25 bold"))
            b.pack(side=LEFT)
            b.bind("<Button-1>",click)
            f.pack()
    elif i==2:
        for j in range(8,12):
            b=Button(f,text=l1[j],padx=33,pady=15,bg="#80dfff",fg="black",font=("Algerian  25 bold"))
            b.pack(side=LEFT)
            b.bind("<Button-1>",click)
            f.pack()

    elif i==3:
        for j in range(12,16):
            b=Button(f,text=l1[j],padx=34,pady=20,bg="#80dfff",fg="black",font=("Algerian  25 bold"))
            b.pack(side=LEFT)
            b.bind("<Button-1>",click)
            f.pack()

root.mainloop()