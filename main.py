from students.signup.signup import signup 
from students.login.login import login
from students.search.search import search
from students.auth.auth import auth
# from studnets.validation.validation import validation


# dictionary={}

def menu():
    
    while True:
        print("1. signup")
        print("2. login")
        print("3. search")
        print("4.authontication")
        print("5. exit")
    
        choice=int(input("please enter the choice:"))
        if choice ==1:
            signup()
        elif choice ==2:
            login()
        elif choice==3:
            search()
        elif choice==4:
            auth() 
        elif choice==5:
            print("exit")    
            break 
        else:
            print("invalid")                  
            
menu()            