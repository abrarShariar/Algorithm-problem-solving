function highest_frequency (input_list) {
    const str_dict = {}
    let max_count = 0
    let max_str = input_list[0]

    // O(n)
    input_list.forEach(item => {
        // O(1)
        if (!(item in str_dict)) {
            str_dict[item] = 1
        } else {
            str_dict[item] = str_dict[item] + 1
        }

        if (str_dict[item] > max_count) {
            max_count = str_dict[item]
            max_str = item
        }
    })
    return max_str
}

console.log(highest_frequency(['abc', 'def', 'abc', 'def', 'abc']))