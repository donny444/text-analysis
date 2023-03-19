from modules import read_book, count_words_fast, word_stats

print("Welcome to Text Analyzer")
print("[1] Read Book")
print("[2] Count Words")
print("[3] Total Unique Words\n")
select = int(input("Please select the options above: "))

if select == 1:
    text = str(input("Please insert the file path: "))
    print(read_book(text))
elif select == 2:
    text = str(input("Please insert the text: "))
    print(count_words_fast(text))
elif select == 3:
    text = str(input("Please insert the text: "))
    text = count_words_fast(text)
    print(word_stats(text))
else:
    print("Select only '1' or '2'")