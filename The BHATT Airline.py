from Tkinter import*
aq=open( 'list_l.txt','r+')
l=aq.readlines()
aq.close()


aw=open( 'list_k.txt','r+')
k=aw.readlines()
aw.close()

ae=open( 'list_j.txt','r+')
j=ae.readlines()
ae.close()

ar=open( 'list_h.txt','r+')
h=ar.readlines()
ar.close()

at=open( 'list_g.txt','r+')
g=at.readlines()
at.close()

ay=open( 'list_f.txt','r+')
f=ay.readlines()
ay.close()

string11=["GUJRAT "+'To'+" BHAJANPURA","BHAJANPURA "+'To'+" GUJRAT","GUJRAT "+'To'+" DELHI","DELHI "+'To'+" GUJRAT","DELHI "+'To'+" BHAJANPURA","BHAJANPURA "+'To'+" DELHI"]

string12=['Tir:-','\n','Name:-','E-mail:-','LEAVING FROM:-','GOING TO:-','']
######################################################################################################################################################################

ff=''

class home:
    def __init__(self,qq):
        self.check1q= qq
        self.o=345
        print self.o
        menubar = Menu(self.check1q)
        usermenu= Menu(menubar, fg = 'blue')
        usermenu.add_command(label='login for reset FLIGHT',command=self.usercall)
        menubar.add_cascade(label= 'Want to  reset FLIGHT', menu=usermenu)
        helpmenu = Menu(menubar, fg = 'blue')
        
        helpmenu.add_command(label="Help",command=self.hellp)
        
        
        
        menubar.add_cascade(label="Help", menu=helpmenu)

        
        
        filemenu = Menu(menubar, fg = 'red')#making menu
        
        filemenu.add_command(label="Exit program", command=self.destroy)#adding options commands
        
        menubar.add_cascade(label="Exit", menu=filemenu)#putting potions

        
        self.check1q.config(menu=menubar)
        
        self.photo1 = PhotoImage(file="1.gif")
        self.photo2 = PhotoImage(file="2.gif")
        self.photo3 = PhotoImage(file="3.gif") 
        self.b11=Button(self.check1q,image= self.photo1,command= self.call )
        self.b2=Button(self.check1q,image= self.photo2,command= self.caall)
        self.b3=Button(self.check1q,image= self.photo3,command= self.infocall)
        self.b11.grid(column= 1,row= 1)
        self.b2.grid(column= 2,row= 1)
        self.b3.grid(column= 3,row= 1)
        
        
        
        self.photo4 = PhotoImage(file="4.gif")
        self.a=Label(self.check1q,image=self.photo4)
        self.a.grid(column= 1,row= 2)
        self.photo5 = PhotoImage(file="5.gif")
        self.a=Label(self.check1q,image=self.photo5)
        self.a.grid(column= 2,row= 2)
        self.photo6 = PhotoImage(file="6.gif")
        self.a=Label(self.check1q,image=self.photo6)
        self.a.grid(column= 3,row= 2)

    def destroy(self):
        self.check1q.destroy()
    def call(self):
        
        rw = Toplevel()
        app = reservation(rw)
        rw.mainloop()
        
    def caall(self):
        
        qw= Toplevel()
        app= cancellation(qw)
        qw.mainloop()
    def infocall(self):
        er= Toplevel()
        app= info(er)
        er.mainloop()
    def usercall(self):
        qt=Toplevel()
        app=login(qt)
        qt.mainloop()
    def hellp(self):
        
        app=Help()
        
        
    
