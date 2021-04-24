function checkUnique (input_str) {
    // using dictionary
    // unique_dict = {}
    // O(n)
    // for (let ch of input_str) {
    //     if (ch in unique_dict) {
    //         return false
    //     }
    //     unique_dict[ch] = 1
    // }
    // return true

    // O(nlogn)
    // sorted array
    // input_list = input_str.split('').sort()
    // // O(n)
    // for (let i = 1; i < input_list.length; i++) {
    //     if (input_list[i] == input_list[i-1]) {
    //         return false
    //     }
    // }

    // return true

    // return new Set(input_str).size === input_str.length
}

input_list = [
    "Abrar",
    "Test",
    "ZZZ",
    "Aa",
    "@@((",
    "1"
]

input_list.forEach(item => {
    console.log(checkUnique(item))
})
