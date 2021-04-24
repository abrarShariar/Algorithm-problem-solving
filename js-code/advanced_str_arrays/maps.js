const myMap = new Map()

// set data to map
myMap.set('name', 'Abrar')
myMap.set('skills', ['Python', 'JavaScript'])
myMap.set(1, 0)

// // get data from a map
// console.log(myMap.get('name'))
// console.log(myMap.get(1))
// console.log(myMap.get('skills'))

// // check if map has a key
// console.log(myMap.has('skills'))
// console.log(myMap.has('test'))

for (const [key, value] of myMap.entries()) {
    console.log(key, value)
}

for (const key of myMap.keys()) {
    console.log(key)
}