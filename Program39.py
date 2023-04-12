
def DisplayReverse(iValue):
    for i in range(iValue,0,-1):
            print(i,end = "\t")


def main():
    print("Enter number : ")
    iNo = int(input())

    DisplayReverse(iNo)

if __name__ == "__main__":
    main()