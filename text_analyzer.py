from collections import Counter
import os
import pandas as pd

def read_book(title_path):  #Reading text form file path.
    with open(title_path, "r", encoding ="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def count_words_fast(text): #Counting differnt words in text.
    text = text.lower()
    skips = [".", ", ", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

#word_counts = count_words_fast(text)
def word_stats(word_counts):    #Checking all unique words in text.
    num_unique = len(word_counts)
    #counts = word_counts.values()
    #return (num_unique, counts)
    return num_unique

book_dir = "./Books"
os.listdir(book_dir)

stats = pd.DataFrame(columns =("language",
							"author",
							"title",
							"length",
							"unique"))

# check >>>stats
title_num = 1
for language in os.listdir(book_dir):
	for author in os.listdir(book_dir+"/"+language):
		for title in os.listdir(book_dir+"/"+language+"/"+author):
			
			inputfile = book_dir+"/"+language+"/"+author+"/"+title
			print(inputfile)
			text = read_book(inputfile)
			(num_unique, counts) = word_stats(count_words_fast(text))
			stats.loc[title_num]= language,
			author.capitalize(),
			title.replace(".txt", ""),
			sum(counts), num_unique
			title_num+= 1
import matplotlib.pyplot as plt
plt.plot(stats.length, stats.unique, "bo-")

plt.loglog(stats.length, stats.unique, "ro")

stats[stats.language =="English"] #to check information on english books
	
plt.figure(figsize =(10, 10))
subset = stats[stats.language =="English"]
plt.loglog(subset.length,
		subset.unique,
		"o",
		label ="English",
		color ="crimson")

subset = stats[stats.language =="French"]
plt.loglog(subset.length,
		subset.unique,
		"o",
		label ="French",
		color ="forestgreen")

subset = stats[stats.language =="German"]
plt.loglog(subset.length,
		subset.unique,
		"o",
		label ="German",
		color ="orange")

subset = stats[stats.language =="Portuguese"]
plt.loglog(subset.length,
		subset.unique,
		"o",
		label ="Portuguese",
		color ="blueviolet")

#plt.legend()
#plt.xlabel("Book Length")
#plt.ylabel("Number of Unique words")
#plt.savefig("fig.pdf")
#plt.show()

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

graph = input("Press D to Plotting Graph: ")

if graph == "D":
    plt.legend()
    plt.xlabel("Book Length")
    plt.ylabel("Number of Unique words")
    plt.savefig("fig.pdf")
    plt.show()