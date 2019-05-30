#!/usr/bin/pyhton
import os
from tkinter import *
Dict={}
f=open("file_dat.txt",'r')

accno=0

for line in f:
        List=line.split('\t')   
        Dict[int(List[0])]=[List[1], List[2],float(List[3].rstrip('\n'))]
        accno=int(List[0])
print(Dict)
f.close()
#93e3e3
#b6ecec
#1cb6b6
#ADD8E6
#739ebf
background_color = "#93e3e3"
button_color = "#739ebf"
root=Tk()
root.title("Banking")
root.geometry("600x450+387+143")
app=Frame(root)
root.configure(background= background_color)
'''app.grid()'''
Label1=Label(root,text="Welcome to ACE Banking Services.")
Label1.place(relx=0.05, rely=0.044, height=41, width=524)
Label1.configure(background= background_color, font="-family {@Malgun Gothic} -size 18 -weight bold")
Label2=Label(root, text= "Click on the service you wish to avail.")
Label2.place(relx=0.25, rely=0.133, height=23, width=320)
Label2.configure(background= background_color,font="-family {@Malgun Gothic} -size 11 -weight bold")


class Create(Frame):
        def __init__(self,master):
                Frame.__init__(self,master)
                self.configure(background=background_color)
                self.grid()
                self.create_widgets()
        def create_widgets(self):
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=0,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.label=Label(self)
                self.label["text"]="Enter your full name"
                self.label.grid(row=0,column=1 ,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=2,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.name=Entry(self)
                self.name.grid(row=1,column=1,sticky=S, padx=50)
                self.label=Label(self)
                self.label["text"]="Enter your initial balance"
                self.label.grid(row=3,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.balance=Entry(self)
                self.balance.grid(row=4,column=1,sticky=S, padx=50)
                self.label=Label(self)
                self.label["text"]="Enter your desired 4-digit PIN"
                self.label.grid(row=5,column=1,sticky=S, padx=50,pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.pin=Entry(self, show="*")
                self.pin.grid(row=6,column=1,sticky=S, padx=50)
                self.button=Button(self)
                self.button["text"]="SUBMIT"
                self.button.configure(height=2, width=20,background=button_color, borderwidth =".5")
                self.button["command"]=self.collect_data
                self.button.grid(row=9,column=1,sticky=S, padx=50)
                self.msg=Text(self,width=30,height=5,wrap=WORD)
                self.msg.insert(0.0,"Enter amount greater than 5000")
                self.msg.grid(row=8,column=1,sticky=S, padx=50, pady=15)
                
        def collect_data(self):
                global accno
                global Dict
                while int(self.balance.get())<5000:
                        self.msg.delete(0.0,END)
                        self.msg.insert(0.0,"Please enter amount greater than 5000")
                        self.balance.delete(0,END)
                #List=[accounts[len(accounts)-1][0]+1,self.name.get(),int(self.balance.get())]

                pin=self.pin.get()
                if not pin.isdigit() or len(pin)>4:
                        self.msg.delete(0.0, END)
                        self.msg.insert(0.0, "Invalid PIN")
                self.msg.delete(0.0,END)
                self.msg.insert(0.0,"Your account number is: "+str(accno+1))
                
                accno+=1                
                Dict[accno]=[self.name.get(), int (self.pin.get()),int(self.balance.get())]
                print(Dict)
                self.balance.delete(0,END)
                self.name.delete(0,END)
                self.pin.delete(0,END)
                quit_fun()
                

class Balance(Frame):
        def __init__(self,master):
                Frame.__init__(self,master)
                self.configure(background=background_color)
                self.grid()
                self.create_widgets()
        def create_widgets(self):
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=0,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.label2=Label(self)
                self.label2["text"]="Enter your account number"
                self.label2.grid(row=0,column=1,sticky=S, padx=50, pady=20)
                self.label2.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=2,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.acc=Entry(self)
                self.acc.grid(row=1,column=1,sticky=S, padx=50)
                self.label=Label(self)
                self.label["text"]="Enter your PIN"
                self.label.grid(row=2,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.pin=Entry(self, show="*")
                self.pin.grid(row=3,column=1,sticky=S, padx=50)
                self.button=Button(self)
                self.button["text"]="SUBMIT"
                self.button.configure(height=2, width=20,background=button_color, borderwidth =".5")
                self.button["command"]=self.collect_data
                self.button.grid(row=7,column=1,sticky=S, padx=50, pady=10)
                self.msg=Text(self,width=30,height=5,wrap=WORD)
                self.msg.insert(0.0,"Enter a valid account number.")
                self.msg.grid(row=6,column=1,sticky=S, padx=50,pady=30)
        def collect_data(self):
                global Dict
                num=int(self.acc.get())
                pin=self.pin.get()
                if not num in Dict.keys():
                        self.msg.delete(0.0,END)
                        self.msg.insert(0.0,"Invalid account number!") 
                        self.acc.delete(0.0,END)
                        num=int(self.acc.get())
                elif int(self.pin.get())!= Dict[num][1]:
                        self.msg.delete(0.0, END)
                        self.msg.insert(0.0, "Invalid PIN")
                else:
                        self.msg.delete(0.0,END)
                        self.msg.insert(0.0,"Balance: "+str(Dict[num][2]))

class Deposit(Frame):
        def __init__(self,master):
                Frame.__init__(self,master)
                self.configure(background=background_color)
                self.grid()
                self.create_widgets()
        def create_widgets(self):
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=0,sticky=S, padx=60)
                self.label1.configure(background= background_color)
                self.label=Label(self)
                self.label["text"]="Enter your account number"
                self.label.grid(row=0,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=2,sticky=S, padx=60)
                self.label1.configure(background= background_color)
                self.acc=Entry(self)
                self.acc.grid(row=1,column=1,sticky=S, padx=50)
                self.label=Label(self)
                self.label["text"]="Enter the amount to be deposited."
                self.label.grid(row=3,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.amt=Entry(self)
                self.amt.grid(row=4,column=1,sticky=S, padx=50)

                self.label=Label(self)
                self.label["text"]="Enter your PIN"
                self.label.grid(row=6,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.pin=Entry(self, show="*")
                self.pin.grid(row=7,column=1,sticky=S, padx=50)
                
                self.button=Button(self)
                self.button["text"]="SUBMIT"
                self.button.configure(height=2, width=20,background=button_color, borderwidth =".5")
                self.button["command"]=self.collect_data
                self.button.grid(row=10,column=1,sticky=S, padx=50)
                self.msg=Text(self,width=30,height=5,wrap=WORD)
                self.msg.insert(0.0,"Final amount will be displayed here.")
                self.msg.grid(row=9,column=1,sticky=S, pady=15)
        def collect_data(self):
                global Dict
                num=int(self.acc.get())
                pin=self.pin.get()
                if not num in Dict.keys():
                        self.msg.delete(0.0,END)
                        self.msg.insert(0.0,"Invalid account number!") 
                        self.acc.delete(0.0,END)
                        num=int(self.acc.get())
                elif int(self.pin.get())!= Dict[num][1]:
                        self.msg.delete(0.0, END)
                        self.msg.insert(0.0, "Invalid PIN number")
                else:
                        add=self.amt.get()
                        Dict[num][2]=float(Dict[num][2])+float(add)
                        self.msg.delete(0.0,END)
                        self.msg.insert(0.0,"Balance: "+str(Dict[num][2])) 
                        quit_fun()

class Withdraw(Frame):
        def __init__(self,master):
                Frame.__init__(self,master)
                self.configure(background = background_color)
                self.grid()
                self.create_widgets()
        def create_widgets(self):
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=0,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.label=Label(self)
                self.label["text"]="Enter your account number"
                self.label.grid(row=0,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=2,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.acc=Entry(self)
                self.acc.grid(row=1,column=1,sticky=S, padx=50)
                self.label=Label(self)
                self.label["text"]="Enter the amount to be withdrawn."
                self.label.grid(row=3,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.amt=Entry(self)
                self.amt.grid(row=4,column=1,sticky=S, padx=50)

                self.label=Label(self)
                self.label["text"]="Enter your PIN"
                self.label.grid(row=6,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.pin=Entry(self, show="*")
                self.pin.grid(row=7,column=1,sticky=S, padx=50)
                
                self.button=Button(self)
                self.button["text"]="SUBMIT"
                self.button["command"]=self.collect_data
                self.button.configure(width=20, height=2,background=button_color, borderwidth =".5")
                self.button.grid(row=11,column=1,sticky=S, padx=50)
                self.msg=Text(self,width=30,height=5,wrap=WORD)
                self.msg.insert(0.0,"Final amount will be displayed here.")
                self.msg.grid(row=9,column=1,sticky=S, padx=50, pady=15)

        def collect_data(self):
                global Dict
                num=int(self.acc.get())
                if not num in Dict.keys():
                        self.msg.delete(0.0,END)
                        self.msg.insert(0.0,"Invalid account number!") 
                        self.acc.delete(0.0,END)
                        num=int(self.acc.get())
                add=float(self.amt.get())
                pin=self.pin.get()
                if int(self.pin.get())!= Dict[num][1]:
                        self.msg.delete(0.0, END)
                        self.msg.insert(0.0, "Invalid PIN number")
                else:
                        if add<=Dict[num][2]:
                                Dict[num][2]=Dict[num][2]-add
                                self.msg.delete(0.0,END)
                                self.msg.insert(0.0,"Balance: "+str(Dict[num][2])) 
                        else:
                                self.msg.delete(0.0,END)
                                self.msg.insert(0.0,"Amount insufficient!")

class Search(Frame):
        def __init__(self,master):
                Frame.__init__(self,master)
                self.configure(background = background_color)
                self.grid()
                self.create_widgets()
        def create_widgets(self):
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=0,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.label=Label(self)
                self.label["text"]="Enter name(full or partial)"
                self.label.grid(row=0,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=2,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.name=Entry(self)
                self.name.grid(row=1,column=1,sticky=S, padx=50)

                self.label=Label(self)
                self.label["text"]="Enter your PIN"
                self.label.grid(row=3,column=1,sticky=S, padx=50,pady=10)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.pin=Entry(self, show="*")
                self.pin.grid(row=4,column=1,sticky=S, padx=50, pady=10)
                self.button=Button(self)
                self.button["text"]="SUBMIT"
                self.button["command"]=self.collect_data
                self.button.configure(width=20, height=2,background=button_color, borderwidth =".5")
                self.button.grid(row=7,column=1,sticky=S, padx=50, pady=10)
                self.msg=Text(self,width=30,height=5,wrap=WORD)
                self.msg.insert(0.0," ")
                self.msg.grid(row=6,column=1,sticky=S, padx=50, pady=20)
        def collect_data(self):
                global Dict
                name=self.name.get()
                found=0
                for num in Dict.keys():
                        if Dict[num][0]!=self.name.get():
                                continue
                        elif Dict[num][0]==self.name.get() and Dict[num][1]==self.pin.get():
                                self.msg.delete(0.0,END)
                                self.msg.insert(0.0,"Name: "+Dict[num][0]+"\nAccount Number: "+str(num))
                                found=1
                                break

                if found==0:
                        self.msg.delete(0.0, END)
                        self.msg.insert(0.0, "Account not found")

class Close(Frame):
        def __init__(self,master):
                Frame.__init__(self,master)
                self.configure(background = background_color)
                self.grid()
                self.create_widgets()
        def create_widgets(self):
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=0,sticky=S, padx=50)
                self.label1.configure(background= background_color)
                self.label=Label(self)
                self.label["text"]="Enter your account number"
                self.label.grid(row=0,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.label1=Label(self)
                self.label1["text"]=""
                self.label1.grid(row=0,column=2,sticky=S, padx=50,pady=20)
                self.label1.configure(background= background_color)
                self.acc=Entry(self, width=20)
                self.acc.grid(row=1,column=1,sticky=S, padx=50)
                self.label=Label(self)
                self.label["text"]="Enter your PIN"
                self.label.grid(row=3,column=1,sticky=S, padx=50, pady=20)
                self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
                self.pin=Entry(self, show="*")
                self.pin.grid(row=4,column=1,sticky=S, padx=50, pady=10)
                self.button=Button(self)
                self.button["text"]="SUBMIT"
                self.button["command"]=self.collect_data
                self.button.configure(width=20, height=2,background=button_color, borderwidth =".5")
                self.button.grid(row=5,column=1,sticky=S, padx=50, pady=10)
                self.label1=Label(self)
                self.msg=Text(self,width=30,height=5,wrap=WORD)
                self.msg.insert(0.0,"")
                self.msg.grid(row=7,column=1,sticky=S, padx=50, pady=20)

        def collect_data(self):
                global Dict
                global accno
                num=int(self.acc.get())
                if not num in Dict.keys():
                        self.msg.delete(0.0,END)
                        self.msg.insert(0.0,"Invalid account number!") 
                        self.acc.delete(0.0,END)
                        num=int(self.acc.get())
                elif int(self.pin.get())!= Dict[num][1]:
                        self.msg.delete(0.0, END)
                        self.msg.insert(0.0, "Invalid PIN number")
                self.msg.insert(0.0,"Thank you for banking with us.\nAmount to be refunded: "+str(Dict[num][2])) 
                del Dict[num]
                print(Dict)

class Transactions(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.configure(background = background_color)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.label1=Label(self)
        self.label1["text"]=""
        self.label1.grid(row=0,column=0,sticky=S, padx=25)
        self.label1.configure(background= background_color)
        self.label=Label(self)
        self.label["text"]="Enter your account number"
        self.label.grid(row=0,column=1,sticky=S, padx=50, pady=10)
        self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
        self.label1=Label(self)
        self.label1["text"]=""
        self.label1.grid(row=0,column=2,sticky=S, padx=50,pady=10)
        self.label1.configure(background= background_color)
        self.acc=Entry(self, width=20)
        self.acc.grid(row=1,column=1,sticky=S, padx=50)

        self.label=Label(self)
        self.label["text"]="Enter receiver's account number"
        self.label.grid(row=3, column=1, sticky=S, padx=50, pady=10)
        self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
        self.acc2=Entry(self, width =20)
        self.acc2.grid(row=4,column=1, sticky=S, padx=150)
        
        self.label=Label(self)
        self.label["text"]="Enter the amount to transfer"
        self.label.grid(row=5, column=1, sticky=S, padx=50, pady=10)
        self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
        self.amt=Entry(self)
        self.amt.grid(row=6, column=1, sticky=S, padx=150)
        
        self.label=Label(self)
        self.label["text"]="Enter yout pin PIN"
        self.label.grid(row=7, column=1, sticky=S, padx=50, pady=10)
        self.label.configure(background= background_color,font="-family {Arabic Transparent} -size 10 -weight bold")
        self.pin=Entry(self, show="*")
        self.pin.grid(row=8, column=1, sticky=S, padx=50, pady=5)
                
        self.button=Button(self)
        self.button["text"]="Transfer"
        self.button["command"]=self.collect_data
        self.button.configure(width=20, height=2,background=button_color, borderwidth =".5")
        self.button.grid(row=9, column=1, sticky=S, padx=150, pady=2)
        self.msg=Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, "Final amount will be displayed here.")
        self.msg.grid(row=10, column=1,sticky=S, pady=15)
    def collect_data(self):
        global Dict
        num1=self.acc.get()
        num2=self.acc2.get()
        if (num1 not in Dict.keys() or num2 not in Dict.keys()):
            self.msg.delete(END)
            self.msg.insert(0.0, "Enter valid account numbers")
            self.acc.delete(END)
            num1=int(self.acc.get())
            num2=int(self.acc2.get())
        amount=float(self.amt.get())
        if amount>float(Dict[num1][1]):
            self.msg.delete(0.0, END)
            self.msg.insert(0.0, "Insufficient Balance")
        elif int(self.pin.get())!=Dict[num1][1]:
                self.msg.delete(0.0, END)
                self.msg.insert(0.0, "Invalid PIN")
        else:
                Dict[num1][2] = float(Dict[num1][2])-float(amount)
                Dict[num2][2] = float(Dict[num2][2])+float(amount)
                self.msg.delete(0.0, END)
                self.msg.insert(0.0, "Transaction successful. \nBalance: "+str(Dict[num1][2]))

                        
def win1():
        root=Tk()
        root.title("Create Account")
        root.geometry("550x400")
        Create(root)
        root.mainloop()
def win2():
        root=Tk()
        root.title("Balance Enquiry")
        root.geometry("550x370")
        app=Balance(root)
        root.mainloop()
def win3():
        root=Tk()
        root.title("Deposit Amount")
        root.geometry("550x400")
        app=Deposit(root)
        root.mainloop()
def win4():
        root=Tk()
        root.title("Withdraw  Amount")
        root.geometry("550x400")
        app=Withdraw(root)
        root.mainloop()
def win5():
        root=Tk()
        root.title("Search")
        root.geometry("550x350")
        app=Search(root)
        root.mainloop()
def win6():
        root=Tk()
        root.title("Close Account")
        root.geometry("550x350")
        app=Close(root)
        root.mainloop()
# def win7():
#         root=Tk()
#         root.title("Import Accounts")
#         root.geometry("550x400")
#         app=Import(root)
#         root.mainloop()

def win8():
        root=Tk()
        root.title("Make a transaction")
        root.geometry("550x400")
        app=Transactions(root)
        root.mainloop()

def quit_fun():
        global Dict
        fi=open("file_dat.txt",'w')
        #Dict=sorted(Dict)
        print(Dict)
        for num in Dict:
                List=[]
                List.append(str(num))
                List.append(Dict[num][0])
                List.append(str(Dict[num][1]))
                List.append(str(Dict[num][2]))
                string='\t'.join(List)+'\n'
                print(string)
                fi.write(string)        
        print('Successful')

Button1 =Button(root)
Button1.place(relx=0.133, rely=0.222, height=44, width=177)
Button1.configure(background=button_color)
Button1.configure(text='''Create Account''',borderwidth =".5")
Button1["command"]=win1

Button2 =Button(root)
Button2.place(relx=0.55, rely=0.222, height=44, width=177)
Button2.configure(background=button_color)
Button2.configure(text='''Balance Enquiry''',borderwidth =".5")
Button2["command"]=win2 

Button3 =Button(root)
Button3.place(relx=0.133, rely=0.378, height=44, width=177)
Button3.configure(background=button_color)
Button3.configure(text='''Deposit amount''', borderwidth =".5")
Button3["command"]=win3

Button4 =Button(root)
Button4.place(relx=0.55, rely=0.387, height=44, width=177)
Button4.configure(background=button_color)
Button4.configure(text='''Withdraw  Amount''', borderwidth =".5")
Button4["command"]=win4

Button5 =Button(root)
Button5.place(relx=0.133, rely=0.533, height=44, width=177)
Button5.configure(background=button_color)
Button5.configure(text='''Search by name''', borderwidth =".5")
Button5["command"]=win5

Button6 =Button(root)
Button6.place(relx=0.133, rely=0.689, height=44, width=177)
Button6.configure(background="#FF3232")
Button6.configure(text='''Delete Account''', borderwidth =".5")
Button6["command"]=win6

Button7 =Button(root)
Button7.place(relx=0.55, rely=0.533, height=44, width=177)
Button7.configure(background=button_color)
Button7.configure(text='''Make Transaction''', borderwidth =".5")
Button7["command"]=win8

Button6 =Button(root)
Button6.place(relx=0.55, rely=0.689, height=44, width=177)
Button6.configure(background="#42d832")
Button6.configure(text='''Save''', borderwidth =".5")
Button6["command"]=quit_fun
root.mainloop()