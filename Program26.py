def Summation():
    iNo1 = 10
    iNo2 = 20
    iNo3 = 30
    iNo4 = 40
    iNo5 = 50

    iSum = 0
    iSum = iSum + iNo1
    iSum = iSum + iNo2
    iSum = iSum + iNo3
    iSum = iSum + iNo4
    iSum = iSum + iNo5

    return iSum

def main():
    Ret = Summation()
    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()