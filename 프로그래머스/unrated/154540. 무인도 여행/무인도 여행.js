function solution(maps) {
  var answer = [];
  const row = maps.length;
  const col = maps[0].length;
  const newMaps = maps.map((ele) => ele.split(""));

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (newMaps[i][j] !== "X") {
        answer.push(bfs(i, j, 0, newMaps));
      }
    }
  }
  return answer.length > 0 ? answer.sort((a, b) => {return a - b}) : [-1];
}

function bfs(i, j, sum, newMaps) {
  const queue = [[i, j]];
  sum = sum + Number(newMaps[i][j]);
  newMaps[i][j] = "X";
  const dr = [0, 0, -1, 1];
  const dc = [-1, 1, 0, 0];

  while (queue.length > 0) {
    const temp = queue.pop();
    const col = temp[1];
    const row = temp[0];

    for (let l = 0; l < 4; l++) {
      const newCol = col + dc[l];
      const newRow = row + dr[l];
      if (
        0 <= newCol &&
        newCol < newMaps[0].length &&
        0 <= newRow &&
        newRow < newMaps.length &&
        newMaps[newRow][newCol] !== "X"
      ) {
        queue.push([newRow, newCol]);
        sum = sum + Number(newMaps[newRow][newCol]);
        newMaps[newRow][newCol] = "X";
      }
    }
  }
  return sum;
}