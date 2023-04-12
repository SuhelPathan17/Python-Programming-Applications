
def DisplayTable(iValue):
    print("Table of "+str(iValue)+" is : ")
    for i in range(1,11,1):
            print(iValue*i,end = "\t")


def main():
    print("Enter number : ")
    iNo = int(input())

    DisplayTable(iNo)

if __name__ == "__main__":
    main()