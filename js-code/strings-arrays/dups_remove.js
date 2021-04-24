function dups_remove (input_str) {
    return [...new Set(input_str)].join('')
}

console.log(dups_remove('aabcd'))
console.log(dups_remove('abcdabcdcdcdcdcdcdabcd'))