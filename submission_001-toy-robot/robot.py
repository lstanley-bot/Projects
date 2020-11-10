

# TODO: Decompose into functions

def move():
    '''
    move_robot
    '''
    size = 10
    width = 10
    length = 20
    
    move_square(size)
    move_rectangle(length, width)
    move_circle()
    move_square_dancing(length)
    move_crop_circles(length)


def move_square(size):
    '''
    moves robot in a square within a degree of 90
    size is defined as a parameter
    '''
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length, width):
    '''
    moves robot in a rectangle within a degree of 90
    length and width is defined as a parameter
    '''
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle():
    '''
    moves robot in a circle within 360 degrees
    '''
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def move_square_dancing(length):
    '''
    makes robot dance in a square motion
    length is defined as a parameter
    '''
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(length)
   
        
def move_crop_circles(length):
    '''
    makes robot move in 4 circles
    length is defined as a parameter
    '''
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()



def robot_start():
    move()


if __name__ == "__main__":

    robot_start()