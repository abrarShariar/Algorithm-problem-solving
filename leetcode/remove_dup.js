function ListNode(val) {
  this.val = val;
  this.next = null;
 }

var deleteDuplicates = function(head) {
  let pointer_i = head;
  if (head === null) return head;
  if (head.next === null) {
    return head;
  }
  let pointer_j = head.next;
  while (pointer_j !== null) {
    while (pointer_i.val === pointer_j.val) {
      pointer_i.next = pointer_j.next;
      pointer_j = pointer_j.next;
      if (pointer_j === null) {
        return head;
      }
    }
    pointer_i = pointer_i.next;
    pointer_j = pointer_j.next;
  }

  return head;
};
