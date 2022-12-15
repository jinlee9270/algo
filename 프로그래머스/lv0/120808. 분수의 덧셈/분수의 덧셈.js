function solution(denum1, num1, denum2, num2) {
    let primes = new Array(1001).fill(true);
    for(let i = 2 ; i <= 1000; i++){
        for (let j = i ; j < parseInt(1000 / i) + 1; j++){
            primes[i * j] = false
        }   
    }
    
    primeNumbers = []
    primes.forEach((prime, idx) => {
        if (prime){
            primeNumbers.push(idx)
        }
    })
    
    let denum = num1 * num2
    let num = (denum1 * num2) + (denum2 * num1)
    
    for(let i = 2; i <= Math.max(denum, num) ; i++){
        while(denum % primeNumbers[i] === 0 && num % primeNumbers[i] === 0){
            denum /= primeNumbers[i]
            num /= primeNumbers[i]
        }
    }
    
    return [num, denum];
}