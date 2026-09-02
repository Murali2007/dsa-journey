"""
Problem: Sort List

Platform: LeetCode

Difficulty: Medium

Approach:

1. Traverse the linked list and store all node values in a Python list.
2. Sort the values using Python's built-in sort() method.
3. Traverse the linked list again and replace each node's value
   with the corresponding sorted value from the list.
4. Return the original head of the linked list.

Key Idea:
Convert the linked list values into an array, sort the array,
and then write the sorted values back into the linked list.

Time Complexity: O(n log n)
    - O(n) to traverse the linked list.
    - O(n log n) to sort the values.
    - O(n) to write the sorted values back.

Space Complexity: O(n)
    - Extra list is used to store all node values.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head) :
        l = []

        curr = head
        while(curr != None):
            l.append(curr.val)
            curr = curr.next
        
        l.sort()

        curr = head
        i = 0
        while(curr != None):
            curr.val = l[i]
            curr = curr.next
            i += 1
        
        return head