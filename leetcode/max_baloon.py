# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         if text == "balloon":
#             return 1

#         ballon_word_count = {
#             'b': 1,
#             'a': 1,
#             'l': 2,
#             'o': 2,
#             'n': 1
#         }
#         ballon_count = 0
#         for ch in text:
#             isBallonExists = ballon_word_count.get(ch, -1)
#             print(ch,isBallonExists)
#             if isBallonExists >= 1:
#                 ballon_word_count[ch] -= 1
#                 # check if all keys in ballon_word_count is 0
#                 if self.isABallon(ballon_word_count):
#                     ballon_count += 1
#                     ballon_word_count = {
#                         'b': 1,
#                         'a': 1,
#                         'l': 2,
#                         'o': 2,
#                         'n': 1
#                     }
#             elif isBallonExists == 0:
#                 if self.isABallon(ballon_word_count):
#                     ballon_count += 1
#                     ballon_word_count = {
#                         'b': 1,
#                         'a': 1,
#                         'l': 2,
#                         'o': 2,
#                         'n': 1
#                     }

#         return ballon_count
    
#     def isABallon(self, ballon_dict):
#         print(ballon_dict)
#         for val in ballon_dict.values():
#             if val != 0:
#                 return False
#         return True

# x = Solution()
# # print(x.maxNumberOfBalloons("nlaebolko"))
# # print(x.maxNumberOfBalloons("loonbalxballpoon"))

# # correct: 10
# print(x.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if text == 'balloon':
            return 1
        balloon_dict = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        # populate dictionary
        for ch in text:
            if ch in balloon_dict.keys():
                balloon_dict[ch] += 1
            
        # count balloons
        count_balloon = len(text)
        for key in balloon_dict.keys():
            if key == 'l' or key == 'o':
                if int(balloon_dict[key]/2) < count_balloon:
                    count_balloon = int(balloon_dict[key]/2)
            else:
                if balloon_dict[key] < count_balloon:
                    count_balloon = balloon_dict[key]

        return count_balloon

x = Solution()
print(x.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
