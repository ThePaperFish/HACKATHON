

def banner(Type,Data = ""):
    if Type == "start":
        print('-----' *18)
        print('\t' *3, "South City Plaza Apartment")
        print('-----' *18)
        
    if Type == "rooms":
        a = """ Apartment Type A
               - 2 bedrooms and equiped with kitchen and laundry
               - Monthly rental is RM300 per room """
        b = """ Apartment Type B
               - 3 bedrooms including one master bedroom with attached bedroom
               - No kitchen and laundry facilities
               - Monthly rental is RM200 with normal room and additional 40% for master room """
        print(a, b, sep='\n')

    if Type == "menu":
        print("\t-- Main Menu --")
        print()
        print("\t1:" , "Login ")
        print("\t2:" , "Register ")

    if Type == "U_menu":
        print("\t-- User Menu --")
        print()
        print("\t1:" , "Book Accommodation ")
        print("\t2:" , "View Booking")
        print("\t3:" , "Payment ")
        print("\t4:" , "Cancel Booking")
        print("\t5:" , "Back")
    
    if Type == "Fuckoff":
        print ("Welcome!",Data)

    print()

def U_login(username,password):
    if username == "" or password == "" :

        print("\tPlease enter a vaild username or/ password")
            
    if username == "1" and password == "1" :
        banner("Fuckoff",username)
        banner("U_menu")       
        M_option = input("\tPlease select an option   :")
        print()

        if M_option.isnumeric():
        
            M_option = int(M_option)
            
            if M_option == 5:
                menu()

def menu():     
    banner("menu")   
    M_option = input("Please select an option   :")
    print()
    M_option = M_option.lower()

    if M_option.isnumeric():
        
        M_option = int(M_option)
        
        if M_option == 1:
            username = input("Please enter your username  : ")
            password = input("Please enter your password  : ")
            print()

            U_login(username,password)
    else:
        
        if "help" in M_option:
            banner(4)
        
banner("start")
banner("rooms")

menu()




