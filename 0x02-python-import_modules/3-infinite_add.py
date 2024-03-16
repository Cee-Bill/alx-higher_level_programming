#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    arg_list = sys.argv[1:]
    my_output = 0

    if arg_len == 0:
        print(my_output)
    elif arg_len == 1:
        my_output = int(arg_list[1])
        print(my_output)
    else:
        for x in arg_list:
            my_output += int(x)
        print(my_output)
