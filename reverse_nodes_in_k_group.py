# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/817587/Python-easy-solution-O(N)-time-o(1)-space
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseHelper(self, head, k, leftNodes):
        if leftNodes < k:
            return head
        
        count = 0
        prev = None
        current = head
        while current and count < k:
            count += 1
            leftNodes -= 1
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        if next:
            head.next = self.reverseHelper(next, k, leftNodes)
            
        return prev
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        leftNodes = 0
        node = head
        while node:
            leftNodes += 1
            node = node.next
            
        return self.reverseHelper(head, k, leftNodes)

s = Solution()
print(s.reverseKGroup(head = [1,2,3,4,5], k = 1))