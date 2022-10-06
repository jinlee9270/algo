function solution(s) {
    let answer = [0,0]
    let newStr = s
    
    while(newStr > 1){
         let xDelZero = newStr.replace(/0/g, '')
        answer[1] += (newStr.length - xDelZero.length)
        newStr = xDelZero.length.toString(2)
        answer[0] += 1
    }
    return answer
}