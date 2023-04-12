
def DivisibleByFive(iValue1):
    iAns = iValue1 % 5
    if(iAns != 0):
        return 0
    else:
        return 1
    

    

def main():
    print("Enter First number : ")
    iNo1 = int(input())

    iRet = DivisibleByFive(iNo1)
    if(iRet == 1):
        print( str(iNo1)+" is divisible by 5")
    else:
        print( str(iNo1)+" is not divisible by 5")
    

if __name__ == "__main__":
    main()