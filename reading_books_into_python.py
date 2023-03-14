#read a book and return it as a string
def read_book(title_path):  
    with open(title_path, "r", encoding ="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

read_book("./Books_EngFr/Books_EngFr/French/diderot/L'oiseau blanc.txt")