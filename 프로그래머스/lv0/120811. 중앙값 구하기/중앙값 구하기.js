function solution(array) {
    array.sort((a, b) => {
        return a - b;
    });
    return array.length % 2 === 0 ? array[array.length / 2] : array[parseInt(array.length / 2)] 
}