let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
//let input = fs.readFileSync("input.text").toString().split("\n");

const num = Number(input[0]);
const opers = input.slice(1);
const answers = opers.map((ele) => {
  const oper = ele.split(" ");
  if (oper[1] === "+") {
    return BigInt(oper[0]) + BigInt(oper[2]) === BigInt(oper[4])
      ? "correct"
      : "wrong answer";
  }
  if (oper[1] === "-") {
    return BigInt(oper[0]) - BigInt(oper[2]) === BigInt(oper[4])
      ? "correct"
      : "wrong answer";
  }
  if (oper[1] === "/") {
    return BigInt(oper[0]) / BigInt(oper[2]) === BigInt(oper[4])
      ? "correct"
      : "wrong answer";
  }
  if (oper[1] === "*") {
    return BigInt(oper[0]) * BigInt(oper[2]) === BigInt(oper[4])
      ? "correct"
      : "wrong answer";
  }
});

console.log(answers.join("\n"));