#####################################################################################################################################################################      



        
class reservation( home ):
    
    
    def __init__(self,ma):
        
        self.ma=ma
        self.check1 = StringVar() 
        self.check2 = StringVar()
        self.radio= StringVar()
    
        self.buttonofstatus= Button(self.ma, text="►FLITE STATUS◄",fg='blue', command= self.status).grid(column=3,row=3)

        self.l0= Label(self.ma,text="your name is")
        self.l0.grid(column= 1,row= 3)
        self.e0= Entry(self.ma)
        self.e0.grid(column= 2,row=3)
        self.e=self.e0.get()############
        self.l4= Label(self.ma,text="your e-mail add.")
        self.l4.grid(column= 1,row= 4)
        self.e4= Entry(self.ma)
        self.e4.grid(column= 2,row= 4)
        self.r=self.e4.get()############

    
        self.l1= Label(self.ma,text="Leaving from")
        self.l1.grid(column= 1,row= 5)    
        self.r11=Checkbutton(self.ma,text="DELHI",variable= self.check1, onvalue="DELHI", offvalue='e')
        self.r11.grid(column= 1,row= 6)
        self.r21=Checkbutton (self.ma,text="GUJRAT",variable= self.check1, onvalue="GUJRAT", offvalue='e')
        self.r21.grid(column= 2,row= 6)
        self.r31=Checkbutton (self.ma,text="BHAJANPURA",variable= self.check1, onvalue="BHAJANPURA", offvalue='e')
        self.r31.grid(column= 3,row= 6)
    
    
        self.l2= Label(self.ma,text="Going to")
        self.l2.grid(column= 1,row= 7)
        self.r111=Checkbutton(self.ma,text="DELHI",variable=self.check2, onvalue="DELHI", offvalue='e')
        self.r111.grid(column= 1,row= 8)
        self.r211=Checkbutton (self.ma,text="GUJRAT",variable=self.check2, onvalue="GUJRAT", offvalue='e')
        self.r211.grid(column= 2,row= 8)
        self.r311=Checkbutton (self.ma,text="BHAJANPURA",variable=self.check2, onvalue="BHAJANPURA", offvalue='e')
        self.r311.grid(column= 3,row= 8)
    
        self.r1=Radiobutton (self.ma,text="student",value=1,variable=self.radio)
        self.r1.grid(column= 1,row= 9)
        self.r2=Radiobutton (self.ma,text="buisness man",value="buisness man",variable=self.radio)
        self.r2.grid(column= 2,row= 9)
        self.r3=Radiobutton (self.ma,text="servant",value="servant",variable=self.radio)
        self.r3.grid(column= 1,row= 10)
        self.r3=Radiobutton (self.ma,text="child",value="child",variable=self.radio)
        self.r3.grid(column= 2,row= 10)
        self.b1 = Button(self.ma, text="►   get  ◄", command= self.get)     
        self.b1.grid(column= 2,row= 11)

        
    def status(self):
        make= Tk()
        df=['l','k','j','h','g','f']
        www=''
        for p in range(6):
            a=open('list_'+str(df[p])+'.txt','r')
            lk=len(a.readlines())
            w=str(lk)
            a.close()
            fv='FLITE:-'+str(string11[p])
            y=w+'seats are left'
            www=www+fv+'\n'+y+'\n'
            b=str(10-lk)+'seats are booked'
            www=www+b+'\n'+'\n'
            print(www)
        lll1=Label(make,text=str(www),fg='green').grid(column=1,row=1)
        make.mainloop()


        
    def get(self):
        print(self.e0.get(),self.e4.get(),self.check1.get(),self.check2.get(),self.radio.get())
        
        if  self.check1.get() ==  self.check2.get() or self.check1.get() =='' or self.check2.get()=='' or self.e0.get()==''or self.radio.get()==''or '@'not in self.e4.get():
          1
          if  self.check1.get() ==  self.check2.get():
            1
            call2= Tk()
            l12= Label(call2,text="ERROR__ Can not go same place try again",fg = 'red').grid(column= 2,row= 1)
            b11=Button(call2,text="close",relief=SUNKEN,height=2,width=5, command= call2.destroy)
            b11.grid(column=2,row=2)
            call2.mainloop()
          elif'@'not in self.e4.get():
              call2= Tk()
              l12= Label(call2,text="ERROR__ e-mail is wrong ",fg = 'blue').grid(column= 2,row= 1)
              b11=Button(call2,text="close",relief=SUNKEN,height=2,width=5, command= call2.destroy)
              b11.grid(column=2,row=2)
              call2.mainloop()
              
            
          else:
              call2= Tk()
              l12= Label(call2,text="ERROR__ Can not can't live any information try again",fg = 'blue').grid(column= 2,row= 1)
              b11=Button(call2,text="close",relief=SUNKEN,height=2,width=5, command= call2.destroy)
              b11.grid(column=2,row=2)
              call2.mainloop()
        else:
            if self.check1.get()=="GUJRAT" and self.check2.get()=="BHAJANPURA":
                a6=open('list_l.txt','r+')
                list1=a6.readlines()
                a6.close()
                w=len(list1)
                if w== 0:
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="SORRY ON SEATS ARE LEFT ",fg = 'red').grid(column= 2,row= 1)
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
                else:
                    
                    
                    qw= open("ll.txt","a+")
                    qw.write(list1[w-1])#
                    ff=list1.pop(w-1)
                    a6=open('list_l.txt','w+')
                    
                    for i in list1:
                        a6.writelines(i)
                    a6.close()
                        
                    
                    qw.write('\n')
                    qw.write(self.e0.get())#
                    qw.write('\n')
                    qw.write(self.e4.get())#
                    qw.write('\n')
                    qw.write(self.check1.get())#
                    qw.write('\n')
                    qw.write(self.check2.get())#
                    qw.write('\n')
                    qw.write(self.radio.get())#
                    qw.write('\n')
                    qw.close()    
                    print(self.e0.get(),self.e4.get(),self.check1.get(),self.check2.get(),self.radio.get())###########################################
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="YOUR TRI NUMBER IS "+str(ff),fg = 'red').grid(column= 2,row= 1)
                    ff=''
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
            elif self.check1.get()=="BHAJANPURA" and self.check2.get()=="GUJRAT":
                a6=open('list_k.txt','r+')
                list2=a6.readlines()
                a6.close()
                w=len(list2)
                if w== 0:
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="SORRY ON SEATS ARE LEFT ",fg = 'red').grid(column= 2,row= 1)
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
                else:
                    
                    qw= open("kk.txt","a+")
                    qw.write(list2[w-1])#
                    ff=list2.pop(w-1)
                    a5=open('list_k.txt','w+')
                    for i in list2:
                        a5.writelines(i)
                    a5.close()
                    
                    qw.write('\n')
                    qw.write(self.e0.get())#
                    qw.write('\n')
                    qw.write(self.e4.get())#
                    qw.write('\n')
                    qw.write(self.check1.get())#
                    qw.write('\n')
                    qw.write(self.check2.get())#
                    qw.write('\n')
                    qw.write(self.radio.get())#
                    qw.write('\n')
                    qw.close()    
                    print(self.e0.get(),self.e4.get(),self.check1.get(),self.check2.get(),self.radio.get())###########################################
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="YOUR TRI NUMBER IS "+str(ff),fg = 'red').grid(column= 2,row= 1)
                    ff=''
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
                
            elif self.check1.get()=="GUJRAT" and self.check2.get()=="DELHI":
                
                a6=open('list_j.txt','r+')
                x3=a6.readlines()
                a6.close()
                w=len(x3)
                if w== 0:
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="SORRY ON SEATS ARE LEFT ",fg = 'red').grid(column= 2,row= 1)
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
                else:
                    qw= open("jj.txt","a+")
                    qw.write(x3[w-1])#
                    ff=x3.pop(w-1)
                    a4=open('list_j.txt','w+')
                    for i in x3:
                        a4.writelines(i)
                    a4.close()
                    
                    qw.write('\n')
                    qw.write(self.e0.get())#
                    qw.write('\n')
                    qw.write(self.e4.get())#
                    qw.write('\n')
                    qw.write(self.check1.get())#
                    qw.write('\n')
                    qw.write(self.check2.get())#
                    qw.write('\n')
                    qw.write(self.radio.get())#
                    qw.write('\n')
                    qw.close()    
                    print(self.e0.get(),self.e4.get(),self.check1.get(),self.check2.get(),self.radio.get())###########################################
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="YOUR TRI NUMBER IS "+str(ff),fg = 'red').grid(column= 2,row= 1)
                    ff=''
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
            elif self.check1.get()=="DELHI" and self.check2.get()=="GUJRAT":
                a6=open('list_h.txt','r+')
                list4=a6.readlines()
                a6.close()
                w=len(list4)
                if w== 0:
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="SORRY ON SEATS ARE LEFT ",fg = 'red').grid(column= 2,row= 1)
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
                else:
                    qw= open("hh.txt","a+")
                    qw.write(list4[w-1])#
                    ff=list4.pop(w-1)
                    a3=open('list_h.txt','w+')
                    for i in list4:
                        a3.writelines(i)
                    a3.close()
                    
                    qw.write('\n')
                    qw.write(self.e0.get())#
                    qw.write('\n')
                    qw.write(self.e4.get())#
                    qw.write('\n')
                    qw.write(self.check1.get())#
                    qw.write('\n')
                    qw.write(self.check2.get())#
                    qw.write('\n')
                    qw.write(self.radio.get())#
                    qw.write('\n')
                    qw.close()    
                    print(self.e0.get(),self.e4.get(),self.check1.get(),self.check2.get(),self.radio.get())###########################################
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="YOUR TRI NUMBER IS "+str(ff),fg = 'red').grid(column= 2,row= 1)
                    ff=''
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
            elif self.check1.get()=="DELHI" and self.check2.get()=="BHAJANPURA" :
                a6=open('list_g.txt','r+')
                list5=a6.readlines()
                a6.close()
                w=len(list5)
                if w== 0:
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="SORRY ON SEATS ARE LEFT ",fg = 'red').grid(column= 2,row= 1)
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
                else:
                    qw= open("gg.txt","a+")
                    qw.write(list5[w-1])#
                    ff=list5.pop(w-1)
                    a2=open('list_g.txt','w+')
                    for i in list5:
                        a2.writelines(i)
                    a2.close()
                    
                    qw.write('\n')
                    qw.write(self.e0.get())#
                    qw.write('\n')
                    qw.write(self.e4.get())#
                    qw.write('\n')
                    qw.write(self.check1.get())#
                    qw.write('\n')
                    qw.write(self.check2.get())#
                    qw.write('\n')
                    qw.write(self.radio.get())#
                    qw.write('\n')
                    qw.close()    
                    print(self.e0.get(),self.e4.get(),self.check1.get(),self.check2.get(),self.radio.get())###########################################
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="YOUR TRI NUMBER IS "+str(ff),fg = 'red').grid(column= 2,row= 1)
                    ff=''
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
            elif self.check1.get()=="BHAJANPURA" and self.check2.get()=="DELHI":
                a6=open('list_f.txt','r+')
                list6=a6.readlines()
                a6.close()
                w=len(list6)
                if w== 0:
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="SORRY ON SEATS ARE LEFT ",fg = 'red').grid(column= 2,row= 1)
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
                else:
                    qw= open("ff.txt","a+")
                    qw.write(list6[w-1])#
                    ff=list6.pop(w-1)
                    a1=open('list_f.txt','w+')
                    for i in list6:
                        a1.writelines(i)
                    a1.close()
                    
                    qw.write('\n')
                    qw.write(self.e0.get())#
                    qw.write('\n')
                    qw.write(self.e4.get())#
                    qw.write('\n')
                    qw.write(self.check1.get())#
                    qw.write('\n')
                    qw.write(self.check2.get())#
                    qw.write('\n')
                    qw.write(self.radio.get())#
                    qw.write('\n')
                    qw.close()    
                    print(self.e0.get(),self.e4.get(),self.check1.get(),self.check2.get(),self.radio.get())###########################################
                    self.ma.destroy()
                    tu= Tk()
                    ls= Label(tu,text="YOUR TRI NUMBER IS "+str(ff),fg = 'red').grid(column= 2,row= 1)
                    ff=''
                    bs=Button(tu,text="close",relief=SUNKEN,height=2,width=5, command= tu.destroy)
                    bs.grid(column=2,row=2)
