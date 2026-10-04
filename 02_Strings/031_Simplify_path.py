"""
Problem: Simplify Path

Platform: LeetCode

Difficulty: Medium

Approach:

Use a list as a stack to process each directory component.

1. Traverse the path character by character and build each path component.
2. Ignore `.` because it represents the current directory.
3. For `..`, remove the most recent directory from the stack if one exists.
4. For a normal directory, add it to the stack.
5. Process the final component after the loop.
6. If no directories remain, return `/`.
7. Otherwise, join all remaining directories to form the simplified path.

Key Idea:

Treat the directory structure like a stack:
normal directory → push,
`..` → pop,
`.` → ignore.

Time Complexity: O(n)

Space Complexity: O(n)
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        part = '/'
        for i in range(1,len(path)):
            ch = path[i]
            if(ch != '/'):
                part += ch
            
            if ch == '/' and part == '/.':
                part = '/'
                continue
            elif ch == '/' and part == '/..':
                if res:
                    res.pop()
                part = '/'
            elif ch == '/' and part != '/':
                res.append(part)
                part = '/'
        
        if part == '/.':
            pass
        elif part == '/..':
            if res:
                res.pop()
        elif part != '/':
            res.append(part)
        
        if not res : return '/'
        return "".join(res)
                
        

            
            


        