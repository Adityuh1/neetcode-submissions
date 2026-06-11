class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        rev_str = clean_s[::-1]
        print(rev_str.lower())
        if clean_s == rev_str:
            return True
        return False
        