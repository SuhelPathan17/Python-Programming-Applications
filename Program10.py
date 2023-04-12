
def DivisibleByFive(iValue1):
    iAns = iValue1 % 5
    if(iAns == 0):
        return True
    else:
        return False
    

    

def main():
    print("Enter First number : ")
    iNo1 = int(input())

    Ret = DivisibleByFive(iNo1)
    if(Ret == True):
        print( str(iNo1)+" is divisible by 5")
    else:
        print( str(iNo1)+" is not divisible by 5")
    

if __name__ == "__main__":
    main()