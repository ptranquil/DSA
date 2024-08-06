def recursion(n):
    while(n!=0):
        print("Recusion!!")
        n-=1
        return recursion(n)

if __name__ == "__main__":
    recursion(10)