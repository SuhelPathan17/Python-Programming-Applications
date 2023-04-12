#Template : Problems on Digits

def SumDigits(iValue):
   iSum = 0

   if(iValue < 0):
       iValue = -iValue
       
   while(iValue > 0):
       
       iSum = iSum + (iValue % 10)
       iValue = int(iValue/10)
   return iSum

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = SumDigits(iNo)
    print("Sum of Digits are : ",Ret)

if __name__ == "__main__":
    main()