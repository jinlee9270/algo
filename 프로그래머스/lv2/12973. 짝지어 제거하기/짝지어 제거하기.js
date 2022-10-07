function solution(s){
    if (s.length % 2 !== 0){
        return 0
    }
    let stack = [s[0]]
    
    for (let i = 1; i < s.length; i++){
        if (stack[stack.length - 1] === s[i]){
            stack.pop()
        }
        else {
            stack.push(s[i])
        }
    }
    if (stack.length > 0) {
        return 0
    }
    else {
        return 1
    }
}