#####################################################################################################################################################################
class cancellation(home):

    
    def __init__(self,ma):
        self.ma= ma
        self.l0= Label(self.ma,text="your tir number is")
        self.l0.grid(column= 1,row= 3)
        self.e0= Entry(self.ma)
        self.e0.grid(column= 2,row=3)
        self.b00= Button(self.ma,text='want cancel your ticket',command= self.find)
        self.b00.grid(column= 2,row=4)
        self.stri997='''['lle1','lle2','lle3','lle4','lle5','lle6','lle7','lle8','lle9','lle10']
['kke1','kke2','kke3','kke4','kke5','kke6','kke7','kke8','kke9','kke10']
['jje1','jje2','jje3','jje4','jje5','jje6','jje7','jje8','jje9','jje10']
['hhe1','hhe2','hhe3','hhe4','hhe5','hhe6','hhe7','hhe8','hhe9','hhe10']
['gge1','gge2','gge3','gge4','gge5','gge6','gge7','gge8','gge9','gge10']
['ffe1','ffe2','ffe3','ffe4','ffe5','ffe6','ffe7','ffe8','ffe9','ffe10']'''
        
    
    def find(self):###############3
        if self.e0.get()=='' or self.e0.get() not in self.stri997:
            ssss=Tk()
            
            self.l0= Label(ssss,text="May you don't give TIR number or type it WRONG",fg='red')
            self.l0.grid(column= 1,row= 1)
            self.b01= Button(ssss,text='                     ok                     ',command= ssss.destroy)
            self.b01.grid(column= 1,row=2)
            ssss.mainloop()
        else:            
            oo=[]
            w= str(self.e0.get())+'\n'
            print(w)
            qs=w[0:2]
            io=str(qs)+'.txt'
            ab=open(io,'r+')
            s=0
            la=ab.readlines()
            
            
            for i in la:
                
        
                if w==i:
                    a=open('list_'+str(w[0])+'.txt','a+')
                    a.writelines(w)
                    a.close()
                    for ig in range(7):
                        print(la[s])
                        la.pop(s)
                        
                        
                else:
                    s=s+1
                    oo.append(i)
            ab.close()
            ag=open(io,'w+')

            for i in la:
                ag.writelines(i)
                
            ag.close()
            oo=[]
            ssss=Tk()
            self.l0= Label(ssss,text="YOUR TICKET IS CANCELED",fg='BLUE')
            self.l0.grid(column= 1,row= 1)
            self.b01= Button(ssss,text='                     ok                     ',command= ssss.destroy)
            self.b01.grid(column= 1,row=2)
            ssss.mainloop()
