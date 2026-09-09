class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        else:
            div = 1
            while x >= 10 * div:
                div = div * 10
            
            while x:
                right = x // div
                left = x % 10

                if left != right:
                    return False

                x = (x % div) // 10
                div = div // 100
            return True






       

        