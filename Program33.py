
def SumFactors(iValue):
    iSum = 0
    for i in range(1,int(iValue/2)+1,1):
        if(iValue % i == 0):
            iSum = iSum + i
    
    return iSum

def main():
    print("Enter number : ")
    iNo = int(input())

    iRet = SumFactors(iNo)
    print("Summation of factors is : ",iRet)
if __name__ == "__main__":
    main()