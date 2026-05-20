from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_str = defaultdict(list)
        k=""
        for i in strs:
            k = "".join(sorted(i))

            grouped_str[k].append(i)

        return [i[1] for i in grouped_str.items()]