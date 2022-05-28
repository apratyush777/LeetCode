s1 = s2 = ""
 temp1 = l1
  temp2 = l2
   while temp1:
        s1 += str(temp1.val)
        temp1 = temp1.next
    while temp2:
        s2 += str(temp2.val)
        temp2 = temp2.next
    n1 = int(s1[::-1])
    n2 = int(s2[::-1])
    add = str(n1+n2)
    final = add[::-1]  # final = 708
    # print(final)
    head = ListNode(final[0], None)
    t = head
    for i in range(1, len(final)):
        node = ListNode(final[i], None)
        t.next = node
        t = t.next
    return head
