function solution(s){
    let answer = true;
    let pairCheckers = new Array
    let temp = null
    
    while (s.length > 0){
        temp = s.charAt(s.length - 1)
        
        if(temp === ')'){
            pairCheckers.push(temp)
        }
        else{
            if(pairCheckers.length === 0){
                answer = false
                break
            }
            else{
                pairCheckers.pop()
            }
        }
        s = s.slice(0, -1)
    }
    
    if(pairCheckers.length !== 0){
        answer = false
    }
    
    return answer;
}