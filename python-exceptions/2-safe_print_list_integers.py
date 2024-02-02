#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in my_list:
            if type(element) == int:
                if element <= x:
                    print("{:d}".format(element), end="")
                    count += 1
        print()
        return (count)

    except Exception as e:
        print(f"{e}")
        return (count)
