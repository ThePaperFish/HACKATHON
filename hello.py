def banner():
    print('-----' *18)
    print('\t' *3, "South City Plaza Apartment")
    print('-----' *18)
    
def type_banner():
    a = """ Apartment Type A
           - 2 bedrooms and equipped with kitchen and laundry
           - Monthly rental is RM300 per room """
    b = """ Apartment Type B
           - 3 bedrooms including one master bedroom with attached bedroom
           - No kitchen and laundry facilities
           - Monthly rental is RM200 for normal room and RM280 for master room """
    print(a, b, sep='\n')

def banner(Type):
    if Type == 0:
        print('-----' *18)
        print('\t' *3, "South City Plaza Apartment")
        print('-----' *18)
        print('\n')
        
    if Type == 1:
        a = """ Apartment Type A
               - 2 bedrooms and equiped with kitchen and laundry
               - Monthly rental is RM300 per room """
        b = """ Apartment Type B
               - 3 bedrooms including one master bedroom with attached bedroom
               - No kitchen and laundry facilities
               - Monthly rental is RM200 with normal room and additional 40% for master room """
        print(a, b, sep='\n')
        print('\n')

    if Type == 2:
        print ("Welcome!")
        
banner(0)
banner(1)

username = input("Please enter your username  : ")
password = input("Please enter your password  : ")

if username.equals("user1") and password.equals("user1") :
    banner(2)
