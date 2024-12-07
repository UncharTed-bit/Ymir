from gooey import Gooey, GooeyParser
@Gooey(program_name="Tamrin 9",
       program_description = "Length and Weight Converter",
       default_size=(500, 500))
def main():
    parser = GooeyParser()
    parser.add_argument("Length" , help="PLZ enter Length in Meter")
    parser.add_argument("selections_1" , choices= ["km" , "cm" , "mm"] , widget= 'Dropdown',)
    parser.add_argument("Weight" , help="PLZ Enter Weight in Kg")
    parser.add_argument("selections_2" , choices= ["ton" , "gr" , "mgr" ] , widget= 'Dropdown',)
    args = parser.parse_args()
    
    if args.selections_1 == "km" :
        print (f"Length is {int(args.Weight) / 1000} km")
    elif args.selections_1 == "cm" :
        print (f"Length is {int(args.Weight) * 100} cm")
    elif args.selections_1 == "mm" :
        print (f"Length is {int(args.Weight) * 1000} mm")
    if args.selections_2 == "ton" :
        print (f"Weight is {int(args.Weight) / 1000} ton")
    elif args.selections_2 == "gr" :
        print (f"Weight is {int(args.Weight) * 1000} gr")
    elif args.selections_2 == "mgr" :
        print (f"Weight is {int(args.Weight) * 1000000} mgr")
main()