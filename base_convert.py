
# originally, this was going to use a dictionary to implement 10-16 for hex
# ASCII hacks were cooler though, so here we are
def convert(num, b):
    if num < b:                     # in case 
        return digit_to_chr(num)

    remainder = num % b
    quotient = num // b

    return convert(quotient, b) + digit_to_chr(remainder)

def digit_to_chr(digit):
    if digit < 10:
        return str(int('0') + digit)
    elif digit > 10 and digit < 16:
        return chr(ord('A') + digit - 10)

#print(convert(30,4))
#print(convert(45, 2))
#print(convert(316, 16))

'''
print(digit_to_chr(16))
print(digit_to_chr(15))
print(digit_to_chr(9))
print(digit_to_chr(10))
'''