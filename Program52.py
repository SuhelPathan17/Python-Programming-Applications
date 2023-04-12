#Template : Problems on Digits

def SumDigits(iValue):
   iSum = 0
   iDigit = 0
   while(iValue > 0):
       iDigit = iValue % 10
       iSum = iSum + iDigit
       iValue = int(iValue/10)
   return iSum

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = SumDigits(iNo)
    print("Sum of Digits are : ",Ret)

if __name__ == "__main__":
    main()