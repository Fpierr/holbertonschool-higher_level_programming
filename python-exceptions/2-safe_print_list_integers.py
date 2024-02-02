#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            element =  my_list[i]
            if type(element) == int:
                print("{:d}".format(element), end="")
                count += 1
        print()
        return (count)

    except IndexError as e:
        print("IndexError: {}".format(e))
