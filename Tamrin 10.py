from gooey import Gooey, GooeyParser
@Gooey(program_name="Tamrin 10",
       program_description = "Text + Count",
       default_size=(500, 500))
def main():
    parser = GooeyParser()
    parser.add_argument("text" , help="PLZ Enter Your Text Here")
    parser.add_argument("selections" , choices= ["a" , "b" , "c" , "d" , "e" , "f" ,
                                                 "g" , "h" , "i" , "j" , "k" , "l" ,
                                                 "m" , "n" , "o" , "p" , "q" , "r" ,
                                                 "s" , "t" , "u" , "v" , "w" , "x" ,
                                                 "y" , "z" ] , widget= 'Dropdown')
    args = parser.parse_args()
    print(args.text.count(args.selections))
main()