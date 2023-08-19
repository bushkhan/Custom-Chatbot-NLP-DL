import nltk
# nltk.download("punkt")
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())


a = "I think I have anxiety"
a = tokenize(a)

words = ['stressed', 'stressing', 'stress']
stemmed_words = [stem(i) for i in words] 


def bag_of_words(tokenized_sentence,all_words):
    pass




