from random import randint

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
        print("1:" , "Login ")
        print("2:" , "Register ")
    
    if Type == "Fuckoff":
        print ("Welcome!",Data)

    print()

def U_login(username,password):
    if username == "" or password == "" :
        
        while randint(0,1000) != 100:
            print("FUCK YOU", '\n')
            
    if username == "1" and password == "1" :
        banner("Fuckoff",username)
    
        
banner("start")
banner("rooms")
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