#####################################################################################################################################################################
        
class info(home):
    
    def __init__(self,ma):
        self.ma= ma       
        self.b00= Button(self.ma,text='ABOUT US',command= self.user1)
        self.b00.grid(column= 1,row=1)
        self.b00= Button(self.ma,text='ABOUT TICKET OWNER',command= self.findd)
        self.b00.grid(column= 2,row=1)
        
    def findd(self):
        self.ma.destroy()
        ax= Tk()
        app= sinfo(ax)
        ax.mainloop()
        
    def user1(self):
        self.ma.destroy()
        ss=Tk()
        self.l0= Label(ss,text='''Corporate Overview
SpiceJet’s mission is to become India’s preferred low-cost airline
delivering the lowest air fares with the highest consumer value\n to price sensitive consumers. We hope to fulfill everyone’s dream of flying!
With India's economic and business growth\n the percentage of traveling population is burgeoning. More and more Indians are traveling for both business and pleasure and everyone needs to save both time and money. SpiceJet's vision is to address that and ensure that flying is for everyone.
The power to fly for everyone
With a dynamic fare structure\n SpiceJet offers fares that are affordable and significantly lower than most airlines. With contemporary interiors\n modern graphics and vibrant colours, SpiceJet is very much like today’s traveler - practical yet stylish. A SpiceJetter will feel ‘this is the smart\n international way to travel\n I've made the smart choice’. SpiceJet is committed to make sure you feel good at the end of a flight\n arriving at your destination - fresh and on time.
The power of performance.
From aircraft to crew and ground staff the focus is on performance. Each SpiceJet employee is groomed to be smart\n friendly\n efficient and well-informed\n ensuring that any interaction will make you feel welcome and looked after. Experienced pilots\n well-trained cabin crew will make every flight a comfortable one. The philosophy is no-frills but high-performance.
The power of safety
SpiceJet invests heavily in safety\n impeccable maintenance and a high level of expertise. Experienced pilots\n engineers and maintenance crew go through rigorous training and are hand-picked for their technical knowledge and expertise. So you can rest assured that there is no cut-back in this key area of modern day flying.
The power behind the power to fly
SpiceJet's key management personnel are all senior\n seasoned professionals and have significant international experience in both launching and managing low-cost airlines. With thousands of cumulative man hours in the industry\n the management is committed to bring to customers in India all the benefits of the global revolution in the skies. SpiceJet aims to make travel comfortable\n affordable and refreshingly efficient experience for all.
Welcome on board India's newest\n smartest and most affordable low-fare airline. India\n get ready for the power to fly!''', fg='blue')###############-----------------------------333
        self.l0.grid(column= 1,row= 1)
        
        
        
