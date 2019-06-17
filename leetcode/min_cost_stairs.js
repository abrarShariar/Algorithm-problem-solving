var minCostClimbingStairs = function(cost) {
  let cost0 = cost[cost.length - 1];
  let cost1 = cost[cost.length - 2];
  let start = cost.length - 1;  // check for 1 in next step
  let currentIndex = start;

  if (cost.length === 2) {
    return Math.min(...cost);
  }

  // when start is 0
  while ((currentIndex - 1) >= 0 && (currentIndex - 2) >= 0) {
    if (cost[currentIndex - 1] < cost[currentIndex - 2]) {
      cost0 += cost[currentIndex - 1];
      currentIndex = currentIndex - 1;
    } else {
      cost0 += cost[currentIndex - 2];
      currentIndex = currentIndex - 2;
    }
  }

  // when start is 1
  start = cost.length - 2;
  currentIndex = start;
  while ((currentIndex - 1) < 0 && (currentIndex - 2) < cost.length) {
    if (cost[currentIndex - 1] < cost[currentIndex - 2]) {
      cost1 += cost[currentIndex - 1];
      currentIndex = currentIndex - 1;
    } else {
      cost1 += cost[currentIndex - 2];
      currentIndex = currentIndex - 2;
    }
  }


  return Math.min(cost0, cost1);
};


console.log(minCostClimbingStairs([10,20,30]));
console.log(minCostClimbingStairs([40,20]));
console.log(minCostClimbingStairs([100,20,30,1]));
console.log(minCostClimbingStairs([0,1,2,2]));
