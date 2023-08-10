function solution(picks, minerals) {
    var answer = 0, i, j;
    var sum = picks.reduce((total, value) => total + value, 0);
    
    // 5개씩 자르기
    var arr = [];
    for (i = 0; i < Math.min(minerals.length, sum*5); i+=5) {
        arr.push(minerals.slice(i, Math.min(i+5, minerals.length)));
    };
    
    //각 미네랄 개수 구하고 내림차순 정렬
    var result = [];
    for (i = 0; i < arr.length; i++) {
        r = [0, 0, 0]
        for (j = 0; j < arr[i].length; j++) {
            if (arr[i][j] == "diamond") r[0] += 1;
            else if (arr[i][j] == "iron") r[1] += 1;
            else r[2] += 1;
        }
        result.push(r)
    }
    result.sort().reverse()
    
    // 계산
    for (i = 0; i < result.length; i++) {
        if (picks[0] > 0) {
            for (j = 0; j < 3; j++) {
                answer += result[i][j]
            }
            picks[0] -= 1
        }
        else if (picks[1] > 0) {
            for (j = 0; j < 3; j++) {
                if (j == 0) answer += result[i][j]*5
                else answer += result[i][j]
            }
            picks[1] -= 1
        }
        else if (picks[2] > 0){
            for (j = 0; j < 3; j++) {
                if (j == 0) answer += result[i][j]*25
                else if (j == 1) answer += result[i][j]*5
                else answer += result[i][j]
            }
            picks[2] -= 1
        }
    }
    return answer;
}