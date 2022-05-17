import cgi
import json
import string
from collections import Counter
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path.endswith('/analyze'):
            self.send_response(200)
            self.send_header('Content-type', 'text/json; charset=utf-8')
            self.end_headers()
            ctype, pdict = cgi.parse_header(self.headers.get_content_type())

            if ctype != 'text/json':
                self.send_response(400)
                self.end_headers()
                return

            content_length = int(self.headers['Content-Length'])
            message = json.loads(self.rfile.read(content_length))
            response = {}
            words, length, wordCount = create_a_word_list(message['text'])
            response['wordCount'] = wordCount
            longest = find_longest_word(words)
            response['longestWord'] = longest
            language = find_language(words)
            response['language'] = language
            avgLength, letters = find_avg_length(words)
            response['avgLength'] = avgLength
            response['letters'] = letters
            alphabeticalMedian, alphabeticalMedianLength = find_median_word_by_alphabetically(words)
            response['alphabeticalMedian'] = {'word': alphabeticalMedian, 'length': alphabeticalMedianLength}
            medianWordByLength, medianWordByLengthLength = find_median_word_by_length(words)
            response['medianWordByLength'] = {'word': medianWordByLength, 'length': medianWordByLengthLength}
            mostFrequent = find_most_frequent_words(words)
            response['mostFrequent'] = mostFrequent
            duration = find_duration(words)
            response['duration'] = duration

            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            self.send_response(404)
            self.end_headers()


english_stop_words = ['stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were',
                      'was']
turkish_stop_words = ['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'birşey', 'biz', 'bu',
                      'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 'hep',
                      'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü', 'nasıl',
                      'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 'siz', 'şu',
                      'tüm', 've', 'veya', 'ya', 'yani']


def create_a_word_list(bare_text):
    text_without_escape_characters = bare_text.replace('\n\n', ' ')
    length = len(text_without_escape_characters)
    print(text_without_escape_characters)
    text_without_punctuation = text_without_escape_characters.translate(str.maketrans('', '', string.punctuation))
    print(text_without_punctuation)
    print(string.punctuation)
    words = text_without_punctuation.split()
    print(words)
    word_count = len(words)

    return words, length, word_count


def find_longest_word(wordList):
    longest_word = max(wordList, key=len)
    print(wordList)
    print(longest_word)
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
    avg_length = round(char_count / len(wordList), 2)
    return avg_length, char_count


def find_median_word_by_alphabetically(wordList):
    wordList.sort()
    median_word = wordList[int(len(wordList) / 2)]
    return median_word, len(median_word)


def find_median_word_by_length(wordList):
    wordList.sort(key=len)
    median_word_by_length = wordList[int(len(wordList) / 2)]
    return median_word_by_length, len(median_word_by_length)


def find_most_frequent_words(wordList):
    most_frequent = [pair[0] for pair in Counter(wordList).most_common(5)]
    return most_frequent


def find_duration(wordList):
    word_count = len(wordList)
    read_time = int(word_count / 265 * 60)
    return read_time


server = HTTPServer(('localhost', 9000), SimpleHTTPRequestHandler)
server.serve_forever()

#  curl -d '{    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
# }' -H "Content-Type: text/json" -X POST 127.0.0.1:9000/analyze
