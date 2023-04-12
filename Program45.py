
def DisplayOddFactors(iValue):
    print("Ever Factors are : ")
    for i in range(1,int(iValue/2)+1,2):
        if((iValue % i == 0)):
            print(i,end="\t")

def main():
    print("Enter Number : ")
    iNo = int(input())

    DisplayOddFactors(iNo)

if __name__ == "__main__":
    main()