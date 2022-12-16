function solution(n) {
    let i = 1
    let piece = 6
    while((piece * i) % n !== 0){
        i += 1
    }
    return i
}