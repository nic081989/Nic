# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         FIXME
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
#def test_matcher_fail_mix6():
    #assert matcher("{[(})") == False

    # s=[{]
    # char = {

# YOU CAN DO IT NICK WE BELIEVE IN YOU


def matcher(str):
    s = Stack([])
    ope=["(","[","{"] # 1-parens, 2-( square)bracket, 3- curly brace
    clo=[")", "]","}"]
    for char in str:
        if char in ope:
            s.push(char)
        elif char in clo:
            if s.is_empty():
                return False
            top= s.pop()  
        if (char==")" and top!="(") or (char=="]" and top!="[")or (char=="{" and top!="{"):
                return False
    return s.is_empty()

def main():

    print("matcher: ", matcher("[()]"))


# Don't run main on import
if __name__ == "__main__":
    main()

