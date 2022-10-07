function solution(n, words) {
    let answer = [0,0]
    const temp = words[0]
    let dic = { [temp] : 1}
    
    for(let i = 1; i < words.length; i++){
        if(words[i - 1].slice(-1) === words[i].charAt(0)){
            if(words[i] in dic){
                answer = [i % n + 1, Math.ceil((i + 1) / n)] 
                break
            }
            else{
                dic[words[i]] = 1
            }
        }
        else{
            answer = [i % n + 1, Math.ceil((i + 1) / n)] 
            break
        }
    }

    return answer;
}