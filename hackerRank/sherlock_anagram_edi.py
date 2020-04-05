import string

# taking the input of the number of strings to take input
q = int(input())
# ascii_lowercase will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.
ALPHABET = string.ascii_lowercase

for i in range(q):
    # take each input as string and store in s
    s = input()
    # the dictionary to hold
    signatures = {}

    # this will hold the count of corresponding characters in each input string
    # signature = [0,0,0,0,......]
    signature = [0 for ch in ALPHABET]
    for letter in s:
        # ord() converts chracters to corresponding ascii value
        signature[ord(letter) - ord(ALPHABET[0])] += 1
    # signature now contains the count to each chracters in the string

    # iterate over all substrings of s
    for start in range(len(s)):
        for finish in range(start, len(s)):
            # initialize substring signatures
            signature = [0 for ch in ALPHABET]
            for letter in s[start:finish+1]:
                signature[ord(letter) - ord(ALPHABET[0])] += 1

            # why tuple? -> here it is used as a key in the signatures dictionary
            signature = tuple(signature)
            signatures[signature] = signatures.get(signature, 0) + 1

    res = 0
    # DID NOT understand this?
    for count in signatures.values():
        # print("Count: ", count)
        res += count*(count-1)/2

    print(res)
