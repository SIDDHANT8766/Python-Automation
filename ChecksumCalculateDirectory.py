import hashlib
import os

def CalculateChechsum(FileName):
    fobj = open(FileName,"rb") #

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()


def DirectoryWatcher(DirctoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirctoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirctoryName)

    if(Ret == False):
        print("It is not a folder")
        return 


    for FolderName , SubFolderName, FileName in os.walk(DirctoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Ckecksum = CalculateChechsum(fname)
            print(f"File name :{fname} Ckechsum : {Ckecksum}")


def main():

    DirectoryWatcher()

if __name__ == "__main__":
    main()