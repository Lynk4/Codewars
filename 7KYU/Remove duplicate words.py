# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

# Example:

# Input:

# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

# Output:

# 'alpha beta gamma delta'



def remove_duplicate_words(s):
    l = []
    for i in s.split():
        if i not in l:
            l.append(i)
    return " ".join(l)
            
        
