var MinStack = function () {
  this.top = -1;
  this.stack = [];
};

MinStack.prototype.push = function(x) {
  // for min array insert till min array
  if (this.length === 0) {
    this.stack.push(x);
    this.top = 0;
    return;
  }

  this.stack.push(x);
  let index = this.top;
  this.top++;
  this.stack.sort((a, b) => b - a);

};

let minStack = new MinStack();
minStack.push(10);
minStack.push(20);
minStack.push(100);
minStack.push(1);

console.log(minStack);
