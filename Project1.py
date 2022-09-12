
from tkinter import W


def perm_gen_lex(in_str: str) -> list[str]:
    # if the input string has nothing, return empty list
    if not in_str:
        return []
    out_list = [] # the result list
    for char_index in range(len(in_str)):
        simple_str = in_str[:char_index] + in_str[char_index + 1:]
        out_list.extend(
            [in_str[char_index] + perm
             for perm in perm_gen_lex(simple_str)]
        )
    return out_list

def convert(num: int, b: int) -> str:
    if num < b:
        return digit_to_chr(num)

    remainder = num % b
    quotient = num // b

    return convert(quotient, b) + digit_to_chr(remainder)

print(convert(316, 16))

def digit_to_chr(digit: int) -> str:
    if digit < 10:
        return chr('0' + digit)
    else:
        return chr('A' + digit - 10)

def mult_two(num):
    digit1 = num % 10
    digit2 = (num // 10) % 10
    return digit1 * digit2

def bears(bear_num):

    if bear_num == 42:
        return True
    elif bear_num < 42:
        return False

    results = []

    if bear_num % 2 == 0:
        results.append(bears(bear_num - (bear_num // 2)))

    if (bear_num % 3 == 0) or (bear_num % 4 == 0):
        product = mult_two(bear_num)
        if product != 0:
            results.append(bears(bear_num- product))
     
    if  bear_num % 5 == 0:
        results.append(bears(bear_num - 42))

    return True in results

print(bears(250))
print(bears(42))
print(bears(53))
print(bears(41))



# print(mult_two(52))





