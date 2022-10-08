function solution(people, limit){
	let answer = 0
    people.sort((a,b) => b - a)
    let start = 0
    let end = people.length - 1
    
    while(start < end){
        if(people[start] + people[end] > limit){
        	start += 1
        } else {
        	start += 1
            end -= 1
        }
        answer += 1
    }
    if(start == end){
        answer += 1
    }
    return answer
}