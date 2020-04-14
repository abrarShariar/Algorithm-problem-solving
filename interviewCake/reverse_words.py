import unittest

def reverse_words(message):
    # Decode the message by reversing the words
    # reverse all chars
    last_index = len(message) - 1
    start_index = 0
    message = reverseShit(start_index, last_index, message)

    # find the next space
    start_index = 0
    while start_index < len(message):
        last_index = getLastIndex(start_index, message)
        message = reverseShit(start_index, last_index, message)
        start_index = last_index + 2

    return message

def reverseShit(start_index, last_index, message):
    while start_index < last_index:
        message[start_index], message[last_index] = message[last_index], message[start_index]
        start_index += 1
        last_index -= 1

    return message

def getLastIndex(start_index, message):
    last_index = start_index
    while message[last_index] != ' ' and last_index < len(message):
        last_index += 1
        if last_index >= len(message):
            break
    return last_index - 1

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
