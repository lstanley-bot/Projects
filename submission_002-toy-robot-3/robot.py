"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""
import re
# from re import split
# from typing import ContextManager, Counter
# from os import name


# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint']
valid_arguments = ['reversed', 'silent', '']

# creating an empty list to record the history
record = []

# flags
silent = False
reversed = False

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()
        

def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ')
    if len(args) == 3:
        return args[0], args[1], args[2]
    elif len(args) == 2:
        return args[0], args[1], ''
    return args[0], '', ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1,arg2) = split_command_input(command)
    command_split = split_command_input(command)
    for i in command_split:
        regex_pattern = '|'.join(map(re.escape, ',.'))
        if '-' in i:
            split_arg = i.split('-')
            if split_arg[0].isdigit() == True and split_arg[1].isdigit() == True:
                return True
            else:
                return False
        elif len(re.split(regex_pattern, i, 0)) != 1:
            return False
    
    return (command_name.lower() in valid_commands) and (len(arg1) >= 0
    and is_int(arg1) or arg1.lower() in valid_arguments) and (len(arg2) >= 0 
    and is_int(arg2) or arg2.lower() in valid_arguments)
    

def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def robot_history(command):
    global record
    command = str(command)
    split_command = command.split()
    if 'help' not in split_command and 'replay' not in split_command:
        record.append(command)
        # print(command)
    return command


def robot_replay(robot_name, commands):
    global record
    range_flag, range_list = range_replay(commands)
    if range_flag == True and range_list == []:
        for i in record:
            handle_command(robot_name, i)
        print(f' > {robot_name} replayed {len(record)} commands.')
    else:
        if len(range_list) == 1:
            counter = 0
            range_single = range_list[0]
            for i in record[-range_single:]:
                handle_command(robot_name, i)
                if counter == range_single:
                    break
                else:
                    counter += 1
            print(f' > {robot_name} replayed {counter} commands.')
      
        elif len(range_list) == 2 and '-' in commands:
            r1 = range_list[0]
            r2 = range_list[1]
            counter = 0
            for i in record[-r1 : -r2]:
                handle_command(robot_name, i)
            print(f' > {robot_name} replayed {len(record[-r1:-r2])} commands.')

def robot_replay_silent(robot_name, commands):
    global record, silent
    range_flags, range_list = range_replay(commands)
    if range_flags == True and range_list == []:
        for i in record:
            handle_command(robot_name, i)
        print(f' > {robot_name} replayed {len(record)} commands silently.')
    
    else:
        if len(range_list) == 1:
            counter = 0
            range_single = range_list[0]
            for i in record[-range_single:]:
                handle_command(robot_name, i)
                # print(i)
                if counter == range_single:
                    break
                else:
                    counter += 1
            print(f' > {robot_name} replayed {(counter)} commands silently.')
      
        elif len(range_list) == 2 and '-' in commands:
            r1 = range_list[0]
            r2 = range_list[1]
            counter = 0
            for i in record[-r1 : -r2]:
                counter += 1
                handle_command(robot_name, i)
            print(f' > {robot_name} replayed {len(record[-r1:-r2])} commands silently.')

    silent = False


def robot_replay_reverse(robot_name, commands):
    global record, reversed
    reversed_list = record[::-1]
    range_flag, range_list = range_replay(commands)
    if range_flag == True and range_list ==[]:
        for i in record[::-1]:
            handle_command(robot_name, i)
        print(f' > {robot_name} replayed {len(record)} commands in reverse.')
      # show_position(robot_name)
    else:
        if len(range_list) == 1:
            counter = 0
            range_single = range_list[0]
            for i in reversed_list[-range_single:]:
                counter += 1
                handle_command(robot_name, i)
            print(f" > {robot_name} replayed {counter} commands in reverse.")
        
        elif len(range_list) == 2 and '-' in commands:
            r1 = range_list[0]
            r2 = range_list[1]
            counter = 1
            for i in reversed_list[-r1:]:
                handle_command(robot_name, i)
                if counter == r2:
                    break
                else:
                    counter += 1
            print(f" > {robot_name} replayed {len(record[-r1:-r2])} commands in reverse.")

    reversed = False


def robot_replay_reverse_silent(robot_name, commands):
    global record, silent, reversed
    reversed_list = record[::-1]
    range_flag, range_list = range_replay(commands)
    if range_flag == True and range_list == []:
        for i in record[::-1]:
            handle_command(robot_name, i)
        print(f' > {robot_name} replayed {len(record)} commands in reverse silently.')
    # show_position(robot_name)
    else:
        if len(range_list) == 1:
            counter = 0 
            range_single = range_list[0]
            for i in reversed_list[-range_single:]:
                counter+=1
                handle_command(robot_name, i)
            print(f" > {robot_name} replayed {counter} commands in reverse silently.")

        elif len(range_list) == 2 and '-' in commands:
            r1 = range_list[0]
            r2 = range_list[1]
            counter = 1
            for i in reversed_list[-r1:]:
                handle_command(robot_name, i)
                if counter == r2:
                    break
                else:
                    counter += 1
            print(f" > {robot_name} replayed {len(record[-r1:-r2])} commands in reverse silently.")

    silent = False
    reversed = False


def range_replay(commands):
    split_command = commands.split()
    for i in range(len(split_command)):
        if split_command[i] in valid_commands or split_command[i] in valid_arguments:
            i+=1
            
            if i == len(split_command):
                return True,[]
        
        elif split_command[i].isdigit() or '-' in split_command[i]:
        
            if split_command[i].isdigit():
                return True,[int(split_command[i])]

            split_range = split_command[i].split('-')
            if len(split_range) == 2 and split_range[0].isdigit() and split_range[1].isdigit():
                return True, [int(split_range[0]),int(split_range[1])]
        else:
            return False,[]


def replay_commands(robot_name, command):
    global silent, reversed
    if 'replay' in command and 'silent' not in command and 'reversed' not in command:
        robot_replay(robot_name, command)
    elif 'replay' in command and 'silent' in command and 'reversed' not in command:
        silent = True
        robot_replay_silent(robot_name, command)
    elif 'replay' in command and 'silent' not in command and 'reversed' in command:
        reversed = True
        robot_replay_reverse(robot_name, command)
    elif 'replay' in command and 'silent' in command and 'reversed' in command:
        silent = True
        reversed = True
        robot_replay_reverse_silent(robot_name, command)


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global silent, reversed

    (command_name, arg, arg1) = split_command_input(command)
    do_next = True

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        replay_commands(robot_name, command)
        
    if silent == True:
        return do_next
    elif 'replay' in command:
        show_position(robot_name)
    else:
        print(command_output)
        show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, record, silent, reversed

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    record = []

    silent = False
    reversed = False

    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        robot_history(command)
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
