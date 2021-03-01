# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/1002860/Python-O(n)-by-linear-scan-w-Comment
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev_node = ListNode(float('-inf'))
        dummy_head = ListNode(float('-inf'))
        last_distinct_node = None
        cur = dummy_head
        
        while head:
            if head.val != prev_node.val and (head.next and head.val != head.next.val or not head.next):
                cur.next = head
                cur = cur.next
                last_distinct_node = head
            prev_node, head = head, head.next
            
        if last_distinct_node:
            last_distinct_node.next = None
            
        return dummy_head.next
                
s = Solution()
print(s.deleteDuplicates(head = [1,2,3,3,4,4,5]))