
def DisplayFactors(iValue):
    print("Factors of "+str(iValue)+"are : ")
    for i in range(1,int(iValue/2)+1,1):
        if(iValue % i == 0):
            print(i,end = "\t")


def main():
    print("Enter number : ")
    iNo = int(input())

    DisplayFactors(iNo)

if __name__ == "__main__":
    main()