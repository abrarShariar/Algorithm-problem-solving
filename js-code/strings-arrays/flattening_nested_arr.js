// recursive solution
function flatten(nestedArray, result_arr) {
    nestedArray.forEach(item => {
        if (Array.isArray(item)) {
            flatten(item, result_arr)
        } else {
            result_arr.push(item)
        }
    })
    return result_arr
}

inputArr = [
    'level1',
    ['level2', ['level3', 'level4', ['level5']]]
]

result_arr = []
console.log(flatten(inputArr, result_arr))