import random


# TODO: Decompose into functions
def run_game():
    correct = False
    turns = 0

    code = get_code()
    check_code(correct, turns, code)


def get_code(): 
    '''
    randomly chooses 4 digits between 1 and 8
    '''
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code


def get_user_input():
    '''
    gets the users input of 4 digits and runs in a loop
    '''
    valid = False
    while not valid:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
        else:
            valid = True
    return answer


def check_code(correct, turns, code):
    '''
    diplays the number of tries and deciments them
    it also checks to see if the digits are in its correct place and if its not
    '''
    while not correct and turns < 12:
        answer = get_user_input()
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: '+str(code))



if __name__ == "__main__":
    run_game()