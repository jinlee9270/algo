let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync("input.text").toString().split("\n");

const [count, orderNum] = input[0].split(" ").map((ele) => Number(ele));
const heights = input[1].split(" ").map((ele) => Number(ele));

const orders = [];
for (let i = 2; i < 2 + orderNum; i++) {
  orders.push(input[i].split(" ").map((ele) => Number(ele)));
}

const prefix = new Array(100002).fill(0);
for (let i = 0; i < orderNum; i++) {
  const [start, end, order] = orders[i];
  prefix[start] += order;
  prefix[end + 1] -= order;
}

for (let i = 0; i < count; i++) {
  prefix[i + 1] += prefix[i]
  heights[i] += prefix[i + 1]
}

console.log(heights.slice(0, count).join(" "));
