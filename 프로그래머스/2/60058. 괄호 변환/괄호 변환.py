def isCorrect(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append("(")
        else:
            if stack: 
                stack.pop()
            else: 
                return False
    return True

def separate(string):
    balance = 0
    for i in range(len(string)):
        if string[i] == '(':
            balance -= 1
        else:
            balance += 1
        if balance == 0:
            return i

def reverseU(string):
    string = list(string)
    for i in range(len(string)):
        if string[i] == '(':
            string[i] = ')'
        else:
            string[i] = '('
    return ''.join(string)
    
def toCorrect(string):
    if isCorrect(string):
        return string
    idx = separate(string)+1
    u = string[:idx]
    v = string[idx:]
    result = ''
    if isCorrect(u):
        result = u+toCorrect(v)
    else:
        result = '('+toCorrect(v)+')'+reverseU(u[1:-1])
    return result
        
def solution(p):
    return toCorrect(p)