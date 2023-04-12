
def SumFactors(iValue):
    iSum = 0
    for i in range(1,int(iValue/2)+1,1):
        if(iValue % i == 0):
            iSum = iSum + i
    
    return iSum

def CheckPerfect(number):
    iRet = SumFactors(number)

    if(iRet == number):
        return True
    else:
        return False

def main():
    print("Enter number : ")
    iNo = int(input())

    bRet = CheckPerfect(iNo)
    if(bRet == True):
        print(str(iNo)+" is Perfect Number")
    else:
        print(str(iNo)+" is not Perfect Number")
if __name__ == "__main__":
    main()