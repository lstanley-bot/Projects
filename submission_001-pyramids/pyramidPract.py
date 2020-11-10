def pyramid(n):
    k = 2 * n 
    for  i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1 
        for j in range(0, i+1):
            print("*", end=" ")
        print("")    
pyramid(5) 

def triangle(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end="")
        print("")
triangle(5)

def square(n):
    k = 1 * n - 1
    for i in range(0, n):
        for j in range(0, k + 1):
            print("*", end="")
        print("")
square(5)         

def diamond(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0 , i + 1):
            print("* ", end="")
        print("")
    k = 1 * n - 1
    for i in range(n , -1 , -1):
        for j in range(0, k):
            print(end=" ")
        k = k + 1
        for j in range(0 , i + 1 - 1):
            print("* ", end="")
        print("")
diamond(5)

def hourglass(n):
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k , 0 , -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
    k = 2 * n - 2
    for i in range(0, n+1):
        for j in range(0 , k):
            print(end=" ")
        k = 1 * k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
hourglass(5)

def rhombus(height):
    for i in range(1, height+1):
        for j in range(1, height - i + 1):
            print(end=" ")
        for j in range(1, height + 1):
            print("*", end="")
        print("")
rhombus(5)

