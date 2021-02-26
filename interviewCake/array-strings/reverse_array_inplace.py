import unittest

# My Solution Works
def reverse_words(message):
    # reverse the words first
    word_start_index = 0
    for i in range(1, len(message)):
        if message[i] == ' ' or i == len(message) - 1:
            word_end_index = i - 1

            if i == len(message) - 1:
                word_end_index = i 

            while word_start_index < word_end_index:
                message[word_start_index], message[word_end_index] = message[word_end_index], message[word_start_index]
                word_start_index += 1
                word_end_index -= 1

            word_start_index = i+1

    # reverse the each character in message
    word_start_index = 0
    word_end_index = len(message) - 1

    while word_start_index <= word_end_index:
        message[word_start_index], message[word_end_index] = message[word_end_index], message[word_start_index]
        word_start_index += 1
        word_end_index -= 1

    return message


# print(reverse_words(['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd']))
# print(re/verse_words(['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd']))
# Tests
class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)