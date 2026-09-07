class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for w in strs:
            counts=[0]*26 #counts of each letter in their respective positions, will act as key for the hashmap 
            for c in w:
                counts[ord(c)-ord("a")]+=1
            hashmap[tuple(counts)].append(w)
        return hashmap.values()

        