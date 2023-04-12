#Template : Problems on Digits

def Reverse(iValue):
    iCnt = 0
    iRev = 0
    while(iValue != 0):
        iDigit = iValue % 10
        iRev = (iRev*10) + iDigit
        iValue = int(iValue / 10)

    return iRev
   

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = Reverse(iNo)
    print("Reversed Number is : ",Ret)

if __name__ == "__main__":
    main()