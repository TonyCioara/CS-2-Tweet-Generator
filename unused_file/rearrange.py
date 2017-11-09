import sys
import random


def rearrange(my_list):

    # Rearrange list into a new list in a random order;
    new_list = []
    while 0 < len(my_list):
        rand_num = random.randint(0, len(my_list) - 1)
        to_append = my_list.pop(rand_num)
        new_list.append(to_append)

    # Return list
    return new_list


def print_func(list):
    # Prints list in 1 line
    to_print = " ".join(list)
    print(to_print)


if __name__ == "__main__":
    current_input = sys.argv[1:]
    new_list = rearrange(current_input)
    print_func(new_list)
