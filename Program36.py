
def DisplayNonFactors(iValue):
    print("Non-Factors of "+str(iValue)+" are : ")
    for i in range(1,iValue,1):
        if((iValue % i) != 0):
            print(i,end = "\t")


def main():
    print("Enter number : ")
    iNo = int(input())

    DisplayNonFactors(iNo)

if __name__ == "__main__":
    main()