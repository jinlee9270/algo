function solution(n, left, right) {
    const answer = []
    
    for (let i = left ; i <= right ; i++){
        answer.push(Math.max(Math.floor(left / n), left++ % n) + 1)
    }
    return answer;
}