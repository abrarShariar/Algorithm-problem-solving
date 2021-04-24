// SOLVED
// function maxProfits (input_list) {
//     buy_index = 0
//     sell_index = buy_index + 1
//     max_profit = input_list[sell_index] - input_list[buy_index]

//     // O(n)
//     while (sell_index < input_list.length) {
//         // keep moving the buy and sell index if there is no profit
//         if (input_list[sell_index] <= input_list[buy_index]) {
//             // no profit
//             buy_index += 1
//             if (buy_index == sell_index) {
//                 sell_index = buy_index + 1
//             }
//         } else {
//             // we are having a profit session
//             max_profit = Math.max(input_list[sell_index] - input_list[buy_index], max_profit)
//             // keep going till we can make profit
//             sell_index += 1
//         }
//     }

//     return max_profit
// }

// Simpler solution
function getMaxProfit (input_list) {
    minPrice = Infinity
    maxProfit = 0

    for (let i = 0; i < input_list.length; i++) {
        minPrice = Math.min(minPrice, input_list[i])
        maxProfit = Math.max(maxProfit, input_list[i] - minPrice)
    }
    return maxProfit
}

input_lists = [
    [0,0,0,0,100],
    [1,1,1,1,10,20,30,0,100],
    [100, 100],
    [0,5,4,1,1,2,3,10],
    [10,7,5,8,4,1,11,9]
]

input_lists.forEach(list => {
    console.log(getMaxProfit(list))
})