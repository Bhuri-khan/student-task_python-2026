import json
def search():
    try:
 
        with open("task.json","r")as file:
            data=json.load(file)
        name = input("please enter the name:") 
        for i in data:

            if i["name"].lower() == name.lower():
                print("Name: ",i["name"])
                print("Age: ",i["age"])
                print("Qualification: ",i["qualification"])
                print("Email: ",i["email"])
                print("Password: ",i["password"])
                return
            else:        
    
                print("data is not found")
                break
        else:
            print("please enter the signup student") 
    
    except Exception as e:
        print("error is ",e)
