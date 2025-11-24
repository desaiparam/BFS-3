# Time Complexity : O(2^N) where N is the length of the input list
# Space Complexity : O(2^N*N) for storing the valid expressions
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using BFS to generate all possible expressions by removing invalid parentheses level by level.
# I maintain a queue to explore each expression and a set to avoid processing duplicates.
# For each expression, I check if it is valid using a helper function.
# If a valid expression is found at the current level, I add it to the result list and set a flag to stop further exploration at deeper levels.
# If not found, I generate new expressions by removing one parenthesis at a time and add them to the queue for further exploration.
# Finally, I return the list of valid expressions.

from typing import List
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        q = deque([s])
        seen = set([s])
        found = False
        def isvalid(curr):
            count = 0
            for i in curr:
                if i.isalpha():
                    continue
                if i == "(":
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        while q and not found:
            for _ in range(len(q)):
                curr = q.popleft()
                if isvalid(curr):
                    res.append(curr)
                    found = True
                elif not found:
                    for i in range(len(curr)):
                        if curr[i].isalpha():
                            continue
                        baby = curr[:i] + curr[i+1:]
                        if baby not in seen:
                            q.append(baby)
                            seen.add(baby)
        return res

        
        