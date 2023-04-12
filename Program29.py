def Summation(iValue):
    iSum = 0

    for i in range(10,iValue+10,10):
        iSum = iSum + i

    return iSum
    

def main():
    print("Enter Number")
    iNo = int(input())
    Ret = Summation(iNo)
    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()