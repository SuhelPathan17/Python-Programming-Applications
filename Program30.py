
def Factorial(iValue):
    iFact = 1
    for i in range(1,iValue+1,1):
        iFact = iFact * i

    return iFact

def main():
    print("Enter No : ")
    iNo = int(input())

    Ret = Factorial(iNo)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()