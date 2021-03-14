# 
def generateDocument(characters, document):
    
    # chars dictionary
    chars_dict = {}
    for ch in characters:
        chars_dict[ch] = chars_dict.get(ch, 0) + 1
    
    for ch_doc in document:
        if ch_doc not in chars_dict:
            return False
        
        chars_dict[ch_doc] = chars_dict[ch_doc] - 1
        if chars_dict[ch_doc] < 0:
            return False

    return True
