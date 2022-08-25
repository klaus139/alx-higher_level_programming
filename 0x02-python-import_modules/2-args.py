#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.srgv) - 1
    if srgc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
