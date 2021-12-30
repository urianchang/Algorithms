from stack import Stack


# Determine if brackets are balanced
def is_match(ch1, ch2):
    if ch1 == "(" and ch2 == ")":
        return True
    elif ch1 == "{" and ch2 == "}":
        return True
    elif ch1 == "[" and ch2 == "]":
        return True 
    else:
        return False


def is_balanced(text):
    s = Stack()
    is_balanced = True
    idx = 0

    while idx < len(text) and is_balanced:
        ch = text[idx]
        if ch in "([{":
            s.push(ch)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, ch):
                    is_balanced = False 
                    break
        idx += 1

    if s.is_empty() and is_balanced:
        return True
    return False


assert is_balanced("(((({}))))") is True
assert is_balanced("[][]]]") is False
assert is_balanced("[][]") is True
assert is_balanced("))") is False


# Reverse string
def reverse_string(text):
    s = Stack()
    for ch in text:
        s.push(ch)
    
    rev = ""
    while not s.is_empty():
        rev += s.pop()

    return rev

assert reverse_string("hello") == "olleh"


# Convert decimal integer to binary
def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return "0"

    s = Stack()
    while dec_num > 0:
        s.push(dec_num % 2)
        dec_num = dec_num // 2
        
    bstring = ""
    while not s.is_empty():
        bstring += str(s.pop())
    
    return bstring

assert convert_int_to_bin(74) == "1001010"
assert convert_int_to_bin(25) == "11001"
assert convert_int_to_bin(26) == "11010"
assert convert_int_to_bin(94) == "1011110"
