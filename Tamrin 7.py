import math
from datetime import datetime
from gooey import Gooey, GooeyParser
@Gooey(program_name="Tamrin 7",
       program_description = "Advanced Calculater",
       default_size=(500, 500))
def main():
    parser = GooeyParser()
    parser.add_argument("number" , help="PLZ Enter a Number")
    parser.add_argument("selections" , choices= ["factorial" , "sqrt" , "exponent"] , widget= 'Dropdown',)
    args = parser.parse_args()
    with open("database7.txt", "w") as g:
        g.write(args.selections)
        g.write(" ")
        g.write(str(datetime.now()))
    if args.selections == "factorial" :
        if int(args.number) <= 0:
            print("Sorry, factorial does not exist for negative numbers")
        else:
            result = math.factorial(int(args.number))
            print(f"The factorial of {args.number} is : {result}")
    elif args.selections == "sqrt" :
        result = math.sqrt(int(args.number))
        print(f"The sqrt of {args.number} is : {result}")
    elif args.selections == "exponent" :
        result = (int(args.number))**2
        print(f"The exponent of {args.number} is : {result}")
main()