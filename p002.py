'''
@Author: qink-DN493
@Date: 2019-12-23 10:08:18
@LastEditors  : qink-DN493
@LastEditTime : 2019-12-24 13:30:53
@Description: 
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
    head = node = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        # print("-----------------")
        # print(head,node)
        # print(head.val,node.val)
        # print(head.next,node.next)
        node.next = ListNode(carry%10)
        # print("-----------------")
        # print(head,node)
        # print(head.val,node.val)
        # print(head.next,node.next)
        # node = node.next
        carry //= 10
        # print("-----------------")
        # print(head,node)
        # print(head.val,node.val)
        # print(head.next,node.next)
    return head.next


addTwoNumbers(ListNode(1), ListNode(2))