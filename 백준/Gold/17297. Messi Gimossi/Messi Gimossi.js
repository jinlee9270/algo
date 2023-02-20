let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
//let input = fs.readFileSync("input.text").toString().split("\n");

function process1(index) {
  const message = "Messi Gimossi";
  let n1 = 13;
  let n2 = 5;
  const fibo = [n2, n1];
  let num = 0;

  const mx = 2 ** 30;
  while (num < mx) {
    num = n1 + 1 + n2;
    n2 = n1;
    n1 = num;
    fibo.push(num);
  }

  let i = fibo.length;
  while (i > 1) {
    if (index === fibo[i - 1] + 1) {
      index = -1;
      break;
    } else if (index > fibo[i - 1]) {
      i -= 2;
      index -= fibo[i + 1] + 1;
    } else {
      i -= 1;
    }
  }

  if (index === -1 || index === 6) {
    return "Messi Messi Gimossi";
  } else {
    return message[index - 1];
  }
}

function process2() {
  let n1 = "Messi Gimossi ";
  let n2 = "Messi ";
  let str = "";
  for (let i = 0; i < 30; i++) {
    let temp = str;
    str = n1 + n2;
    n2 = n1;
    n1 = str;
  }

  return " " + str;
}

function process2Answer(answer, index) {
  if (answer[index] === " ") {
    return "Messi Messi Gimossi";
  }
  return answer[index];
}

input2 = Number(input[0]);
console.log(process1(input2));
