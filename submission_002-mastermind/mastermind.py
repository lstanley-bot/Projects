import random


def run_game():
#step 1
    c_list = ["0", "0", "0", "0"]

    for i in range(0, len(c_list)):
        random_c_list = random.randint(1, 8)
        while random_c_list in c_list:
            random_c_list = random.randint(1, 8)
        c_list[i] = random_c_list
    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    
    
#step 2
    number_tries = 12
    
    while number_tries != 0:
        user_input = input("Input 4 digit code: ")
        
        while (user_input.isdigit() == False
               or len(user_input) < 4 
               or len(user_input) > 4
               or "0" in user_input
               or "9" in user_input):
            
            print("Please enter exactly 4 digits.")
            user_input = input("Input 4 digit code: ")
        
        user_input_list = list(user_input)

#step 3

        correct_i = 0
        incorrect_i = 0
        for i in range(0, len(c_list)):
            if c_list[i] == int(user_input_list[i]):
                correct_i += 1
            elif int(user_input_list[i]) in c_list:
                incorrect_i += 1
            else:
                i += 1
        print("Number of correct digits in correct place:    ", correct_i)
        print("Number of correct digits not in correct place:", incorrect_i)
        
        if correct_i == 4:
            print("Congratulations! You are a codebreaker!")
            print("The code was: ", end="")
            for i in range(0, len(c_list)):
                print(c_list[i], end="")
            print()
            break
        elif correct_i != 4:
            number_tries -= 1
            print("Turns left:", number_tries)
            
        if number_tries == 0:
            print("The code was: ", end="")    
            for i in range(0, len(c_list)):
                print(c_list[i], end="")
            print()
            break
    

if __name__ == "__main__":
    run_game()
