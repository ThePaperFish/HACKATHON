
def banner(Type):
    if Type == 0:
        print('-----' *18)
        print('\t' *3, "South City Plaza Apartment")
        print('-----' *18)
        
    if Type == 1:
        a = """ Apartment Type A
               - 2 bedrooms and equiped with kitchen and laundry
               - Monthly rental is RM300 per room """
        b = """ Apartment Type B
               - 3 bedrooms including one master bedroom with attached bedroom
               - No kitchen and laundry facilities
               - Monthly rental is RM200 with normal room and additional 40% for master room """
        print(a, b, sep='\n')

    if Type == 2:
        print("1:" , "Login ")
        print("2:" , "Register ")
    
    if Type == 3:
        print ("Welcome!")

    print()
        
banner(0)
banner(1)
banner(2)

M_option = input("Please select an option   :")

if M_option.isnumeric():
    
    M_option = int(M_option)
    
    if M_option == 1:
        username = input("Please enter your username  : ")
        password = input("Please enter your password  : ")

    
else:
    
    if "help" in M_option:
        banner(4)




