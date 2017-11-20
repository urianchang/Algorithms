"""
Lists

Initialize your list and read in the value of n followed by n lines of
commands where each command will be of the 7 types listed above. Iterate
through each command in order and perform the corresponding operation
on your list.
"""

if __name__ == '__main__':
    L = []
    for _ in xrange(int(raw_input())):
        cmd = raw_input().strip().split(' ')
        if cmd[0] == "insert":
            L.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print L
        elif cmd[0] == "remove":
            if int(cmd[1]) not in L:
                continue
            else:
                L.remove(int(cmd[1]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort()
        elif cmd[0] == "pop":
            L.pop()
        elif cmd[0] == "reverse":
            L.reverse()
