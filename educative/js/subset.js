// function isSubset(arr1, arr2) {
//     countOccurance = arr2.reduce((accumulatedVal, currentVal) => {
//         if (arr1.includes(currentVal)) {
//             accumulatedVal += 1;
//         }
//         return accumulatedVal;
//     }, 0);

//     return countOccurance === arr1.length;
// }

function isSubset (arr1, arr2) {
	// dictionary for arr1
	const arr2_dict = {}
	arr2.forEach(item => {
		arr2_dict[item] = true;
	});
	let isValid = true;
	arr1.forEach(item => {
		if (!arr2_dict[item]) {
			isValid = false;
			return;
		}
	});
	return isValid;
}

console.log(isSubset([1,2,3], [4,5,6]));