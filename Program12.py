

def DivisibleByThreeAndFive(iValue):
    iAns1 = iValue % 3
    iAns2 = iValue % 5
    if((iAns1 == 0) and (iAns2 == 0)):
        return True
    else:
        return False

def main():
    print("Enter Number : ")
    iNo = int(input())

    Ret = DivisibleByThreeAndFive(iNo)
    if(Ret == True):
        print(str(iNo)+" is Divisible by 3 & 5")
    else:
        print(str(iNo)+" is not Divisible by 3 & 5")


if __name__ == "__main__":
    main()