# Demonstration of Sequance


def Display(iValue):
    iCnt = 1
    while(iCnt<=iValue):
        print(iCnt)
        iCnt = iCnt + 1
        
def main():
   print("Enter number of Iterations : ")
   iNo = int(input())
   Display(iNo)

if __name__ == "__main__":
    main()