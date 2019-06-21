function ListNode(val) {
     this.val = val;
     this.next = null;
}

var mergeTwoLists = function(l1, l2) {
  let lr = new ListNode(-1);
  let pointer = lr;

  while (l1 !== null && l2 !== null) {
    let n = new ListNode(-1);
    if (l1.val < l2.val) {
      n.val = l1.val;
      l1 = l1.next;
    } else {
      n.val = l2.val;
      l2 = l2.next;
    }
   lr.next = n;
   lr = lr.next;
  }

  while (l1 !== null) {
    let n = new ListNode(l1.val);
    lr.next = n;
    lr = lr.next;
    l1 = l1.next;
  }

  while (l2 !== null) {
    let n = new ListNode(l2.val);
    lr.next = n;
    lr = lr.next;
    l2 = l2.next;
  }
  return pointer.next;
};
