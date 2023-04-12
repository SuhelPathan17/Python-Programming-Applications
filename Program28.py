def Summation():
    iSum = 0

    for i in range(10,60,10):
        iSum = iSum + i

    return iSum
    

def main():
    Ret = Summation()
    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()