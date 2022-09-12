from doctest import OutputChecker
from turtle import pos
from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

# a Number needs to be able to be evaluated if it's a negative, a float, or an int
def is_Num_(charr):
    try:
        int(charr)
    except:
        raise PostfixFormatException("Invalid token")
    else:
        return isinstance(int(charr), int)

def is_Operand_(charr):
    if charr in ["+", "-", "*", "**", "^", "/", "<<", ">>"]:
        return True
    else:
        return False

def is_Float_(charr):
    if "." in charr:
        return True
    else:
        return False

def test_input_operands_num(in_str):
    res = in_str.split()
    operand_cnt = 0
    operators_cnt = 0
    for i in res:
        if is_Operand_(i): # it actually is checking if it's an operator
            print("Should be operator:", i)
            operators_cnt += 1
        elif is_Float_(i):
            print("Should be operand:", i)
            operand_cnt += 1
        elif is_Num_(i):
            print("Should be operand:", i)
            operand_cnt += 1
    if operators_cnt > operand_cnt - 1:
        raise PostfixFormatException("Insufficient operands")        
    if operators_cnt < operand_cnt - 1:
        raise PostfixFormatException("Too many operands")
    print("operand_cnt: ", operand_cnt)
    print("operators_cnt: ", operators_cnt)

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    # to account for stacks sizes larger than a certain amount

    test_input_operands_num(input_str)

    my_stack = Stack(2*len(input_str))
    input_str = input_str.split()
    for i in input_str: 
        if is_Operand_(i):
            try:
                y = my_stack.pop()  # this is popped first
                x = my_stack.pop()  # this is the value that precedes it
            except:
                raise PostfixFormatException("Insufficient operands")
            if i == "+":
                my_stack.push(x + y)
            elif i == ">>":
                my_stack.push(x >> y)
            elif i == "<<": 
                my_stack.push(x << y)
            elif i == "**" or i == "^":
                if x < 0 and 0 < y < 1:
                    raise ValueError
                else:
                    my_stack.push(x ** y)
            elif i == "/":
                if y == 0:
                    raise ValueError
                else:
                    my_stack.push(x / y)
            elif i == "-":
                my_stack.push(x - y)
            elif i == "*":
                my_stack.push(x * y)
            else:
                raise PostfixFormatException
        elif is_Float_(i):
            my_stack.push(float(i))
        elif i.isnumeric() or i.lstrip('-').isnumeric():
            my_stack.push(int(i))
        elif isinstance(i, str):
            raise PostfixFormatException('Invalid token')
        else:
            #print(i)
            raise PostfixFormatException

    if my_stack.size() != 1: # in case anymore operands are left unused, then too many are there and we must raise error
        #yield 'Too many operands'
        raise PostfixFormatException("Too many operands")

    return my_stack.pop()


def association(operand):
    if operand in ['<<', '>>', '+', '-', '*', '/']:
        return 'LEFT'
    elif operand in ['**', '^']:
        return 'RIGHT'
    else:
        print("Big Error Energy")
        return None


def precedence(operand):
    if operand in ['<<', '>>']:
        return 0 # lowest precedence
    elif operand in ['+', '-']:
        return 1 # a low precedence
    elif operand in ['/', '*']:
        return 2 # medium precedence
    elif operand in ['**', '^']:
        return 3 # high precedence
    elif operand in ['(', ')']:
        return 4 # highest precedence
    else:
        print("Big Error Energy")
        return None

def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    # to account for stacks sizes larger than a certain amount
    my_stack2 = Stack(2*len(input_str))

    our_expression = ""
    for i in input_str.split():
        if i.isnumeric() or is_Float_(i) or i.lstrip('-').isnumeric():
            our_expression += i
            our_expression += " "
        elif i == '(':
            my_stack2.push(i)
        elif i == ")":
            while my_stack2.peek() != '(':
                our_expression += my_stack2.pop() + ' '
            my_stack2.pop() # pop the '(' once you reach it
        elif is_Operand_(i):
            # when countering open paran: push it onto the stack
            # pop all operators and append to expression until a closing paran is reached
            if my_stack2.size() != 0: # in case we are starting with the first term , just append
                if my_stack2.peek() == "(" or my_stack2.peek() == ")": # in case the only thing preceding the operator is a paran
                    my_stack2.push(i)
                elif (precedence(i) <= precedence(my_stack2.peek()) and association(i) == 'LEFT') or (association(i) == 'RIGHT' and precedence(i) < precedence(my_stack2.peek())):
                    #our_expression += ' ' + str(my_stack2.pop()) + ' '
                    our_expression += str(my_stack2.pop()) + ' '
                    my_stack2.push(i)
                else:
                    my_stack2.push(i)
            else:
                my_stack2.push(i)

    while my_stack2.is_empty() != True:
        to_add = my_stack2.pop()

        if is_Operand_(to_add):
            our_expression += to_add + ' '
        elif is_Float_(to_add):
            our_expression += to_add + ' '
        elif is_Num_(to_add):
            our_expression += to_add + ' '

    return our_expression.rstrip()


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    # to account for stacks sizes larger than a certain amount
    my_stack3 = Stack(2*len(input_str))
    for i in input_str.split()[::-1]:
        if is_Operand_(i):
            my_stack3.push(i)
            # in case we're looking at only the first 2 encounter
            if my_stack3.size() >= 2:    
                #print(my_stack3.peek())
                operand_ = my_stack3.pop() # our most recent push is the operand
                op1 = my_stack3.pop()
                op2 = my_stack3.pop()

                my_str = op1 + " " + op2 + " " + operand_
                my_stack3.push(my_str)
        else:
            my_stack3.push(i)
    return my_stack3.peek()