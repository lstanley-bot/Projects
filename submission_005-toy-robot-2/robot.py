
def robot_start():
    """This is the entry function, do not change"""

    directions = 'starting point'
    x = 0
    y = 0
    name = name_robot()
    power = True
    while power == True:
        get_command = command_input(name)
        power, x, y, directions = command(name, get_command, directions, x, y)


def name_robot():
    '''
    gets the name of the robot from the kid
    '''
    name = input("What do you want to name your robot? ").upper()
    print(name + ": Hello kiddo!")
    return name


def command_input(name):
    '''
    gets the command input from the on what the robot should do
    '''
    get_command = input(name+": What must I do next? ").lower()
    return get_command


def command(name, get_command, directions, x, y):
    '''
    calls all the movement functions including help and off
    prints out the position of robot
    '''
    power = True
    while power == True:
        # get_command = input(name+": What must I do next? ").lower()
        if get_command.lower() == "off":
            off_command(name, get_command)
            power = False
            continue

        elif "forward" in get_command.lower():
            x , y = forward_movements(name, get_command, x, y, directions)
            print(f" > {name} now at position ({x},{y}).")
            break

        elif "back" in get_command.lower():
            x , y = back_movements(name, get_command, x, y, directions)
            print(f" > {name} now at position ({x},{y}).")
            break

        elif "right" in get_command.lower():
            # print(directions)
            directions = handle_command(get_command, directions)
            right_movements(name, get_command, x, y)
            break

        elif "left" in get_command.lower():
            directions = handle_command(get_command, directions)
            left_movements(name, get_command, x, y)
            break

        elif "sprint" in get_command.lower():
            x , y = sprint_movements(name, get_command, x, y, directions)
            print(f" > {name} now at position ({x},{y}).")
            break

        elif get_command.lower() == "help":
            print(get_help())
            break
            
        else:
            print(name+": Sorry, I did not understand '"+get_command.capitalize()+"'.")
            # get_command = command_input(name)
            break
    return power , x, y, directions


def off_command(name, get_command):
    '''
    shuts the robot off by making power = False
    '''
    power = True
    while power == True:
        if get_command.lower() == "off":
            print(name + ": Shutting down..")
            power = False
            continue
    return "ROB: Shutting down.."


def get_help():
    '''
    prints out the help command to display what the robot can do
    '''
    help_robot = "I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\n"
    return help_robot


def forward_movements(name, get_command, x, y, directions):
    '''
    handles all the forward commands for robot
    inclueds the safe zone for the robot
    prints out the the movement of the robot
    '''
    steps = get_command.split()
    if len(steps) != 2:
        print(name+": Sorry, I did not understand '"+get_command+"'.")
    else:
        steps_x_y = steps[1]
        if directions == 'starting point':
            if y + int(steps_x_y) > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
            
                y += int(steps[1])

        elif directions == 'right':
            if x + int(steps_x_y) > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")

                x += int(steps[1])
              
        elif directions == 'left':
            if x - int(steps_x_y) < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")

                x -= int(steps[1])
        else:
            directions == 'back'
            if y - int(steps_x_y) < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")

                y -= int(steps[1])
    return x , y


def back_movements(name, get_command, x, y, directions):
    '''
    handles all the back commands for robot
    inclueds the safe zone for the robot
    prints out the the movement of the robot
    '''
    steps = get_command.split()
    if len(steps) != 2:
        print(name+": Sorry, I did not understand '"+get_command+"'.")
        get_command = input(name+": What must I do next? ")
    else:
        steps_x_y = steps[1]
        if directions == 'starting point':
            if y - int(steps_x_y) < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                y -= int(steps[1])

        elif directions == 'right':
            if x - int(steps_x_y) < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")

                x -= int(steps[1])

        elif directions == 'left':
            if x + int(steps_x_y) > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")

                x += int(steps[1])
        else:
            directions == 'back'
            if y + int(steps_x_y) > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")

                y += int(steps[1])
    return x , y


def right_movements(name,get_command, x, y):
    '''
    controls the right movement
    displays it turned
    prints out the position
    '''
    if get_command == 'right':
        print(f" > {name} turned {get_command}.")
        print(f" > {name} now at position ({x},{y}).")
    return x , y
    

def left_movements(name, get_command, x, y):
    '''
    controls the left movement
    displays it turned
    prints out the position
    '''
    if get_command == 'left':
        print(f" > {name} turned {get_command}.")
        print(f" > {name} now at position ({x},{y}).")
    return x , y


def sprint_movements(name, get_command, x, y, directions):
    '''
    controls the sprint movement of the robot by means of recursion
    '''
    steps = get_command.split()
    if len(steps) != 2:
        print(name+": Sorry, I did not understand '"+get_command+"'.")
    else:
        if steps[1] != "0":
            x , y = forward_movements(name,"forward "+ str(steps[1]), x, y, directions)
            get_command = "sprint " + str(steps[1])
            x , y = sprint_movements(name,steps[0] +" "+ str(int(steps[1]) -1), x, y, directions)
    return x,y 


def handle_command(get_command, directions):
    '''
    lets the robot know in which direction it is by using logic
    '''
    if get_command == 'right' and directions == 'starting point':
        directions = 'right'
    elif get_command == 'right' and directions == 'right':
        directions = 'back'
    elif get_command == 'right' and directions == 'back':
        directions = 'left'
    elif get_command == 'right' and directions == 'left':
        directions = 'starting point'
    elif get_command == 'left' and directions == 'starting point':
        directions = 'left'
    elif get_command == 'left' and directions == 'left':
        directions = 'back'
    elif get_command == 'left' and directions == 'back':
        directions = 'right'
    elif get_command == 'left' and directions == 'right':
        directions = 'starting point'
    # print(directions)
    return directions



if __name__ == "__main__":
    robot_start()

