<<<<<<< HEAD
def banner(Type):
    if Type == 0:
        print('-----' *18)
        print('\t' *3, "South City Plaza Apartment")
        print('-----' *18)

banner(0) # 0 is start
=======
def banner():
    print('-----' *18)
    print('\t' *3, "South City Plaza Apartment")
    print('-----' *18)
    
def type_banner():
    a = """ Apartment Type A
           - 2 bedrooms and equiped with kitchen and laundry
           - Monthly rental is RM300 per room """
    b = """ Apartment Type B
           - 3 bedrooms including one master bedroom with attached bedroom
           - No kitchen and laundry facilities
           - Monthly rental is RM200 with normal room and additional 40% for master room """
    print(a, b, sep='\n')

banner()
type_banner()
>>>>>>> bddb69d51d109eb5841c8961fcb4921fd95868c1
number_a = int(input())
number_b = int(input())
