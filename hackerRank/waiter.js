function waiter(number, q) {

    let primeList = [];
    let s = 2;
    for (let i = 0; i < q;i++) {
        let c = 0;
        for (let j = 1;j<=s/2;j++) {
          if (s%j === 0) {
            c++;
          }
        }
        if (c === 1) {
          primeList.push(s);
        }
        s++;
    }


    let A = [];
    let B = [];

    for (let i=0;i<=q;i++) {
      A.push([]);
      B.push([]);
    }
    A[0] = number;

    for (let i=0;i<q;i++) {
      let p = primeList[i];
      let targetA = A[i];

      while (targetA.length !== 0) {
        let num = targetA.pop();
        if (num%p === 0) {
          B[i].push(num);
        } else {
          A[i+1].push(num);
        }
      }
    }

    let resultArr = [];
    for (let i=0;i<B.length;i++) {
      for (let j = B[i].length - 1;j>=0;j--) {
        resultArr.push(B[i][j]);
      }
    }

    for (let i=0;i<A.length;i++) {
      for (let j = A[i].length - 1;j>=0;j--) {
        resultArr.push(A[i][j]);
      }
    }

    return resultArr;
}

console.log(waiter([3,3,4,4,9], 2).join("\n"));
// console.log(waiter([3,4,7,6,5], 1).join("\n"));
