def accum(st):
    result = []
    for i, char in enumerate(st, 1):
        result.append((char * i).title())
    return '-'.join(result)
