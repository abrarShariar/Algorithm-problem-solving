// generator function or factory functions
function addFactory(storedNum) {
    return function addNum(numToAdd) {
        return storedNum + numToAdd
    }
}

const adderFactory10 = addFactory(10)
const adderFactory20 = addFactory(20)
console.log(adderFactory10(4))
console.log(adderFactory10(10))


