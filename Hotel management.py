
print ('Welcome to Hotel')

c='y'

#Cost Calulation Function

def cost(Type,j,duration):

    global l



    for er in l:

        tempstr=er.split(" ")

        if j in tempstr:

            i=l.index(er)

    global c_cost

    if Type=='A' or Type=='a':

        print (" The amount you need to pay is = "),

        if duration<=2:



            c_cost='1700'

            print (' Rs . 1700 ')

            l[i]=l[i]+c_cost + '\n'

        else:

            tempcost=duration*949 + 1700

            print (' Rs . ',tempcost)

            c_cost=str(tempcost)

            l[i]=l[i]+c_cost + '\n'

    elif Type=='B' or Type=='b':

        print ' The amount you need to pay is =',

        if duration<=2:



            c_cost='2700'

            print ' Rs . 2700 '

            l[i]=l[i]+c_cost + '\n'

        else:

            tempcost=duration*1450 + 2700

            print ' Rs . ',tempcost

            c_cost=str(tempcost)

            l[i]=l[i]+c_cost + '\n'

    if Type=='C' or Type=='c':

        print ' The amount you need to pay is =',

        if duration<=2:



            c_cost='4700'

            print ' Rs . 4700 '

            l[i]=l[i]+c_cost + '\n'

        else:

           tempcost=duration*2950 + 2700

           print ' Rs . ',tempcost

           c_cost=str(tempcost)

           l[i]=l[i]+c_cost + '\n'

    

            

l=[];cstr=[]

from Tkinter import *

import random

import time

#Main body for hotel management

