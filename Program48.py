#Template : Problems on Digits

def CountDigits(iValue):
   iCnt = 0
   iDigit = 0
   while(iValue > 0):
       iCnt = iCnt + 1
       iValue = int(iValue/10)
   return iCnt

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = CountDigits(iNo)
    print("No. of Digits are : ",Ret)

if __name__ == "__main__":
    main()