class Solution:
    def reformat(self, s: str) -> str:
        al_count = 0
        num_count = 0

        al_list = []
        num_list = []
        output_str = ''

        for ch in s:
            if ord(ch) >= 97 and ord(ch) <= 122:
                al_count += 1
                al_list.append(ch)
            else:
                num_count += 1
                num_list.append(ch)

        if abs(al_count - num_count) > 1:
            return ''

        al_index = 0
        num_index = 0

        if al_count == num_count:
            for i in range(len(s)):
                if i%2:
                    output_str += al_list[al_index]
                    al_index += 1
                else:
                    output_str += num_list[num_index]
                    num_index += 1
        
        
        elif al_count > num_count:
            al_index = 0
            output_str += al_list[al_index]
            al_index += 1
            for i in range(1, len(s)):
                if i%2:
                    output_str += num_list[num_index]
                    num_index += 1
                else:
                    output_str += al_list[al_index]
                    al_index += 1
                    
        
        elif al_count < num_count:
            num_index = 0
            output_str += num_list[num_index]
            num_index += 1
            for i in range(1, len(s)):
                if i%2:
                    output_str += al_list[al_index]
                    al_index += 1
                else:
                    output_str += num_list[num_index]
                    num_index += 1

        return output_str

        
x = Solution()
print(x.reformat("a0b1c2"))
print(x.reformat("leetcode"))
print(x.reformat("1229857369"))
print(x.reformat("covid2019"))
print(x.reformat("ab123"))