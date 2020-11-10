

import random


def create_outline():
    print("Course Topics:")

    course = set(["Introduction to Python",
             "Tools of the Trade",
             "How to make decisions",
             "How to repeat code",
             "How to structure data",
             "Functions",
             "Modules"])

    course = list(course)
    course = sorted(course)
    for topics in course:
        print("* "+ topics)
    
    print("Problems: ")


    course_problems = {"Introduction to Python" : ["Problem 1", "Problem 2", "Problem 3"],
             "Tools of the Trade" : ["Problem 1", "Problem 2", "Problem 3"],
            "How to make decisions" : ["Problem 1", "Problem 2", "Problem 3"],
            "How to repeat code" : ["Problem 1", "Problem 2", "Problem 3"],
            "How to structure data" : ["Problem 1", "Problem 2", "Problem 3"],
            "Functions" : ["Problem 1", "Problem 2", "Problem 3"],
            "Modules" : ["Problem 1", "Problem 2", "Problem 3"]
            }

    names = ["Azria", "Ashleigh", "Tyra", "Courtney", "Karen"]
    
    status = ["[STARTED]", "[GRADED]", "[COMPLETED]"]
    
    problem = ["Problem 1", "Problem 2", "Problem 3"]
    
    students_list = [( "1.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , status[0]),
                    ( "2.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , status[0]),
                    ( "3.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , status[1]),
                    ( "4.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , status[2]),
                    ( "5.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , status[2]),
                    ]

    for i in course:
        print(f"* {i} : " ,end ="")
        for problem in course_problems[i]:
            if problem == "Problem 3":
                print(f"{problem} " ,end ="")
            else:
                print(f"{problem}, " ,end ="")
        print()


    print("Student Progress:")
    for i in range(0,5):
        for j in range(0,7):
            print(students_list[i][j], end=" ")
        print()

if __name__ == "__main__":
    create_outline()
