def changeSharp(song):
    dict = {'C#': '1', 'D#': '2', 'F#': '4', 'G#': '5', 'A#': '6'}
    for key, value in dict.items():
        song = song.replace(key, value)
    return song

def solution(m, musicinfos):
    musicinfos = [string.split(',') for string in musicinfos]
    m = changeSharp(m)
    
    # [재생 시간, 노래 제목, 재생 구간] 배열 만들기
    array = []
    for music in musicinfos:
        # 노래 재생 시간 구하기
        startTime = int(music[0][:2])*60 + int(music[0][3:])
        endTime = int(music[1][:2])*60 + int(music[1][3:])
        runningTime = endTime-startTime
        # 노래 재생 구간 구하기
        runningRange = ''
        for i in range(runningTime):
            changeMusic = changeSharp(music[3])
            runningRange += changeMusic[i%len(changeMusic)]
        array.append([runningTime, music[2], runningRange])
    
    # 정답 구하기
    array.sort(key=lambda x:-x[0])
    for a in array:
        if m in a[2]:
            return a[1]
    return '(None)'