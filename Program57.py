#Template : Problems on Digits

def DisplayEvenOddDigits(iValue):
   iEvenCnt = 0
   iOddCnt = 0
   iDigit = 0
   if(iValue == 0):        #Filter
       iEvenCnt = iEvenCnt + 1
       
   if(iValue < 0):         #Updater
       iValue = -iValue

   while(iValue != 0):
       iDigit = iValue % 10

       if(iDigit % 2 == 0):
           iEvenCnt = iEvenCnt + 1
       else:
           iOddCnt = iOddCnt + 1

       iValue = int(iValue/10)
   
   print("Even Count of Digits is : ",iEvenCnt)
   print("Odd Count of Digits is : ",iOddCnt)

def main():
    print("Enter Number : ")
    iNo = int(input())

    DisplayEvenOddDigits(iNo)
    

if __name__ == "__main__":
    main()