let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync("input.text").toString().split("\n");

const standard = input[0].split("");
const compare = input[1].split("");

const dp = Array.from(Array(standard.length + 1), () =>
  Array(compare.length + 1).fill(0)
);
for (let i = 1; i <= standard.length; i++) {
  for (let j = 1; j <= compare.length; j++) {
    if (compare[j - 1] === standard[i - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1
    } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
    }
  }
}
console.log(dp[standard.length][compare.length]);
