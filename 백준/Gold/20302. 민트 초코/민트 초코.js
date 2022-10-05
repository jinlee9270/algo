let fs = require('fs');
const { cachedDataVersionTag } = require('v8');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('./input.text').toString().split('\n');

const numbers = input[1].split(' ')
const maxNum = 100001
let divisorsChecker = Array(maxNum).fill(0)
let primesFinder = Array(maxNum).fill(0)
let isInt = true
let inZero = false

for (let i = 2; i *i < maxNum; i++) { 
    if(primesFinder[i] === 0){
        for (let j = 2 * i; j < maxNum; j += i) { 
            primesFinder[j] = i
        }
    }
}

for(let i = 0; i < numbers.length; i += 2){
    let number = Math.abs(parseInt(numbers[i]))
    let isUp = true

    if(i == 0 || numbers[i - 1] == '*'){
        isUp = true
    }
    else if(numbers[i - 1] == '/'){
        isUp = false
    }

    if(number === 0){
        inZero = true
        break
    }
    else{
        while(true) {
            if(primesFinder[number] === 0){
                if(isUp){
                    divisorsChecker[number] += 1
                }
                else{
                    divisorsChecker[number] -= 1
                }
                break
            }
            if(isUp){
                divisorsChecker[primesFinder[number]] += 1
            }
            else{
                divisorsChecker[primesFinder[number]] -= 1
            }
            number /= primesFinder[number]
            // console.log("divisor",divisorsChecker[primesFinder[number]], "primesFinder",primesFinder[number], "number",number)
        }
    }
}

if(!inZero){
    for(let i = 2; i < maxNum; i++){
        if(divisorsChecker[i] < 0){
            isInt = false
            break
        }
    }
}

if(isInt){
    console.log("mint chocolate")
}
else{
    console.log("toothpaste")
}
