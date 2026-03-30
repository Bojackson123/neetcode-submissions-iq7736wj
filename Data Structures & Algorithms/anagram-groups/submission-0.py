class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res_dict = defaultdict(list)
        for s in strs:
            res_dict[''.join(sorted(s))].append(s)

        res = []


        for k, v in res_dict.items():
            res.append(v)
        
        return res