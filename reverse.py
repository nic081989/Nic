# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Nicholas Ngobi
# ASSIGNMENT:   Project 2: Stacks & Queue

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    return q_new
def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()
