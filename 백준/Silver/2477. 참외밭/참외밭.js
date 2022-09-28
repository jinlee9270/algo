let fs = require('fs');
const { cachedDataVersionTag } = require('v8');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('./input.text').toString().split('\n');

const kMellon = parseInt(input[0])
let maxWidth = 0
let maxHeight = 0
let cuttingArea = 1

let newInput = input.slice(1)

for (let i = 0; i < 6; i++) {
    const element = newInput[i]

    const dirLen = element.split(' ')
    const dir = parseInt(dirLen[0])
    const len = parseInt(dirLen[1])

    if (dir === 3 || dir === 4) {
        maxHeight = Math.max(len, maxHeight)
    }
    else {
        maxWidth = Math.max(len, maxWidth)
    }
}

for (let i = 0; i < 6; i++) {
    const dirLen = newInput[i].split(' ').map(element => parseInt(element))
    const bendingSide = newInput[(i + 1) % 6].split(' ').map(element => parseInt(element))
    const bendFinder = newInput[(i + 2) % 6].split(' ').map(element => parseInt(element))

    if(dirLen[0] === bendFinder[0]) {
        cuttingArea = cuttingArea * bendingSide[1]
    }
}

console.log(((maxWidth * maxHeight) - cuttingArea) * kMellon)
