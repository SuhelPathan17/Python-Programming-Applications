
def DisplayEvenFactors(iValue):
    print("Ever Factors are : ")
    for i in range(1,int(iValue/2)+1,1):
        if((iValue % i == 0) and (i % 2 == 0)):
            print(i,end="\t")

def main():
    print("Enter Number : ")
    iNo = int(input())

    DisplayEvenFactors(iNo)

if __name__ == "__main__":
    main()