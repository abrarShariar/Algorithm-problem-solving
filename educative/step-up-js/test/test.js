const assert = require('assert')
const bin_search = require('../binary_search').bin_search

console.log(bin_search([1], 2))

// describe("Binary testing", function () {
//     test('binary search', function () {
//         expect(bin_search([1,2,3], 2)).toBe(2);
//         expect(bin_search([2], 2)).toBe(2);
//         expect(bin_search([1,2,3,4], 10)).toBe(-1);  
//     }) 
// })