#####################################################################################################################################################################        
        
        
        

class sinfo(home):
    

    def __init__(self,ma):
        
        self.ma= ma
        self.l0= Label(self.ma,text="► your tir number is")
        self.l0.grid(column= 1,row= 3)
        self.e01= Entry(self.ma)
        self.e01.grid(column= 2,row=3)
        self.b00= Button(self.ma,text='҉ want to know about ticket woner ҉ ',command= self.find)
        self.b00.grid(column= 2,row=4)
        self.stri997='''['lle1','lle2','lle3','lle4','lle5','lle6','lle7','lle8','lle9','lle10'']
['kke1','kke2','kke3','kke4','kke5','kke6','kke7','kke8','kke9','kke10']
['jje1','jje2','jje3','jje4','jje5','jje6','jje7','jje8','jje9','jje10']
['hhe1','hhe2','hhe3','hhe4','hhe5','hhe6','hhe7','hhe8','hhe9','hhe10']
['gge1','gge2','gge3','gge4','gge5','gge6','gge7','gge8','gge9','gge10']
['ffe1','ffe2','ffe3','ffe4','ffe5','ffe6','ffe7','ffe8','ffe9','ffe10']'''

       
#####################################################################################################################################################################    
    
    def find(self):
        if self.e01.get()=='' or self.e01.get() not in self.stri997 :
            
            sss=Tk()
            self.l0= Label(sss,text="May you don't give TIR number or type it WRONG")
            self.l0.grid(column= 1,row= 1)

            button= Button(sss,text='                     ok                     ',command= sss.destroy )
            button.grid(column=1,row=2)
            sss.mainloop()
        else:
            res= Toplevel()     
            w= str(self.e01.get())+'\n'
            print(w)
            qs=w[0:2]
            io=str(qs)+'.txt'
            ab=open(io,'r+')
            s=0
            lw=ab.readlines()
            print(lw)
            for i in lw:
                
        
                if w==i:
                    
                    for ig in range(7):
                        print(lw[s])
                        self.l00= Label(res,text=str(string12[ig])+str(lw[s]).rstrip('\n'))
                        self.l00.grid(column= 1,row= ig)
                        s=s+1
                else:
                    s=s+1
            self.photo11 = PhotoImage(file="11.gif")
            self.a=Label(res,image=self.photo11)
            self.a.grid(column= 1,row= 8)
            ab.close()
        
