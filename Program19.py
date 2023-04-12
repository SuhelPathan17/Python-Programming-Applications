def Display(iValue):
    iCnt = 1
    while(iCnt <= iValue):
        print("Jay Ganesh...")
        iCnt = iCnt + 1
        
def main():
    print("Enter Number of Iterations : ")
    iNo = int(input())
    Display(iNo)

if __name__ == "__main__":
    main()