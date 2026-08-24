"""
Problem: Merge Two Sorted Lists

Platform: LeetCode

Difficulty: Easy

Approach:

Use two pointers to traverse both sorted linked lists simultaneously. Compare
the current nodes of the two lists and attach the node with the smaller value
to the result list. The `head` pointer stores the first node of the merged list,
while `prev` keeps track of the last node added to the result. Continue until
one of the lists becomes empty. Finally, attach all remaining nodes from the
non-empty list to the merged list. If either input list is initially empty,
return the other list directly.

Time Complexity: O(n + m)

Space Complexity: O(1)
"""
class Solution:
    def mergeTwoLists(self, list1, list2):
        i = list1
        j = list2
        head = None

        if i == None:
            return j

        if j == None:
            return i

        while i != None and j != None:
            if i.val <= j.val:
                if head == None:
                    head = i
                    prev = i
                else:
                    prev.next = i
                    prev = i

                i = i.next

            else:
                if head == None:
                    head = j
                    prev = j
                else:
                    prev.next = j
                    prev = j

                j = j.next

        while i != None:
            prev.next = i
            prev = i
            i = i.next

        while j != None:
            prev.next = j
            prev = j
            j = j.next

        return head
