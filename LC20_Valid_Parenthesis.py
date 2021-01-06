"""
Runtime: 28 ms, faster than 83.24% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.1 MB, less than 95.25% of Python3 online submissions for Valid Parentheses.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) & 1:
            return False
        match = {
            '(':')',
            '[':']',
            '{':'}',             
                }
        tracking = []
        for i in s:
            if i in match.keys():
                tracking.append(i)
            else:
                if not tracking or match[tracking.pop()] != i:
                    return False
        return not tracking
