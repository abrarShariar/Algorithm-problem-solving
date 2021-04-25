// Versatile add
// add(3)(4) 
// add(10)(12)

function addFactory(adder, toAdd) {
    if (toAdd != undefined) {
        return adder + toAdd
    }
    return function addSum (toAdd) {
        return adder + toAdd
    }
}

console.log(addFactory(3)(4))
console.log(addFactory(10)(12))
console.log(addFactory(5,10))