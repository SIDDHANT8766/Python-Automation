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


def FindDuplicate(DirctoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirctoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirctoryName)

    if(Ret == False):
        print("It is not a folder")
        return 
    
    Duplicate = {}


    for FolderName , SubFolderName, FileName in os.walk(DirctoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Ckecksum = CalculateChechsum(fname)

            if(Ckecksum in Duplicate):
                Duplicate[Ckecksum].append(fname)
            else:
                Duplicate[Ckecksum]= [fname]

    return Duplicate

def DisplayResult(MyDict):

    Result = list(filter(lambda x : len(x) > 1 ,MyDict.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        
        print("Value of count is :",Count)
        Count = 0


def DeleteDuplicate(Path = "Marvellous"):

    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1 ,MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted file :",subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1

        Count = 0

    print("Total deleted file :",Cnt)

def main():

    DeleteDuplicate()

if __name__ == "__main__":
    main()