#####################################################################################################################################################################        
class login(home):
    
    def __init__(self,ma):
        self.ma=ma
        self.l0= Label(self.ma,text="҉ Enter  MANAGEMENT Password to reset FLIGHT ҉ ")
        self.l0.grid(column= 1,row= 1)
        self.e01= Entry(self.ma)
        self.e01.grid(column= 2,row=2)
        button1= Button(self.ma,text='►reset FLIGHT◄',command=self.choose  )
        button1.grid(column=1,row=2)
        
    def choose(self):
        
        if self.e01.get()== 'ilovemyfather':
            self.ma.destroy()
            self.zz=Tk()
            self.l0o= Label(self.zz,text="WHICH FLIGHT YOU WANT TO CHANGE ")
            self.l0o.grid(column= 1,row= 1)
            self.l0oo= Label(self.zz,text="FLIGHTE NAME ARE:- ")
            self.l0oo.grid(column= 1,row= 2)
            self.l0ooo= Label(self.zz,text='FLIGHT--------lle')
            self.l0ooo.grid(column= 2,row= 3)
            self.l0oo= Label(self.zz,text="FLIGHT--------kke")
            self.l0oo.grid(column= 2,row= 4)
            self.l0oo= Label(self.zz,text="FLIGHT--------jje")
            self.l0oo.grid(column= 2,row= 5)
            self.l0oo= Label(self.zz,text="FLIGHT--------hhe")
            self.l0oo.grid(column= 2,row= 6)
            self.l0oo= Label(self.zz,text="FLIGHT--------gge")
            self.l0oo.grid(column= 2,row= 7)
            self.l0oo= Label(self.zz,text="FLIGHT--------ffe")
            self.l0oo.grid(column= 2,row= 8)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 3)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 4)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 5)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 6)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 7)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 7)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 8)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 9)

            self.l0ooo= Label(self.zz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 3)
            self.l0ooo= Label(self.zz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 4)
            self.l0ooo= Label(self.zz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 5)
            self.l0ooo= Label(self.zz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 6)
            self.l0ooo= Label(self.zz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 7)
            self.l0ooo= Label(self.zz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 7)
            self.l0ooo= Label(self.zz,text='E'    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 8)

            
            
            self.e011= Entry(self.zz)
            self.e011.grid(column=2 ,row=9)
            self.l0ooo= Label(self.zz,text='Q '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 10)
            button= Button(self.zz,text='   reset FLIGHT   ',command=self.create  )
            button.grid(column=3,row=10)
            self.zz.mainloop()
        elif self.e01.get()== 'resetall':
            l3=['l','k','j','h','g','f']        
            for i in l3:
                x=open(str(i)+str(i)+'.txt','w+')             
                x.close()
                x=open('list_'+str(i)+'.txt','w+')
                for j in range(10):
                    x.writelines(i+i+'e'+str(j+1))
                    x.write('\n')             
                x.close()
            qwe=Tk()
            self.l0ooo= Label(qwe,text='☺ ALL FILES ',fg='BLUE')
            self.l0ooo.grid(column=1,row=1)
            self.l0ooo= Label(qwe,text=' AND FLIGHTES ',fg='BLUE')
            self.l0ooo.grid(column=3,row=1)
            self.l0ooo= Label(qwe,text=' ARE RESET ☺',fg='BLUE')
            self.l0ooo.grid(column=5,row=1)
            self.l0ooo= Label(qwe,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column=2,row=1)
            self.l0ooo= Label(qwe,text='Q'    ,font='Wingdings')
            self.l0ooo.grid(column=4,row=1)
            button= Button(qwe,text='                     ok                     ',command= qwe.destroy )
            button.grid(column=1,row=3)
                
            
        
        elif self.e01.get()=='resetrecodes':
            self.ma.destroy()
            self.zzz=Tk()
            self.l0o= Label(self.zzz,text="WHICH file YOU WANT TO CHANGE ", fg= 'red')
            self.l0o.grid(column= 1,row= 1)
            self.l0oo= Label(self.zzz,text="FILE NAME ARE:- ")
            self.l0oo.grid(column= 1,row= 2)
            self.l0ooo= Label(self.zzz,text='FILE--------lle')
            self.l0ooo.grid(column= 2,row= 3)
            self.l0oo= Label(self.zzz,text="FILE--------kke")
            self.l0oo.grid(column= 2,row= 4)
            self.l0oo= Label(self.zzz,text="FILE--------jje")
            self.l0oo.grid(column= 2,row= 5)
            self.l0oo= Label(self.zzz,text="FILE--------hhe")
            self.l0oo.grid(column= 2,row= 6)
            self.l0oo= Label(self.zzz,text="FILE--------gge")
            self.l0oo.grid(column= 2,row= 7)
            self.l0oo= Label(self.zzz,text="FILE--------ffe")
            self.l0oo.grid(column= 2,row= 8)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 3)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 4)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 5)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 6)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 7)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 7)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 8)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 9)

            self.l0ooo= Label(self.zzz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 3)
            self.l0ooo= Label(self.zzz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 4)
            self.l0ooo= Label(self.zzz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 5)
            self.l0ooo= Label(self.zzz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 6)
            self.l0ooo= Label(self.zzz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 7)
            self.l0ooo= Label(self.zzz,text='E '    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 7)
            self.l0ooo= Label(self.zzz,text='E'    ,font='Wingdings')
            self.l0ooo.grid(column= 3,row= 8)

            
            
            self.e011= Entry(self.zzz)
            self.e011.grid(column=2 ,row=9)
            self.l0ooo= Label(self.zzz,text='1 '    ,font='Wingdings')
            self.l0ooo.grid(column= 1,row= 10)
            button= Button(self.zzz,text=' ►reset FLIGHT◄ ',command=self.reset  )
            button.grid(column=3,row=10)
            self.zzz.mainloop()
            
        else:
            qwe=Tk()
            self.l0ooo= Label(qwe,text='͏WRONG PASSWORD TRY AGAIN͏',fg='green')
            self.l0ooo.grid(column=1,row=1)
            button= Button(qwe,text='                     ►ok◄                     ',command= qwe.destroy )
            button.grid(column=1,row=2)

            qwe.mainloop()


            
    def create(self):
        if self.e011.get()=='' or self.e011.get()not in'lle,kke,jje,hhe,gge,ffe':
            
            qwe=Tk()
            self.l0ooo= Label(qwe,text='WRONG FLIGHT TRY AGAIN',fg='green')
            self.l0ooo.grid(column=1,row=1)
            button= Button(qwe,text='                    ►ok◄                    ',command= qwe.destroy )
            button.grid(column=1,row=2)
            qwe.mainloop()
        
            
            
            
        else:
            
            l=str(self.e011.get())
            q=l[0]
            x=open('list_'+str(q)+'.txt','w+')
            for i in range(10):
                x.writelines(q+q+'e'+str(i+1))
                x.write('\n')             
            x.close()
            self.zz.destroy()
            qwe=Tk()
            self.l0ooo= Label(qwe,text='Q',fg='green',font='Wingdings')
            self.l0ooo.grid(column=1,row=1)
            self.l0ooo= Label(qwe,text='☺ FLIGHT IS NOW RESET ☻',fg='green')
            self.l0ooo.grid(column=1,row=1)
            button= Button(qwe,text='                     ok                     ',command= qwe.destroy )
            button.grid(column=1,row=2)

            qwe.mainloop()


            
    def reset(self):
        
        l=str(self.e011.get())
        q=l[0]
        x=open(str(q)+str(q)+'.txt','w+')             
        x.close()
        self.zzz.destroy()
        qwe=Tk()
        self.l0ooo= Label(qwe,text='Q',fg='green',font='Wingdings')
        self.l0ooo.grid(column=1,row=1)
        self.l0ooo= Label(qwe,text='☺ FILE IS NOW RESET ☺',fg='BLUE')
        self.l0ooo.grid(column=1,row=1)
        button= Button(qwe,text='                     ok                     ',command= qwe.destroy )
        button.grid(column=1,row=2)
                    
        
