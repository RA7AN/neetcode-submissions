class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {} # number : frequency
        

        # nums[i] is the key
        # hashmap[nums[i]] is its value in the hashmap

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        # we can extract pairs of (number, frequency) from hashmap using hashmap.items

        # let us first write a simple function to extract just the frequency from a pair

        def get_frequency(item):
            return item[1]

        #now we use that frequency function to sort the hashmap in descending order using sorted() function

        sorted_items = sorted(hashmap.items(), key = get_frequency, reverse=True)

        # sorted items will be a list of pairs of sorted (number, frequency) in descending order

        #lets write a loop to extract just the frequencies from sorted_items and append it to a list result

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result
        


        