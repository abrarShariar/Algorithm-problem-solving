
# using floyds cycle detection algo
def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2
    while current1 != current2:
        if current1 is None:
            current1 = head2
        else:
            current1 = current1.next
        
        if current2 is None:
            current2 = head1
        else:
            current2 = current2.next

        if current1 == current2:
            return current1.data
            

    return current1.data