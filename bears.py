

def mult_two(num):
    digit1 = num % 10
    digit2 = (num // 10) % 10
    return digit1 * digit2

def bears(bear_num):

    # we check before we clear the list in the recursion in case it has a 42 option in
    if bear_num == 42:
        return True
    elif bear_num < 42:
        return False

    results = []

    # first branch of possible permutations, which will recurse by itself through all the branches starting with div by 2
    if bear_num % 2 == 0:
        results.append(bears(bear_num - (bear_num // 2))) # appending to an output vs returning so if can go onto elif in case it doesn't work

    if (bear_num % 3 == 0) or (bear_num % 4 == 0):
        product = mult_two(bear_num)
        # this happened bc of the branches hitting 0 and not getting any closer to 42 so it just got stuck in a loop
        if product != 0:
            results.append(bears(bear_num- product))
     
    if  bear_num % 5 == 0:
        results.append(bears(bear_num - 42))

    # checking if there is a 42==42 in results
    return True in results

# print(bears(250))
# print(bears(42))
# print(bears(53))
# print(bears(41))
# print(mult_two(52))