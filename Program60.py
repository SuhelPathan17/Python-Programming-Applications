#Template : Problems on Digits

def CheckPalindrom(iValue):
    iCnt = 0
    iRev = 0
    iTemp = iValue
    while(iValue != 0):
        iDigit = iValue % 10
        iRev = (iRev*10) + iDigit
        iValue = int(iValue / 10)

    return (iRev == iTemp)
   

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = CheckPalindrom(iNo)
    if(Ret == True):
        print("It is a palindrome number")
    else:
        print("It is not a palindrome number")


if __name__ == "__main__":
    main()