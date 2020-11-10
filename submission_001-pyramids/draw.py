

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    user_input = input("Shape?: ")
    while user_input.lower() not in ['pyramid', 'triangle', 'square', 'diamond', 'rhombus', 'hourglass']:
        #print("Invalid Shape!")
        user_input = input("Shape?: ")
    return user_input.lower()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = 82
    while height > 81:
        try:
            height = int(input("Height?: "))
        except ValueError:
            height = 82
    return height


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        for r in range(1, height+1):
            for c in range(1, height):
                print(" ", end="")
            height = height - 1
            for j in range(0, 2 * r - 1):
                print("*", end="")
            print("")
    if outline == True:
        k = 0
        for r in range(1, height+0):
            for c in range(r, height):
                print(" ", end="")
            while(k != (2 * r - 1)):
                if (k == 0 or k == 2 * r - 2):
                    print("*", end="")
                else:
                    print(" ", end="")
                k = k + 1
            k = 0
            print("")
        for r in range(0, 2 * height - 1):
            print("*", end="")
        print("")
       

# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        for r in range(0, height):
            for c in range(0, height):
                print("*", end="")
            print("")
    if outline == True:
        for r in range(1, height + 1):
            if(r == 1 or r == height):
                for c in range(1, height + 1):
                    print("*", end="")
            else:
                for c in range(1, height + 1):
                    if (c == 1 or c == height):
                        print("*", end="")
                    else:
                        print(end=" ")
            print("")      


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for r in range(0, height):
            for c in range(0, r+1):
                print("*", end="")
            print("")
    if outline == True:
        for r in range(height):
            for c in range(r + 1):
                if r == height - 1 or c == 0 or c == r:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")       

       
#Extra shape 1
def draw_diamond(height, outline):
    if outline == False:
        k = height - 1
        for r in range(0, height):
            for c in range(0, k):
                print(end=" ")
            k = k - 1
            for c in range(0 , r + 1):
                print("* ", end="")
            print("")
        k = height
        for r in range(height , -1, -1):
            for c in range(height, k):
                print(end=" ")
            k = k + 1
            for c in range(0 , r + 1 - 1):
                print("* ", end="")
            print("")
    if outline == True:
        k = 0
        for r in range(1, height + 1):
            for c in range(1, height - r + 1):
                print(" ", end="")
            while(k != (2 * r - 1)):
                if(k == 0 or k == 2 * r - 2):
                    print("*", end="")
                else:
                    print(" ", end="")
                k = k + 1
            k = 0
            print("")
        height = height - 1
        for r in range(height, 0, -1):
            for c in range(0, height - r + 1):
                print(" ", end="")
            k = 0
            while(k != (2 * r - 1)):
                if(k == 0 or k == 2 * r - 2):
                    print("*", end="")
                else:
                    print(" ", end="")
                k = k + 1
            print("")

#Extra shape 2
def draw_rhombus(height, outline):
    if outline == False:
        for r in range(1, height+1):
            for c in range(1, height - r + 1):
                print(end=" ")
            for c in range(1, height + 1):
                print("*", end="")
            print("") 
    if outline == True:
        for r in range(1, height + 1):
            for c in range(1, height-r+1):
                print(end=" ")
            if r == 1 or r == height:
                for c in range(1, height+1):
                    print("*", end="")
            else:
                for c in range(1, height+1):
                    if c == 1 or c == height:
                        print("*", end="")
                    else:
                        print(end=" ")
            print("")

#Extra shape 3
def draw_hourglass(height, outline):
    if outline == False:
        k = height 
        for r in range(height, 0, -1):
            for c in range(k , height , -1):
                print(end=" ")
            k = k + 1
            for c in range(0, r):
                print("* ", end="")
            print("")
        k = height - 1
        for r in range(0, height):
            for c in range(0 , k):
                print(end=" ")
            k = 1 * k - 1
            for c in range(0, r + 1):
                print("* ", end="")
            print("")
    if outline == True:
        height = height - 1
        for r in range(0, 2 * height - 1):
            print("*", end="")
        print("")
        for r in range(height, 1, -1):
            for c in range(1, height-r+1):
                print(" ",end="")
            k = 0
            while(k != (2 * r - 1)):
                if(k == 0 or k == 2 * r - 2):
                    print("*", end="")
                else:
                    print(" ", end="")
                k = k + 1
            print("")
        k = 0
        for r in range(1, height+1):
            for c in range(1, height-r+1):
                print(" ", end="")
            while(k != (2 * r - 1)):
                if (k == 0 or k == 2 * r - 2):
                    print("*", end="")
                else:
                    print(" ", end="")
                k = k + 1
            k = 0
            print("")
        for r in range(0, 2 * height - 1):
            print("*", end="")
        print("")


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'diamond':
        draw_diamond(height, outline)
    elif shape == 'rhombus':
        draw_rhombus(height, outline)
    elif shape == 'hourglass':
        draw_hourglass(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    get_input = input("Outline only? (y/N): ")
    if get_input == "y" or get_input == "Y":
        return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

