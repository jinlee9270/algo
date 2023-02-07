function solution(x, y, n) {
    var answer = 0;
    const dp = new Array(1000001).fill(1000001)
    dp[x] = 0
    
    for(let i = x; i <= y ; i++){
        if (i + n <= y && dp[i] != 1000001 && dp[i] + 1 < dp[i + n]){
            dp[i + n] = dp[i] + 1 
            }
        if (i * 2 <= y && dp[i] != 1000001 && dp[i] + 1 < dp[i * 2]){
            dp[i * 2] = dp[i] + 1 
            }
        if (i * 3 <= y && dp[i] != 1000001 && dp[i] + 1 < dp[i * 3]){
            dp[i * 3] = dp[i] + 1 
            }
    }
    
    return dp[y] === 1000001 ? -1 : dp[y];
}