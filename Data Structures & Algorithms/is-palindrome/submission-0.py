class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_s = s
        s = temp_s.lower()
        list_s = list(s)
        cleaned_list_s = []
        for i in list_s:
            if i.isalnum():
                cleaned_list_s.append(i)

        
        reversed_list_s = list(reversed(cleaned_list_s))
        if cleaned_list_s == reversed_list_s:
            return True
        return False
        