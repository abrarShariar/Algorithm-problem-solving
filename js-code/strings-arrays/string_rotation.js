function string_rotation (str1, str2) {
    // if the length of the string are not same => blah
    if (str1.length != str2.length) {
        return false
    }
    // find the starting point on str2 => cause str2 is the rotationed one
    str1_start_index = 0
    str2_start_index = str1_start_index

    while (str2_start_index < str2.length) {
        if (str2[str2_start_index] == str1[0]) {
            break
        }
        str2_start_index += 1
    }

    // O(n)
    // start checking if the next elements in the string are matching
    while (str1_start_index < str1.length) {
        if (str1[str1_start_index] != str2[str2_start_index]) {
            return false
        } else {
            str2_start_index = str2_start_index == str2.length - 1 ? 0 : str2_start_index += 1
            str1_start_index += 1
        }
    }
    return true
}

console.log(string_rotation("abcde", "bcdea"))
console.log(string_rotation("abcde", "a"))
console.log(string_rotation("abc", "bcx"))
console.log(string_rotation("rotation", "tationro"))