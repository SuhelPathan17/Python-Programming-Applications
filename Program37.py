
def SumNonFactors(iValue):
    iSum = 0
    for i in range(1,iValue,1):
        if((iValue % i) != 0):
            iSum = iSum + i
    return iSum

def main():
    print("Enter number : ")
    iNo = int(input())

    Ret = SumNonFactors(iNo)
    print("Summation of Non-Factors is : ",Ret)

if __name__ == "__main__":
    main()