####################################################################################################################################################            



class Help:
    def __init__(self):
        qwe=Tk()

        self.l0ooo= Label(qwe,text='''Corporate Overview
SpiceJet’s mission is to become India’s preferred low-cost airline
delivering the lowest air fares with the highest consumer value\n to price sensitive consumers. We hope to fulfill everyone’s dream of flying!
With India's economic and business growth\n the percentage of traveling population is burgeoning. More and more Indians are traveling for both business and pleasure and everyone needs to save both time and money. SpiceJet's vision is to address that and ensure that flying is for everyone.
The power to fly for everyone
With a dynamic fare structure\n SpiceJet offers fares that are affordable and significantly lower than most airlines. With contemporary interiors\n modern graphics and vibrant colours, SpiceJet is very much like today’s traveler - practical yet stylish. A SpiceJetter will feel ‘this is the smart\n international way to travel\n I've made the smart choice’. SpiceJet is committed to make sure you feel good at the end of a flight\n arriving at your destination - fresh and on time.
The power of performance.
From aircraft to crew and ground staff the focus is on performance. Each SpiceJet employee is groomed to be smart\n friendly\n efficient and well-informed\n ensuring that any interaction will make you feel welcome and looked after. Experienced pilots\n well-trained cabin crew will make every flight a comfortable one. The philosophy is no-frills but high-performance.
The power of safety
SpiceJet invests heavily in safety\n impeccable maintenance and a high level of expertise. Experienced pilots\n engineers and maintenance crew go through rigorous training and are hand-picked for their technical knowledge and expertise. So you can rest assured that there is no cut-back in this key area of modern day flying.
The power behind the power to fly
SpiceJet's key management personnel are all senior\n seasoned professionals and have significant international experience in both launching and managing low-cost airlines. With thousands of cumulative man hours in the industry\n the management is committed to bring to customers in India all the benefits of the global revolution in the skies. SpiceJet aims to make travel comfortable\n affordable and refreshingly efficient experience for all.
Welcome on board India's newest\n smartest and most affordable low-fare airline. India\n get ready for the power to fly!
''',fg='blue')
        self.l0ooo.grid(column=1,row=1)
        button= Button(qwe,text='                     ok                     ',command= qwe.destroy )
        button.grid(column=1,row=2)
        qwe.mainloop()
            
        
####################################################################################################################################################        

        
            




        

        
    
qqq= Tk()
app= home(qqq)
qqq.mainloop()

############################################################################################################################################################


