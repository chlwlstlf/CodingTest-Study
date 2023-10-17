import re

def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = re.sub(r"[^a-z0-9\-\_\.]", "", answer) #^: 제외
    # 3단계
    answer = re.sub(r"\.+", ".", answer)
    # 4단계
    answer = re.sub(r"^\.", "", answer) # ^문자: 문자가 시작인지
    answer = re.sub(r"\.$", "", answer)
    # 5단계
    if answer == "": 
        answer = "a"
    # 6단계 
    if len(answer) >= 16: 
        answer = answer[:15]
        answer = re.sub(r"\.$", "", answer)
    # 7단계
    if len(answer) <= 2:
        answer += answer[-1]*(3-len(answer))
    return answer