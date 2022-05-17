import string
from collections import Counter
text = "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing. " \
       "However, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place. " \
       "Neurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."

text_2 = 'Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered ' \
       'through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too ' \
       'much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch ' \
       'pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing ' \
       'sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages ' \
       'from both our bodies and the surrounding world.'
text_3 = text_2.replace('\n\n', ' ').replace('\n', ' ').replace('\t', ' ')
print(text_3)

english_stop_words = ['stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were', 'was']
turkish_stop_words = ['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'birşey', 'biz', 'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü', 'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani']


def create_a_word_list(bare_text):

    text_without_escape_characters = bare_text.replace('\n\n', ' ')
    length = len(text_without_escape_characters)

    text_without_punctuation = text_without_escape_characters.translate(str.maketrans('', '', string.punctuation))
    words = text_without_punctuation.split()
    word_count = len(words)

    return words, length, word_count


def find_longest_word(wordList):
    longest_word = max(wordList, key=len)
    return longest_word


def find_language(wordList):
    turkish_threshold = 0
    english_threshold = 0
    for word in wordList:
        if word in turkish_stop_words:
            turkish_threshold += 1
        if word in english_stop_words:
            english_threshold += 1
    language = 'Turkish' if turkish_threshold > english_threshold else 'English'
    return language


def find_avg_length(wordList):
    char_count = 0
    for word in wordList:
        char_count += len(word)
    avg_length = char_count/len(wordList)
    return avg_length, char_count


def find_median_word_by_alphabetically(wordList):
    wordList.sort()
    median_word = wordList[int(len(wordList)/2)]
    return median_word, len(median_word)


def find_median_word_by_length(wordList):
    wordList.sort(key=len)
    median_word_by_length = wordList[int(len(wordList)/2)]
    return median_word_by_length, len(median_word_by_length)


def find_most_frequent_words(wordList):
    most_frequent = [pair[0] for pair in Counter(wordList).most_common(5)]
    return most_frequent


words,length,word_count = create_a_word_list(text_2)
print(words)
print(length)
print(find_longest_word(words))
print(find_language(words))
print(find_avg_length(words))
print(find_median_word_by_alphabetically(words))
print(find_median_word_by_length(words))
print(find_most_frequent_words(words))

