def outline_pyramid(height):
    k = 0
    for i in range(1, height+0):
        for j in range(i, height):
            print(" ", end="")
        while(k != (2 * i - 1)):
            if (k == 0 or k == 2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        k = 0
        print("")
    for i in range(0, 2 * height - 1):
        print("*", end="")
    print()
outline_pyramid(5)


def outline_diamond(height):
    k = 0
    for i in range(1, height+1):
        for j in range(1, height-i+1):
            print(" ", end="")
        while(k != (2 * i - 1)):
            if(k == 0 or k == 2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        k = 0
        print("")
    height = height - 1
    for i in range(height, 0, -1):
        for j in range(0, height-i+1):
            print(" ", end="")
        k = 0
        while(k != (2 * i - 1)):
            if(k == 0 or k == 2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        print("")
outline_diamond(5)


def outline_square(height):
    for i in range(1, height + 1):
        if(i == 1 or i == height):
            for j in range(1, height + 1):
                print("*", end="")
        else:
            for j in range(1, height + 1):
                if (j == 1 or j == height):
                    print("*", end="")
                else:
                    print(end=" ")
        print("") 
outline_square(5)


def outline_rhombus(height):
    for i in range(1, height + 1):
        for j in range(1, height-i+1):
            print(end=" ")
        if i == 1 or i == height:
           for j in range(1, height+1):
               print("*", end="")
        else:
            for j in range(1, height+1):
                if j == 1 or j == height:
                    print("*", end="")
                else:
                    print(end=" ")
        print("")
outline_rhombus(5) 


def outline_triangle(height):
    for i in range(height):
        for j in range(i + 1):
            if i == height - 1 or j == 0 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
outline_triangle(5)

def outline_hourglass(height):  
    height = height - 1
    for i in range(0, 2 * height - 1):
        print("*", end="")
    print("")
    for i in range(height, 1, -1):
        for j in range(1, height-i+1):
            print(" ",end="")
        k = 0
        while(k != (2 * i - 1)):
            if(k == 0 or k == 2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        print("")
    k = 0
    for i in range(1, height+1):
        for j in range(1, height-i+1):
            print(" ", end="")
        while(k != (2 * i - 1)):
            if (k == 0 or k == 2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        k = 0
        print("")
    for i in range(0, 2 * height - 1):
        print("*", end="")
    print()
outline_hourglass(5)