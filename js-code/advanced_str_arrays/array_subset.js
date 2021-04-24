function array_subset (arr1, arr2) {
    // create a dictionary of the first array => O(n)
    // create a dictionary of the second array => O(n)
    // check if all the items in the second array is also there in the first array => O(n)

    if (arr2.length > arr2.length) {
        return false
    }

    arr1_dict = {}
    arr2_dict = {}
    
    arr1.forEach(item => {
        if (arr1_dict[item] == undefined) {
            arr1_dict[item] = 1
        } else {
            arr1_dict[item] = arr1_dict[item] + 1
        }
    })

    arr2.forEach(item => {
        if (arr2_dict[item] == undefined) {
            arr2_dict[item] = 1
        } else {
            arr2_dict[item] = arr2_dict[item] + 1
        }
    })

    for (const key in arr2_dict) {
        if (arr1_dict[key] == undefined || arr2_dict[key] > arr1_dict[key]) {
            return false
        }
    }
    return true
}


console.log(array_subset([1,2,3,3], [2,3,3,3]))
// is an empty set subset of any other set?
console.log(array_subset([1,2,3,3], []))