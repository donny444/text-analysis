from collections import Counter

text = "This is my test text. We're keeping this text short to keep things manageable."
text = text.lower()

#read a book and return it as a string
def read_book(title_path):  
    with open(title_path, "r", encoding ="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text
#print(read_book("Books_EngFr/Books_EngFr/French/diderot/L'oiseau blanc.txt"))

#counts word frequency
def count_words(text):
    skips = [".", ", ", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
#print(count_words(text))#You can check the function

#counts word frequency using Counter from collections
def count_words_fast(text):
    text = text.lower()
    skips = [".", ", ", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts
#print(count_words_fast(text))#You can check the function

word_counts = count_words_fast(text)
def word_stats(word_counts):
    num_unique = len(word_counts)
    #counts = word_counts.values()
    #return (num_unique, counts)
    return num_unique

#print(word_stats(word_counts))