from gooey import Gooey, GooeyParser
@Gooey(program_name="Tamrin 1",
       program_description = "To Store 4 Number",
       default_size=(700, 400))
def main():
    parser = GooeyParser()
    parser.add_argument("Number_1", help="PLZ Enter a Number")
    parser.add_argument("Number_2", help="PLZ Enter a Number")
    parser.add_argument("Number_3", help="PLZ Enter a Number")
    parser.add_argument("Number_4", help="PLZ Enter a Number")
    args = parser.parse_args()
    with open("database1.txt", "w") as f:
        f.write(args.Number_1)
        f.write("\n")
        f.write(args.Number_2)
        f.write("\n")
        f.write(args.Number_3)
        f.write("\n")
        f.write(args.Number_4)
    with open("database1.txt", "r") as g:
        file = g.read().split("\n")
    for i in (file) :
        i = int(i)
        if i % 2 == 0 :
            print (f"{i}    zoj ast")
        else :
            print (f"{i}    fard ast")
main()