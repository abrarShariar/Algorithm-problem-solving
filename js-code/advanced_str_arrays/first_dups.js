function getFirstDups (inputStr) {
    // populate a set as we go
    const charSet = new Set()
    // if exists in a set return that character
    for (const ch of inputStr) {
        if (charSet.has(ch)) {
            return ch
        }
        charSet.add(ch)
    }
    return -1
}

const input_lists = [
    "abcde",
    "abcdde",
    "aabbddee",
    "helolekjk"
]

input_lists.forEach(list => {
    console.log(getFirstDups(list))
})



