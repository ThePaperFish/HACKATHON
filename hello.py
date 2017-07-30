def small(numa,numb):
    dif = abs(numa - numb)
    sumab = numa + numb
    return((sumab -dif)/2)

def smallest(amount):
    if (amount == 0):
        return num[0]
    else:
        return small(smallest(amount -1),num[amount])

num = []
temp1 = 0
temp = input("Enter Number " + str(len(num) +1) + " : ")

while (temp.isdigit()):
    num.append(temp)
    temp = input("Enter Number " + str(len(num) +1) + " : ")

num = [int(s) for s in num]

print(smallest(len(num)-1))
