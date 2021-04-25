

function bin_search (input_list, target) {

    if (input_list.length == 1 && input_list[0] == target) {
        return target
    }   

    let start_index = 0
    let end_index = input_list.length - 1

    while (start_index < end_index) {
        let mid = parseInt((end_index + start_index) / 2)
        if (input_list[mid] == target) {
            return target
        } else if (target > input_list[mid]) {
            start_index = mid + 1
        } else {
            end_index = mid - 1
        }
    }
    return -1
}

module.exports = {
    bin_search
}





