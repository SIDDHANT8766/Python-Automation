# CommandLine Input

import psutil
import sys

def main():
    Border = "-"*50
    print(Border)
    print("----- Marvellous Platform Surveillence System ----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Create automatic logs")
            print("2 : Execute periodically")
            print("3 : Sends mail with the log")
            print("4 : Store the infornamtion sbout processes")
            print("5 : Store information about CPU")
            print("6 : Stror information about RAM usage")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeIntervel : The time in miniuts for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please refer --u or --h for more details")

    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval :",sys.argv[1])
        print("Dictionary name :",sys.argv[2])

    else:
        print("Invalide number of commandline arguments")
        print("Unable to proced as there is no such option")
        print("Please refer --u or --h for more details")


    print(Border)
    print("--------- Thank you fro using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()