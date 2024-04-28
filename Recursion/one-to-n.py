if __name__ == '__main__':
    n=10
    start=1
    def oneToN(start):
        if(start > n):
            return
        else:
            print(start)
            start+=1
            return oneToN(start)
    
    oneToN(start)