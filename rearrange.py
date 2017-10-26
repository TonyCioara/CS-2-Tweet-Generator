import sys
import random
current_input = sys.argv


def rearrange(my_list):
    # Delete first word;
    my_list.pop(0)

    # Rearrange list into a new list in a random order;
    new_list = []
    index = 0
    while index < len(my_list):
        rand_num = random.randint(0, len(my_list) - 1)
        new_list.append(my_list[rand_num])
        my_list.pop(rand_num)
    print(new_list)


rearrange(current_input)
