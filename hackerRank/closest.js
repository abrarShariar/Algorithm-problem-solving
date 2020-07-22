function findClosest (arr1, arr2, target) {
	let i1 = 0;
	let i2 = arr2.length - 1;
	let diff = target;
	// two pointers loop

	while (i1 < arr1.length && i2 >= 0) {
		const sum = arr1[i1] + arr2[i2];
		if (Math.abs(target - sum) < diff) {
			diff = Math.abs(target - sum);
			console.log(i1, i2);
			console.log(sum);
			if (sum === target) return [i1, i2];
			if (sum < target) {
				i1++;
			} else {
				i2--;
			}
		} else {
			i1++;
			i2--;
		}
	}
	return [i1, i2];
}

let arr1 = [2, 9, 14, 20, 47];
let arr2 = [1, 5, 8, 10, 20];
const target = 50;

console.log(findClosest(arr1, arr2, target));