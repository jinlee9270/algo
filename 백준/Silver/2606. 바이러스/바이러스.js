let fs = require("fs");
const { cachedDataVersionTag } = require("v8");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
// let input = fs.readFileSync("./input.txt").toString().split("\n");

let node = Number(input[0]);
let vertexs = input.slice(2);
const parent = [0];
for (let i = 1; i <= node; i++) {
  parent.push(i);
}

vertexs.map((ele) => {
  let vertex = ele.split(" ");
  union(Number(vertex[0]), Number(vertex[1]));
});

for (let i = 1; i <= node; i++) {
    parent[i] = find(i);
}

let cnt = 0;
for (let i = 2; i <= node; i++) {
  if (parent[i] === 1) {
    cnt++;
  }
}
console.log(cnt);

function find(x) {
  if (x === parent[x]) {
    return x;
  } else {
    let y = find(parent[x]);
    // parent[x] = y;
    return y;
  }
}

function union(x, y) {
  x = find(x);
  y = find(y);
  if (x <= y) {
    parent[y] = x;
  } else {
    parent[x] = y;
  }
}
