from wordcloud import WordCloud


def get_frequency_list(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    for word in file_contents.split(" "):
        # clean up any punctuation marks
        cleaned_up_word = ""
        for ch in word:
            if ch.isalpha():
                cleaned_up_word += ch

        if cleaned_up_word not in uninteresting_words:
            frequency_list[cleaned_up_word] = frequency_list.get(cleaned_up_word, 0) + 1

    return frequency_list

def get_uninteresting_words():
    uninteresting_set = { 'a', 'an', 'the', 'to', 'if', 'else', 'is' }
    return uninteresting_set

def read_from_file():
    data = None
    with open("text.txt", "r") as file:
        data = file.read().replace('\n', ' ')
    return data

if __name__ == "__main__":
    file_data = read_from_file()
    if not file_data:
        raise Exception("No data found in file! WTF")
    
    frequency_list = get_frequency_list(file_data)
    print(frequency_list)
    cloud = WordCloud()
    cloud.generate_from_frequencies(frequency_list)
    cloud.to_file("myfile.jpg")

