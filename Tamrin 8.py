from math import factorial
def fac(var_1):
    if int(var_1) <= 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        result = factorial(int(var_1))
        print(f"The factorial of {var_1} is : {result}")
        return (result)
vorodi = fac(int(input("plz input a number : ")))
def zyf(var_2):
    if var_2 % 2 == 0 :
        print("bazi adad tasadofi")
    else :
        print("mashin hesab")
zyf(vorodi)