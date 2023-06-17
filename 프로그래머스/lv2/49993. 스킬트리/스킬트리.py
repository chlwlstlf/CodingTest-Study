def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)):
        idx = 0
        f = 0
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in list(skill):
                if skill_trees[i][j] == skill[idx]:
                    idx += 1
                else:
                    f = 1
                    break
        if f == 0:
            answer += 1
        
    return answer