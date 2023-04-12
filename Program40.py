
def DisplayReverse(iValue):
    iCnt = iValue
    while(iCnt != 0):
        print(iCnt,end = "\t")
        iCnt = iCnt - 1
        


def main():
    print("Enter number : ")
    iNo = int(input())

    DisplayReverse(iNo)

if __name__ == "__main__":
    main()