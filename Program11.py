

def DivisibleByThreeAndFive(iValue):
    if((iValue % 3 == 0) and (iValue % 5 == 0)):
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