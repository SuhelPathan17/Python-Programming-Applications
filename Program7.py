
def Multiplication(iValue1, iValue2):
    iAns = iValue1 * iValue2
    return iAns

    

def main():
    print("Enter First number : ")
    iNo1 = int(input())

    print("Enter Second number : ")
    iNo2 = int(input())

    iRet = Multiplication(iNo1,iNo2)
    print("Multiplication is : ",iRet)

if __name__ == "__main__":
    main()