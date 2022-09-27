let fs = require('fs');
const { cachedDataVersionTag } = require('v8');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let sum = 0
let arr = []
let mn = 9999999
let answer = 0

input.forEach(element => {
    sum += parseInt(element)
    arr.push(sum)
})

arr.forEach(candidate => {
    let absValue = Math.abs(100 - candidate)
    if (absValue < mn) {
        mn = absValue
        answer = candidate
    }
    else if (absValue === mn) {
        answer = Math.max(answer, candidate)
    }
})

console.log(answer)
