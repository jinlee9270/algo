function solution(skill, skill_trees) {
    let answer = 0
    let skillList = skill.split('')

    
    for(let i = 0; i < skill_trees.length; i++){
        let newDic = {}
        let isPossible = true
        for(let j = 0; j < skillList.length ; j++){
            if(skill_trees[i].indexOf(skillList[j]) !== -1){
                newDic[skillList[j]] = skill_trees[i].indexOf(skillList[j])
            }
        }
        const results = Object.entries(newDic)
        
        results.sort((a, b) => {
          if (a[1] < b[1]) {
            return -1
          }
          if (a[1] > b[1]) {
            return 1
          }
        })
        
        for(let j = 0; j < results.length; j++){
            if(results[j][0] !== skill[j]){
                isPossible = false
            }
        }
        if(isPossible){
            answer += 1
        }
    }
    return answer
}