while c=='y':

    print ''' Please choose one of the choices given below to experience our services

              1. Room booking

              2. View your reservation details

              3. Cancel your reservation

              4. Order Food'''

    choice=int(raw_input('enter your choice (1,2,3,4) : '))

    if choice==1:   #For Room Booking

        print "You have chosen to stay in our hotel "

        fobj=open('bookings.txt','w')

        cobj=open('cost.txt','w')

        n=int(raw_input('How many people are going to stay in this hotel : '))

        for i in range (n):

           

            Name=raw_input(' Enter the ' + str(i+1) + '\'st customers name - ')

            age=raw_input(" Enter your age : ")

            Id=raw_input(" Give valid Identification proof : ")

            Type=raw_input(' Enter the type of room you want (Normal(enter A): Rs.1700 , Suite(enter B):Rs.2700 or Delux(enter C):Rs.4700) : ')

            duration=int(raw_input('Enter the duration of your stay  (Number of days) : '))

            l.append(Name + ' ' + age + ' ' + Id + ' ' + Type + ' '+str(duration)+' ')

            cost(Type,Id,duration)

            cstr.append(Id + ' ' + '0' + '\n')

        print ' You have done your booking and may proceed to your respective room.'

        fobj.writelines(l)

        cobj.writelines(cstr)
        
        fobj.close()

        cobj.close()

    elif choice==2:     #For Viewing the list of Customers

        fobj=open('bookings.txt','r')

        l=fobj.readlines()

        foodcost = 0

        c = open('cost.txt','r')

        arr = c.readlines()

        fobj.seek(0)

        idproof=raw_input("Enter your Id : ")

        tempread=fobj.read()

        if idproof not in tempread:

            print "No reservations with that ID available"

        for i in arr:

            li = i.split()

            if ( li[0] == idproof):

                foodcost = foodcost + float(li[1])

        c.close()

        for j in l:

            ltemp=j.split(' ')

            if idproof == ltemp[2]:

                print "The customer's name is - ",ltemp[0]

                print "The customer's age is - ",ltemp[1]

                print "The customer's Id is - ",ltemp[2]

                print "The customer's room type choice : ",ltemp[3]

                print "The duration of the stay : ",ltemp[4],"days"

                cc = (float(ltemp[5]) + foodcost)
                
                print "Cost incurred: Rs.",cc

            

    elif choice==3:     #For Canceling the Customer details


            fobj=open('bookings.txt','r')
    
            q=fobj.readlines()

            cobj=open('cost.txt','r')

            p=cobj.readlines()

            cou = 0

            delId = raw_input("Enter the Id Number : ")

            for i in q:

                lstemp = i.split()

                if delId == str(lstemp[2]):

                    q.remove(i)

                    print "Reservation is Removed."

                    break

            fobj.close()

            for j in p:

                ls = j.split()

                if delId == str(ls[0]):

                    p.remove(j)

            if (len(q)==0) | (cou == 0):

                print "No reservations"            
            
            cobj.close()

            fobj=open("bookings.txt","w")

            fobj.writelines(q)

            cobj = open('cost.txt','w')

            cobj.writelines(p)


    elif choice==4:   #For Taking the Food Order of the Customer

        
        Id = raw_input('Enter the Id Number : ')

        root = Tk()

        root.geometry("1600x800+0+0")

        root.title("FOOD ORDER PORTAL")



        text_Input = StringVar()

        operator= " "







        Tops = Frame( root, width = 1600, height = 50 ,bg = "gold4" , relief=SUNKEN)

        Tops.pack(side=TOP)



        f1 = Frame( root, width = 800,height = 700  , relief=SUNKEN)

        f1.pack(side=LEFT)



        f2 = Frame( root, width = 300, height = 700 , relief=SUNKEN)

        f2.pack(side=RIGHT)

        #==========time=============================



        localtime = time.asctime(time.localtime(time.time()))



        #==============info=========================



        lblInfo = Label(Tops, font=("arial" , 50 ,"bold") ,text="Order Portal",fg="gold" , bd=10 , anchor = "w")

        lblInfo.grid(row=0, column=0)



        lblInfo = Label(Tops, font=("arial" , 20 ,"bold") ,text=localtime,fg="Steel Blue" , bd=10 , anchor = "w")

        lblInfo.grid(row=1, column=0)

        total = 0

        #=============calculator=============================

        def btnClick(numbers):

            global operator

            operator=operator + str(numbers)

            text_Input.set( operator)

        txtDisplay = Entry(f2, font=("arial", 20 , "bold"), textvariable=text_Input, bd =30, insertwidth=4,bg="powder blue", justify = "right")

        txtDisplay.grid(columnspan=4)



        def btnClearDisplay():

            global operator

            operator=" "

            text_Input.set(" ")



        def btnEqualsInput():

            global operator

            sumup=str(eval(operator))

            text_Input.set(sumup)

            operator=" "

        def Ref():
            global Totalcost

            x=random.randint(10345,23456)

            randomRef=str(x)

            rand.set(randomRef)

            Cof=float(Fries.get())

            CoP=float(Pav_bhaji.get())

            #CoCh=float(Chana_Bhatura.get())

            CoBurger=float(Chicken_Burger.get())

            CoS=float(Chicken_Shawarma.get())

            Cocola=float(Cola.get())

            CostofFries=Cof*25

            CostofCola=Cocola*35

            CostofPav=CoP*40

            #CostofChana=CoCh*80

            CostofBurger=CoBurger*50

            CostofShawarma=CoS*35

            Costofmeal="Rs.",str('%2f' % (CostofFries+CostofCola+CostofPav+CostofBurger+CostofShawarma))

            PayTax=((CostofFries+CostofCola+CostofPav+CostofBurger+CostofShawarma)*0.3)

            Totalcost=(CostofFries+CostofCola+CostofPav+CostofBurger+CostofShawarma)

            Ser_Charge=((CostofFries+CostofCola+CostofPav+CostofBurger+CostofShawarma)/99)

            Service='Rs.'+str('%2f' % Ser_Charge)

            PaidTax="Rs."+str(PayTax)

            Overallcost='Rs.'+str((PayTax+Totalcost+Ser_Charge))

            Service_charge.set(Service)

            Cost.set(Costofmeal)

            Total.set(Overallcost)

            Tax.set(PaidTax)

                                  
        def price():        #Price Button

            roo = Tk()

            roo.geometry("600x220+0+0")

            roo.title("Price List")

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)

            lblinfo.grid(row=0, column=0)

            lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)

            lblinfo.grid(row=0, column=2)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)

            lblinfo.grid(row=0, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Large Fries", fg="steel blue", anchor=W)

            lblinfo.grid(row=1, column=0)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)

            lblinfo.grid(row=1, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pav Bhaji", fg="steel blue", anchor=W)

            lblinfo.grid(row=2, column=0)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)

            lblinfo.grid(row=2, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Shawarma", fg="steel blue", anchor=W)

            lblinfo.grid(row=3, column=0)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)

            lblinfo.grid(row=3, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Burger", fg="steel blue", anchor=W)

            lblinfo.grid(row=4, column=0)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)

            lblinfo.grid(row=4, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cola", fg="steel blue", anchor=W)

            lblinfo.grid(row=6, column=0)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    
            lblinfo.grid(row=6, column=3)

            roo.mainloop()
    

        def qExit():

            root.destroy()

        def Reset():

            rand.set('')

            Fries.set('')

            Pav_bhaji.set('')

            Chana_Bhatura.set('')

            Chicken_Burger.set('')

            Chicken_Shawarma.set('')

            Cola.set('')

            Tax.set('')

            Cost.set('')

            Service_charge.set('')
            
            Total.set('')
        
        def Save():

            cobj=open('cost.txt','a+')

            '''for i in cobj:

                lstemp=i.split(" ")

                if Id == lstemp[1]:

                    ls1 = lstemp.pop()

                    cstr.append(str(Id)+' '+str(Totalcost)+'\n')

                    #cobj.writeline(cstr)    

                else:

                    cstr.append(i)
'''

            cstr.append(str(Id)+' '+str(Totalcost)+'\n')
            
            cobj.writelines(cstr)

            cobj.close()

            root.destroy()
 
        def Exit():

            root.destroy()

            



        btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2 , column=0)





        btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2 , column=1)





        btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2 , column=2)





        Addition = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2 , column=3)



        #============================================================================================================

        btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3 , column=0)





        btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3 , column=1)





        btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3 , column=2)





        Subtraction = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3 , column=3)



        #===============================================================================================================

        btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4 , column=0)





        btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4 , column=1)





        btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4 , column=2)





        Multiply = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "*", bg="powder blue", command=lambda: btnClick("*")).grid(row=4 , column=3)



        #==================================================================================================================================



        btn0 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5 , column=0)





        btnClear = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "C", bg="powder blue", command=btnClearDisplay).grid(row=5 , column=1)





        btnEquals= Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "=", bg="powder blue",command=btnEqualsInput).grid(row=5 , column=2)





        Division = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("arial" , 20 , "bold") , text= "/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5 , column=3)



        #================================Restaurant Info 1======================================================================================

        rand=StringVar()

        Fries = StringVar()

        Pav_bhaji=StringVar()

        Chana_Bhatura=StringVar()

        Chicken_Burger=StringVar()

        Chicken_Shawarma=StringVar()

        Tax=StringVar()

        Cost=StringVar()

        Service_charge=StringVar()

        Cola=StringVar()

        Total=StringVar()

        

        lblReference = Label(f1,font=("arial" , 16,"bold"), text="Reference" , bd=16, anchor = "w")

        lblReference.grid(row=0,column=0)

        txtReference=Entry(f1,font=("arial" , 16,"bold"), textvariable=rand , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtReference.grid(row=0,column=1)

        lblFries = Label(f1,font=("arial" , 16,"bold"), text="Large Fries" , bd=16, anchor = "w")

        lblFries.grid(row=1,column=0)

        txtFries=Entry(f1,font=("arial" , 16,"bold"), textvariable=Fries, bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtFries.grid(row=1,column=1)

        lblpavbhaji = Label(f1,font=("arial" , 16,"bold"), text="Pav Bhaji" , bd=16, anchor = "w")

        lblpavbhaji.grid(row=2,column=0)

        txtpavbhaji=Entry(f1,font=("arial" , 16,"bold"), textvariable=Pav_bhaji , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtpavbhaji.grid(row=2,column=1)

        lblchickenshawarma = Label(f1,font=("arial" , 16,"bold"), text="Chicken shawarma" , bd=16, anchor = "w")

        lblchickenshawarma.grid(row=3,column=0)

        txtchickenshawarma=Entry(f1,font=("arial" , 16,"bold"), textvariable=Chicken_Shawarma , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtchickenshawarma.grid(row=3,column=1)

        lblchickenburger= Label(f1,font=("arial" , 16,"bold"), text="Chicken Burger" , bd=16, anchor = "w")

        lblchickenburger.grid(row=0,column=2)

        txtchickenburger=Entry(f1,font=("arial" , 16,"bold"), textvariable=Chicken_Burger , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtchickenburger.grid(row=0,column=3)

        lblcola= Label(f1,font=("arial" , 16,"bold"), text="Cola" , bd=16, anchor = "w")

        lblcola.grid(row=1,column=2)

        txtcola=Entry(f1,font=("arial" , 16,"bold"), textvariable=Cola , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtcola.grid(row=1,column=3)

        lblcost = Label(f1,font=("arial" , 16,"bold"), text="Cost" , bd=16, anchor = "w")

        lblcost.grid(row=3,column=2)

        txtcost=Entry(f1,font=("arial" , 16,"bold"), textvariable=Cost , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtcost.grid(row=3,column=3)

        lbltax= Label(f1,font=("arial" , 16,"bold"), text="Tax" , bd=16, anchor = "w")

        lbltax.grid(row=2,column=2)

        txttax=Entry(f1,font=("arial" , 16,"bold"), textvariable=Tax , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txttax.grid(row=2,column=3)
        
        lblservicecharge= Label(f1,font=("arial" , 16,"bold"), text="Service Charge" , bd=16, anchor = "w")

        lblservicecharge.grid(row=4,column=2)

        txtservicecharge=Entry(f1,font=("arial" , 16,"bold"), textvariable=Service_charge , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtservicecharge.grid(row=4,column=3)

        lblchanabhatura = Label(f1,font=("arial" , 16,"bold"), text="Total Cost" , bd=16, anchor = "w")

        lblchanabhatura.grid(row=4,column=0)

        txtchanabhatura=Entry(f1,font=("arial" , 16,"bold"), textvariable=Total , bd=10, insertwidth=4,bg="powder blue", justify ="right")

        txtchanabhatura.grid(row=4,column=1)


        #------------------------------------Buttons---------------------------------------------------#

        btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=0,text="Total",bg="green3",command=Ref).grid(row=5,column=1)

        btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=0,text="Reset",bg="firebrick1",command=Reset).grid(row=5,column=2)

        btnQuit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=0,text="Quit",bg="magenta2",command=Exit).grid(row=5,column=3)

        btnPrice=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=0,text="Price",bg="red2",command=price).grid(row=5,column=0)

        btnSave=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=0,text="Save and Exit",bg="blue3",command=Save).grid(row=6,column=1)       

        
        root.mainloop()

        

    c=raw_input("Do you want to continue?(y/n)")
