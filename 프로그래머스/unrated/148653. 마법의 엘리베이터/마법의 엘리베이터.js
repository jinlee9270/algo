function solution(storey) {
  return NumberofMagincStone(storey, 0);
}

function NumberofMagincStone(storey, sum) {
  if (storey === 1 || storey === 0) {
    return storey + sum;
  }

  const result1 = NumberofMagincStone(
    Math.floor(storey / 10),
    sum + (storey % 10)
  );
  const result2 = NumberofMagincStone(
    Math.floor(storey / 10) + 1,
    sum + 10 - (storey % 10)
  );

  return Math.min(result1, result2);
}