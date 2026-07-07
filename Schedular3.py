import time
import datetime
import schedule    # 3rd party

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def main():
    print("Inside Marvellous AutomationScript at : ",datetime.datetime.now())

    schedule.every(20).seconds.do(fun)     

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()