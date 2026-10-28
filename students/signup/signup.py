import json
import datetime

with open("students/data/task.json","r") as file:
    data=json.load(file)

def signup():
    
    dictionary={}   
    try:
        while True:
            name = input("please enter the name:")
            if len(name)>2:
                if name.isalpha():
                    break
                    
                else:
                    with open("students/logs/errors.log",'a') as file_name:
                        file_name.write(f"[{str(datetime.datetime.now())}] [ERROR] - Name - invalid your name \n")
                    print("Invalid Your Name")
            else:
                with open("studnets/logs/errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Name -  Minimum 2 Character \n")
                print("Invalid Name")
        
    except Exception as e:
        print("error e",e)                
    
    try:    
        while True:
            
            age = input("please enter the age:")
            if len(age)>=0:
                if age.isdigit():
                    break
                else:
                    with open("students/logs/errors.log",'a') as file:
                        file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Age - Invalid Your Age\n")
                    print("Invalid Your Age")
            else:
                with open("students/logs/errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Age - Please Age 0 to Greater\n")
                print("Please Age 0 to Greater")
    except Exception as e:
        print("error is ",e)                
    try:
        qualification = []
        
        while True:
            qualification = input("please enter the quaifctaion: ")
        
            q = input("Enter Qualification (close karne ke liye no likho): ")
            if q.lower() == "no":
                break
            qualification.append(q)                                                                             
            dictionary["qualification"] = qualification
    except ValueError:
        print("error ",e)
                            
                           
                        # with open("students/logs/errors.log",'a') as file:
                        #     file.write(f"[{str(datetime.datetime.now())}] [ERROR] - qualification - Invalid Your Qualification \n")
                        # print("Invalid Your Qualification")  
        
                          
        while True:
                 
            address=input("Enter Address: ")
            if len(address)>4:
                if address.isalpha():
                    break
                else:
                    print("Invalid Your Address")
            else:        
                with open("students/logs/errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - address - Invalid Your Address \n")
                print("Invalid address")
        
    except Exception as e:
        print("error ",e)            
                
    try:            
        while True:
            email=input("Enter Email ID: ")
            if len(email)>6:
                if "@" in email and ".com" in email:
                    break
                else:
                    print("Invalid Your Email ID")
            else:
                with open("students/logs/errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - email - Invalid Your    Email \n")
                print("Invalid email")
    except Exception as e:
        print("error ",e)     
            
    try:        
        while True:
            password=input("Enter Password: ")
            if len(password)>5:
                if password.isalnum():
                    break
                else:
                    print("Invalid Your Password")
            else:
                print("Please 6 character password try again")
                
                with open("students/logs/errors.log",'a') as file:
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
    data.append(dictionary)          
    with open("students/data/task.json","w") as file:
       
        json.dump(data,file,indent=4)
    print("data save succesfully")
