let fs = require('fs');
const { cachedDataVersionTag } = require('v8');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('./input.text').toString().split('\n');

const n = parseInt(input[0])
const newInput = input.slice(1)
let bambooMap = new Array()
let pandaMap = Array.from(Array(n), () => Array(n).fill(1))

for (let i = 0;i < n; i++){
    bambooMap.push(newInput[i].split(/\s+/).map(num => parseInt(num)))
}

que = new Array
for (let i = 0; i < n; i++){
    for (let j = 0; j < n; j++){
        que.push([bambooMap[i][j], i, j])
    }
}
que.sort((a, b) => {
    return b[0] - a[0];
})

function bfs(){
    dr = [0,0,1,-1]
    dc = [-1,1,0,0]

    while (que.length > 0) {
        let cur = que.pop()
        for (let i = 0;i < 4;i++){
            nr = cur[1] + dr[i]
            nc = cur[2] + dc[i]
            if (0 <= nr && nr < n && 0 <= nc && nc < n &&
                bambooMap[nr][nc] < bambooMap[cur[1]][cur[2]] &&
                pandaMap[cur[1]][cur[2]] < pandaMap[nr][nc] + 1){
                pandaMap[cur[1]][cur[2]] = pandaMap[nr][nc] + 1
            }
        }
    }
}

bfs()
console.log(Math.max(...pandaMap.flat()))
