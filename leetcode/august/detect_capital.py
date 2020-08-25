class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = []
        lowers = []
        for el in word:
            if ord(el) >= 65 and ord(el) <= 90:
                caps.append(el)
            else:
                lowers.append(el)
                
        if len(caps) == len(word) or len(lowers) == len(word):
            return True
        elif len(caps) == 1 and caps[0] == list(word)[0]:
            return True
        
        return False
                