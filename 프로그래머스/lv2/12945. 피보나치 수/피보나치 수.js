function solution(n) {
    const fibo = Array(100001).fill(0)
    fibo[1] = 1
    fibo[2] = 1
    
    for(let i = 2; i <= n; i++){
        fibo[i] = (fibo[i - 1] % 1234567) + (fibo[i - 2] % 1234567)
    }
    return fibo[n] % 1234567
}