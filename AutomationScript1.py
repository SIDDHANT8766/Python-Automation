import sys

def main():
    Border = "-"*40
    print(Border)
    print("-------- Marvellos Automation ----------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform ____")
            print("This is a automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : ______")
            print("Argument2 : ______")

        else:
            # print("Unmached Command Line arguments")
            print("Use the given flags as :")
            print("--u : Used to display the usage")
            print("--h : Used to display the help")
            
    else:
        print("Invalid number of Command Line arguments")
        print("Use the given flags as :")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)
    print("------- Thank you for using script -----")
    print("--------- Marvellos Infosystems --------")
    print(Border)


if __name__ == "__main__":
    main()