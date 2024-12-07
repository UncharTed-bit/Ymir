from collections import Counter 
from gooey import Gooey, GooeyParser
@Gooey(program_name="Tamrin 4",
       program_description = "To Uppercase and Lowercase",
       default_size=(700, 400))
def main():
    parser = GooeyParser()
    parser.add_argument("Your_Input", help="PLZ Enter an Statement")
    args = parser.parse_args()
    print(args.Your_Input.swapcase())
    for i in (args.Your_Input) :
        count = Counter(args.Your_Input)
        print( i , count[i] )
main()