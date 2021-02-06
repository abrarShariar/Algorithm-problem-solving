def caesarCipherEncryptor(string, key):
    result_string = ""
    for i in range(len(string)):
        current_ch_val = ord(string[i])
        target_ch_val = current_ch_val + key

        while target_ch_val > ord('z'):
            diff = target_ch_val - ord('z')
            target_ch_val = ord('a') + diff - 1
        
        result_string += chr(target_ch_val)
    
    return result_string


print(caesarCipherEncryptor("xyz", 2))
print(caesarCipherEncryptor("abc", 52))


