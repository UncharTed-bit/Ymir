from gooey import Gooey, GooeyParser
@Gooey(program_name="Tamrin 6",
       program_description = "Login",
       default_size=(500, 500))
def main():
    parser = GooeyParser()
    parser.add_argument("Name" , help="PLZ Enter Your Name, First Letter Is Capital")
    parser.add_argument("Last_Name" , help="PLZ Enter Your Last Name, First Letter Is Capital")
    args = parser.parse_args()
    with open("database6.txt", "r") as g:
        file = g.read()
    if args.Name in file and args.Last_Name in file :
        print("Login Successfully")
    else : 
        print("Login Failed")
main()