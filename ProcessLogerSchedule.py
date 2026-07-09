import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return 

    else:
        os.mkdir(FolderName)
        print("Directory for logfiles created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print(FileName)

    fobj = open(FileName,"w")

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

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        # Wait till abort
        print("Platform Surveillence System Started Sucessfully")
        print("Directory created with name : ",sys.argv[2])
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