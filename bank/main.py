import sqlite3

conn=sqlite3.connect("Bank.db") # to create a data base

cursor=conn.cursor() #cursor will be used to write and execute code 



def acc_creation(name,phone,dob,address,addhar,gender,acc_type):
    cursor.execute(f"insert into Acoount(name,phone,aadhar,dob,gender,address,acc_type,amount) values('{name}',{phone},{addhar},'{dob}','{gender}','{address}','{acc_type}',500)")

    conn.commit()
    print("acc created success fully")
    
    

def pin_gen(acc,pin,c_pin):
    
    #! used to get all the db data as an obj
    
    # data=cursor.execute(f"select * from Acoount where acc_no={acc}")
    
    #! used to fetch one row data fully
    
    # result=data.fetchone()
    
    if(pin==c_pin):
        cursor.execute(f"update Acoount set pin={pin} where acc_no={acc} ")
        conn.commit()
    else:
        print("pin and c pin are not matching")
    
    
def balance(acc,pin):
    data=cursor.execute(f"select * from Acoount where acc_no={acc}")
    result=data.fetchone()
    
    
    if(pin==result[-3]):
        print(f"balance is {result[-2]}")
        
        
    else:
        print("invalid pin")
        
        
    
def withdraw(acc,pin):
     
     data=cursor.execute(f"select * from Acoount where acc_no={acc}")
     result=data.fetchone()
     
     
     if(pin==result[-3]):
        withdraw=int(input("enter the withdraw ammount"))
        print(f"balance is {result[-2]}")
        if(withdraw<result[-2]):
            amm=result[-2]-withdraw
            cursor.execute(f"update Acoount set amount={amm} where acc_no={acc} ")
            conn.commit()
            print(f"remaining balance is {amm}")
         
         
        else:
            print("you dont have that much try a smaller amount")
        
        
     else:
        print("invalid pin")
     
     
         
def deposit(acc,pin):
     
     data=cursor.execute(f"select * from Acoount where acc_no={acc}")
     result=data.fetchone()
     
     if(pin==result[-3]):
         deposit=int(input("enter the deposit ammount"))

         if(deposit>0 and deposit<=100000):
             amm=result[-2]+deposit
             cursor.execute(f"update Acoount set amount={amm} where acc_no={acc} ")


             conn.commit()

             print(f"balance is {amm}")

         else:
             print("enter a valid ammount")
         
     else:
         print("invalid pin")
     
    
def acc_transfer(from_acc,to_acc,pin):
    data=cursor.execute(f"select * from Acoount where acc_no={from_acc}")
    result=data.fetchone()
    if(pin==result[-3]):
        trancfer_amm=int(input("enter the ammount of transfer"))
        if(trancfer_amm<result[-2]):
            amm=result[-2]-trancfer_amm
            cursor.execute(f"update Acoount set amount={amm} where acc_no={from_acc} ")
            conn.commit()
            print(f"remaining balance is {amm}")
        
            data1=cursor.execute(f"select * from Acoount where acc_no={to_acc}")
            to_account=data1.fetchone()
            to=to_account[-2]+trancfer_amm
        
            cursor.execute(f"update Acoount set amount={to} where acc_no={to_acc} ")
            conn.commit()
        
        
    else:
        print("invalid pin")

     
user_input=int(input('''
1. acc creation         
2.pin generation
3.balance         
4.withdrawl
5.deposit
6.acc transfer
         
         '''))





if user_input==1:
    print("thanks for jo bhi hai wahi ")
    name=input('naam bata apna ')
    dob=input(" kab tapka dharti pe ??")
    phone=int(input("chal num bata maamu "))
    add=input("rehta kidhar hai be ??")
    aadhar=int(input("addahr no "))
    gender=input("ladka / ladki ")
    acc_type=input("tera type bata chal ( account ka )")
    acc_creation(name,phone,dob,add,aadhar,gender,acc_type)



if user_input==2:
    acc=int(input("enter acc number"))
    pin=int(input('enter your new pin'))
    c_pin=int(input("confirm your pin"))
    pin_gen(acc,pin,c_pin)

if user_input==3:
    acc=int(input("enter acc number"))
    pin=int(input('enter your pin'))
    balance(acc,pin)

if user_input==4:
    acc=int(input("enter acc number"))
    pin=int(input('enter your pin'))
    
    withdraw(acc,pin)
    
    
if user_input==5:
    acc=int(input("enter acc number"))
    pin=int(input('enter your pin'))
    
    deposit(acc,pin)
    
if user_input==6:
    from_acc=int(input("enter senders acc number"))
    to_acc=int(input("enter receivers acc number"))

    pin=int(input('enter your pin'))
    acc_transfer(from_acc,to_acc,pin)