import datetime
import json
dictionary={}
with open("task.json","r") as file:
    data=json.load(file)
 
def validation():
    try:
    
        while True:
            name = input("please enter the name:")
            if len(name)>2:
                if name.isalpha():
                    break
                    
                else:
                    with open("errors.log",'a') as file_name:
                        file_name.write(f"[{str(datetime.datetime.now())}] [ERROR] - Name - invalid your name \n")
                    print("Invalid Your Name")
            else:
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Name -  Minimum 2 Character \n")
                print("Invalid Name")
        
                    
    
        
        while True:
            
            age = input("please enter the age:")
            if len(age)>0:
                if age.isdigit():
                    break
                else:
                    with open("errors.log",'a') as file:
                        file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Age - Invalid Your Age\n")
                    print("Invalid Your Age")
            else:
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Age - Please Age 0 to Greater\n")
                print("Please Age 0 to Greater")

        while True:       
              
            qualifications = []
            qualification = input("Enter Qualification: ")
            qualifications.append(qualification)
    
            choice = input("Add qualificatio (yes/no): ")
    
            if choice.lower() != "yes":
                break
    
            print("Your Qualifications:")
            
            for q in qualifications:
                print(q)
    
                qualification=input("Enter Qualification: ")
                if len(qualification)>1:
                    if qualification.isalnum():
                        break
                    else:           
                        with open("errors.log",'a') as file:
                            file.write(f"[{str(datetime.datetime.now())}] [ERROR] - qualification - Invalid Your Qualification \n")
                        print("Invalid Your Qualification")  
        
                          
        while True:
                 
            address=input("Enter Address: ")
            if len(address)>4:
                if address.isalpha():
                    break
                else:
                    print("Invalid Your Address")
            else:        
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - address - Invalid Your Address \n")
                print("Invalid address")
        
                
                
                
        while True:
            email=input("Enter Email ID: ")
            if len(email)>6:
                if "@" in email and ".com" in email:
                    break
                else:
                    print("Invalid Your Email ID")
            else:
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - email - Invalid Your    Email \n")
                print("Invalid email")
         
            
            
        while True:
            password=input("Enter Password: ")
            if len(password)>5:
                if password.isalnum():
                    break
                else:
                    print("Invalid Your Password")
            else:
                print("Please 6 character password try again")
                
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - password - Invalid Your Password \n")
                print("Invalid password")
        
        date_time=datetime.datetime.now()
        dictionary={
            "name":name,
            "age":age,
            "qualification":qualification,
            "email":email,
            "password":password,
            "date_time":str(date_time)
        }
    
    except Exception as e :
        print("error is",e)
                            
        with open("task.json","w") as file:
            data.append(dictionary)
            json.dump(data,file,indent=4)
        print("data save succesfully")