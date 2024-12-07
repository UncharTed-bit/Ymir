from gooey import Gooey, GooeyParser
@Gooey(program_name="Tamrin 2",
       program_description = "Name + LastName + Calculate",
       default_size=(500, 500))
def main():
    parser = GooeyParser()
    parser.add_argument("Name" , help="PLZ Enter Your Name, First Letter Is Capital")
    parser.add_argument("Last_Name" , help="PLZ Enter Your Last Name, First Letter Is Capital")
    parser.add_argument("Num_1" , help="PLZ Enter Number 1")
    parser.add_argument("Num_2" , help="PLZ Enter Number 2")
    parser.add_argument("selections" , choices= ["+" , "-" , "*" , "/"] , widget= 'Dropdown',)
    args = parser.parse_args()
    with open("database2.txt", "r") as g:
        file = g.read()
    if args.Name in file and args.Last_Name in file and len(args.Num_1) == 2 and len(args.Num_2) == 2 :
        if args.selections == "+" :
            print (int(args.Num_1) + int(args.Num_2))
        elif args.selections == "-" :
            print (int(args.Num_1) - int(args.Num_2))
        elif args.selections == "*" :
            print (int(args.Num_1) * int(args.Num_2))
        elif args.selections == "/" :
            print (int(args.Num_1) / int(args.Num_2))
    else : 
        print("Error")
main()