def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    set1 = []
    set2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set2.append(str2[i:i+2])
    
    union = set1+set2
    intersec = []
    
    for i in set1:
        if i in set2:
            intersec.append(i)
            set2.remove(i)
            
    for i in intersec:
        if i in union:
            union.remove(i)
    
    if union:
        answer = len(intersec)/len(union)
    else:
        answer = 1
        
    return int(answer*65536)