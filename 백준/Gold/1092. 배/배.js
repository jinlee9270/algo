let fs = require('fs');
const { cachedDataVersionTag } = require('v8');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('./input.text').toString().split('\n');

const craneNum = parseInt(input[0])
const weightLimits = input[1].split(' ').map(ele => parseInt(ele))
const loadNum = parseInt(input[2])
let loadWeights =  input[3].split(' ').map(ele => parseInt(ele))
let time = 0
let lastMove = Array.from({length: loadNum}, () => 0)

loadWeights.sort(function(a, b) {
    return b - a
})

weightLimits.sort(function(a, b) {
    return b - a
})
// console.log(loadWeights)
// console.log(weightLimits)

if (weightLimits[0] < loadWeights[0]) {
    console.log(-1)
    // 여기서 프로그램 종료
}

else {
    while (true) {
        for(let i = 0;i < craneNum; i++){
            let picked = false
            for (let j = lastMove[i]; j < loadNum; j++) {
                if (loadWeights[j] <= weightLimits[i] && loadWeights[j] != 0) {
                    loadWeights[j] = 0
                    lastMove[i] = j
                    picked = true
                    break
                }
            }
            if (!picked) {
                lastMove[i] = loadNum
            }
        }
        time += 1
        let weightSum = 0
        for (let i = 0; i < loadNum; i++){
            weightSum += loadWeights[i]
        }
        // console.log(time, loadWeights, weightSum)
        if (weightSum === 0){
            break
        }
    }
    console.log(time)
}
