#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_size = len(sys.argv) - 1
    arg_list = sys.argv

    if arg_size == 0:
        print("0 arguements.")
    elif arg_size == 1:
        print("{} argument:\n{}: {}".format(arg_size, arg_size, arg_list[1]))
    else:
        print("{} arguments:".format(arg_size))
        for i, arg in enumerate(arg_list[1:]):
            print("{}: {}".format(i+1, arg))
