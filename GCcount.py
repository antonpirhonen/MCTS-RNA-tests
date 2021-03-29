def GCcount(seq):
    if (len(seq) == 0): raise Exception("Sequence length is zero")
    a = c = g = u = 0
    for char in seq:
        if char == 'A':
            a += 1
            continue
        if char == 'C':
            c += 1
            continue
        if char == 'G':
            g += 1
            continue
        if char == 'U':
            u += 1
            continue
        raise Exception("Undefined char: " + str(char) + " found in sequence")
    return (float(c+g))/(a+u+c+g)