function rotateMatrix (mat) {
    const columnLimit = mat[0].length
    const rowLimit = mat.length
    resultMat = []

    for (let column = 0; column < columnLimit; column++) {
        const newMat = []
        for (let row = rowLimit - 1; row >= 0; row--) {
            newMat.push(mat[row][column])
        }
        resultMat.push(newMat)
    }
    return resultMat
}

input_mat = [
    [1,2,3,10],
    [4,5,6,11],
    [7,8,9,12],
    [0,0,0,0]
]

console.log(rotateMatrix(input_mat))