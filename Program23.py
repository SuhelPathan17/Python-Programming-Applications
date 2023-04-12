# Demonstration of Sequance


def Display(iValue):
    for i in range(1,iValue+1,1):
        print(i)
        
def main():
   print("Enter number of Iterations : ")
   iNo = int(input())
   Display(iNo)

if __name__ == "__main__":
    main()