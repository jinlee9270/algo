function solution(price) {
    if(price >= 500000){
        return parseInt(price * 0.8)
    }
    if(300000 <= price && price < 500000){
        return parseInt(price * 0.9)
    }
    if(100000 <= price && price < 300000){
        return parseInt(price * 0.95)
    }
    return price;
}