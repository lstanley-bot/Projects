def pyramid(n): 
    for  i in range(1, n+1):
        for j in range(1, n):
            print(" ", end="")
        n =  n - 1
        for j in range(0, 2*i-1):
            print("*", end="")
        print("")    
pyramid(10)
