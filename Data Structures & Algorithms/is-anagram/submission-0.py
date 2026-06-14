class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Array to store frequency of each letter (a-z)
        freq = [0] * 26
        
        # Count characters from both strings in one pass
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        # Check if all frequencies are zero
        for count in freq:
            if count != 0:
                return False
        
        return True