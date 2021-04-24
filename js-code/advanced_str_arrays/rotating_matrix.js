// function rotateMatrix (mat) {
//     const columnLimit = mat[0].length
//     const rowLimit = mat.length
//     resultMat = []

//     for (let column = 0; column < columnLimit; column++) {
//         const newMat = []
//         for (let row = rowLimit - 1; row >= 0; row--) {
//             newMat.push(mat[row][column])
//         }
//         resultMat.push(newMat)
//     }
//     return resultMat
// }

function rotateMatrix (mat) {
    const columnLimit = mat[0].length
    const rowLimit = mat.length

    for (let column = 0; column < columnLimit; column++) {
        for (let row = rowLimit - 1; row >= 0; row--) {
            mat[column][(rowLimit - 1) - row], mat[row][column] = mat[row][column], mat[column][(rowLimit - 1) - row]
        }
    }
    return mat
}

input_mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

console.log(rotateMatrix(input_mat))