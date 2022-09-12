def perm_gen_lex(in_str):
    res = []
    if len(in_str) == 1:
        res.append(in_str)

    for char_idx in range(len(in_str)):
        cut_str = in_str[char_idx]
        simple_str = in_str[:char_idx] + in_str[char_idx + 1:]
        for result in perm_gen_lex(simple_str):
            res.append(cut_str + result)

    return res
        

#print(perm_gen_lex('abc'))

