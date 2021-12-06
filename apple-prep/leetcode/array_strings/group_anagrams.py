# SOLVED!
class Solution:
    def groupAnagrams(self, strs):
        # sort each string in alphabetical order
        result_list = []
        original_str_index_map = {}

        for i in range(len(strs)):
            st = strs[i]
            st = str(sorted(list(st)))
            original_str_index_map[st] = original_str_index_map.get(st, []) + [i]

        # now original str index has all the indices of a particular str
        for (key, value) in original_str_index_map.items():
            temp_list = []
            for index in value:
                temp_list.append(strs[index])
            result_list.append(temp_list)

        return result_list


