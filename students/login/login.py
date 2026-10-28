import json
def login():
    try:
        
    
        email=input("please enter the email:")
        password=input("please enter the password:")
        with open("task.json","r") as file:
            data=json.load(file)
        for i in data:    
            if i["email"]==email and i["password"]==password:
                print("login succesfully") 
                return       
        
            else:
                print("email or password not match:")
                break
    except Exception as e:
        print("error is ",e)    
        
