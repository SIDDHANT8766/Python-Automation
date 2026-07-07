# python CommandLine4.py  11  21 

import sys

def main():

    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    print(No1 + No2)   # 32

    #for i in range(len(sys.argv)):
     #   print(sys.argv[i])
      #  print(int(sys.argv[1]) + (sys.argv[2]))
        


if __name__ == "__main__":
    main()