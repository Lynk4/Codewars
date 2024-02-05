def valid_parentheses(paren_str):
    stack = []
    for s in paren_str:
        if(s == '('):
            stack.append(s)
        elif(s == ')'):
            try:
                stack.pop()
            except:
                return False
    if(len(stack) == 0):
        return True
    else:
        return False
