from colorama import Fore , Back , Style
def zarb(var_1 , var_2) :
    list = []
    for i in range(1 , var_1+1):
        for j in range (1, var_2+1):
            if i == j == 2 :
                continue
            elif i == 4 or j == 4 :
                print(Fore.RED + "" , i*j , end = " ")
                list.append(i*j)
            else :
                print(Fore.YELLOW + "" , i*j , end = " " + Style.RESET_ALL)
                list.append(i*j)
        print()
    return(list)
var_1 = int(input("plz enter num 1 : "))
var_2 = int(input("plz enter num 2 : "))
list_even = []
if 6 <= var_1 <= 10 and 6 <= var_2 <= 10 :
    var_res = zarb(var_1 , var_2)
    for i in var_res:
        if i % 2 == 0 :
            list_even.append(i)
else :
    print("invalid input")
print(list_even)