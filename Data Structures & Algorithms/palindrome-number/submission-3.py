class Solution:
    def isPalindrome(self, x: int) -> bool:
#half reversal technique so that we only compare starting half of the number and the ending half of the number
        reversed_half = 0

        if x < 0 or (x % 10 == 0 and x!=0): #if number is negative, it cannot be a plaindrome 
            # or if x is a multiple of 10 (edge case becuase +ve multiples of 10 cant be palindromes)
            # except 0 as 0 is a plaindrome
            return False
        else:
            while x > reversed_half:
                reversed_half = (reversed_half * 10) + (x % 10) 
    #multiplying exisitng reversed half by 10 and adding the lates extract digit from x
                x = x//10
            
            return (x == reversed_half) or (x == reversed_half//10)
            # we return the or of these two because
            # either x is an even number and (x == reversed_half) will cpmpare both halves
            # or x is odd and reverse half has an extra digit (from its middle) that we dont 
            # need to compare so we discard it by (x == reversed_half//10)

    


