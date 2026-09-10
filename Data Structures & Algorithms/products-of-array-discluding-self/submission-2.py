class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_prdct = 1
        output_array=[]
        for i in range(len(nums)):
            full_prdct *= nums[i]

        for j in range(len(nums)):
            if nums [j] == 0:
                k = 0
                res_0 = 1
                while( k < len(nums)):
                    if k != j:
                        res_0 *= nums[k]
                    k+=1
                output_array.append(res_0)
            else:
                res = full_prdct // nums[j]
                output_array.append(res)
        
        return output_array