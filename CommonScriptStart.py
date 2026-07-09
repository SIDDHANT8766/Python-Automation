import sys
import os
import time
import schedule

def fun(DirName):
    pass


def main(): 

    Border = "-"*50
    print(Border)
    print("---------- Marvellous Data Shield System ---------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated file")
            print("3 : Create an archive of backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeIntervel : The time in miniuts for periodic scheduling")
            print("SourceDirectory : Name of directory to packed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please refer --u or --h for more details")

    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval :",sys.argv[1])
        print("Dictionary name :",sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])

        # Wait till abort
        print("Data Shield System Started Sucessfully")
        print("Time interval :",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalide number of commandline arguments")
        print("Unable to proced as there is no such option")
        print("Please refer --u or --h for more details")


    print(Border)
    print("--------- Thank you fro using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()