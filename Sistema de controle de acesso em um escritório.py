cargo = input("writte your work position: ")

if cargo == "CEO": 
    print ("access granted.")
elif cargo == "Analyst":
    day = input ("enter the week day: ")
    if day == "Saturday":
        print("Sorry, access denied")
    elif day == "Sunday":
        print("Sorry, access denied")
    else: 
        print("Access granted")
