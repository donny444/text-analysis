from collections import Counter

text = "This is my test text. We're keeping this text short to keep things manageable."
text = text.lower()

# counts word frequency
def count_words(text):                  
    skips = [".", ", ", ":", ";", "'", '"'] 
    for ch in skips: 
        text = text.replace(ch, "") 
    word_counts = {} 
    for word in text.split(" "): 
        if word in word_counts: 
            word_counts[word]+= 1 
        else: 
            word_counts[word]= 1 
    return word_counts 
  
#count_words(text)#You can check the function 
  
# counts word frequency using
# Counter from collections 
def count_words_fast(text):     
    text = text.lower() 
    skips = [".", ", ", ":", ";", "'", '"'] 
    for ch in skips: 
        text = text.replace(ch, "") 
    word_counts = Counter(text.split(" ")) 
    return word_counts 
  
#count_words_fast(text)#You can check the function