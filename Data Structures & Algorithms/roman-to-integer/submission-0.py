class Solution:
    def romanToInt(self, s: str) -> int:
        # for eg: s = 'MCMMCIV'

        roman_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        } # symbol : value
        
        total = 0

        for i in range(len(s)-1): 
            #loop to visit and deciding whether to +/- the current symbol value from total, except the last symbol as it is add by default. s[i+1] would error with index out of bound if we dont exclude the last pos
            current_val =  roman_map[s[i]] #current symbol's value from the map
            
            next_val = roman_map[s[i+1]] #current symbol's value from the map

            if(current_val >= next_val):
                total += current_val
            else:
                total -= current_val

        last_val = roman_map[s[-1]] # the last val which we are adding outside the loop because it will be added by default as there is no next character to compare to so it doesnt have to stay in the loop

        total += last_val
        
        return total

            


