def vowel_2_index(string):
    output = ''
    for i, char in enumerate(string):
        if char.lower() in 'aeiou':
            char = str(i+1)
        output += char
    return output
