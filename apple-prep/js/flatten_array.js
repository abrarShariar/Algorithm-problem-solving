function flatten(nestedArray) {
    // Your code here
    const result_arr = [];
    return flatten_me(nestedArray, result_arr);
}

function flatten_me (nestedArray, result_arr) {
    for (let i = 0; i < nestedArray.length; i++) {
        const currentElement = nestedArray[i];
        if (currentElement.isArray()) {

        }
    }
}