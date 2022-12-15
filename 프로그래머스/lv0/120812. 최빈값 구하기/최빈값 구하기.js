function solution(array) {
    const arrCnts = new Array(1000).fill(0)
    
    array.forEach(ele => {
        arrCnts[ele] += 1
    })

    let mx = Math.max(...arrCnts)
    let cnt = 0
    let mxIdx = null
    arrCnts.forEach((ele, idx) => {
        if(mx === ele){
            cnt += 1
            mxIdx = idx
        }
    })
    return cnt > 1 ? -1 : mxIdx
}