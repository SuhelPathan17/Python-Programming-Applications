#Template : Problems on Digits

def CountEvenDigits(iValue):
   iCnt = 0
   iDigit = 0
   if(iValue == 0):        #Filter
       return 1
   if(iValue < 0):         #Updater
       iValue = -iValue

   while(iValue != 0):
       iDigit = iValue % 10

       if(iDigit % 2 == 0):
           iCnt = iCnt + 1

       iValue = int(iValue/10)
   return iCnt

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = CountEvenDigits(iNo)
    print("No. of Digits are : ",Ret)

if __name__ == "__main__":
    main()