def disemvowel(string_):
    _string = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for s in string_:
        if s in vowels:
            continue
        _string += s
    string_ = _string
    return string_
