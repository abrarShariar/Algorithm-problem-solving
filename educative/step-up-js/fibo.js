
// ITERATIVE
// function fibonacci (n) {
//     if (n <= 1) {
//         return [1]
//     } 
//     if (n <= 2) {
//         return [1,1]
//     }

//     const result = []
//     result.push(1)
//     result.push(1)
//     for (let i = 2; i < n; i++) {
//         const newItem = result[i-1] + result[i-2]
//         result.push(newItem)
//     }

//     return result
// }

// RECURSIVE => get the nth fibonacci
function fibonacci (n, fiboDict) {
    if (n <= 2) {
        return n-1
    }
    
    if (fiboDict[n-1] == undefined) {
        fiboDict[n-1] = fibonacci(n-1)
    }

    return fiboDict[n-1] + fiboDict[n-2]
}

const testData = [4,6,8,1,2]
const fiboDict = {}
testData.forEach(data => {
    console.log(fibonacci(data, fiboDict))
})