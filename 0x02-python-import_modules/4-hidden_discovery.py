#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for x in sorted(dir(hidden_4)):
        if x[:2] != '__':
            print("{}".format(x))
