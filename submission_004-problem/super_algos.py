
def find_min(element):
    """TODO: complete for Step 1"""
    '''
    returns -1 if i isn't and int or if the list is empty
    returns -1 when the length of the element is less than 1
    using recursion to find the min value
    '''
    for i in element:
        if type(i) != int or i == "":
            return -1
    if len(element) < 1:
        return -1
    if (len(element) == 1):
        return element[0]
    if element[0] < element[1]:
        element[1] = element[0]
    return find_min(element[1:])


def sum_all(element):
    """TODO: complete for Step 2"""
    '''
    returns -1 if i isn't and int or if the list is empty
    returns -1 when the length of the element is less than 1
    using recursion to sum up the list
    '''
    for i in element:
        if type(i) != int or i == "":
            return -1
    if len(element) < 1:
        return -1
    if (len(element) == 1):
        return element[0]
    if (len(element) != 1):
        element[1] = element[0] + element[1]
    return sum_all(element[1:])



def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    '''
    returns an empty list if i isn't and int or if the list is empty
    returns an empty list when the length of the element is less than 1
    returns the charater set if n = 1
    returns an empty list if the length of the character set is more than one
    uses recursion to find the possible strings
    '''
    for i in character_set:
        if type(i) == int or i == "":
            return []
    if len(character_set) < 1:
        return []
    if n == 1:
        return character_set
    elif len(character_set) > 1:
        new_list = []
        for i in character_set:
            for j in find_possible_strings(character_set, n-1):
                new_list.append(i + j)
    return new_list


# if __name__ == '__main__':

#     element = [9, 5, 7, 2, 3]
#     print(find_min(element))
#     element = [-1,-2,-3]
#     print(sum_all(element))
#     character_set = ["o", "k"]
#     print(find_possible_strings(character_set, 2))