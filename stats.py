def get_book_wordcount(book_text):
    words = book_text.split()
    return len(words)

def counting_characters(book_text):
    character_counted = {}
    lowercase_text = book_text.lower()
    for char in lowercase_text:
        if char not in character_counted:
                character_counted[char] = 1
        else:
            character_counted[char] += 1
    return character_counted

def sort_on(d):
    return d["num"]
 
def dictionary_sorter(characters_counted):
    empty_list = []
    for char, count in characters_counted.items():
        temp_dict = {"char": char, "num": count}
        empty_list.append(temp_dict)
    # next you’ll sort empty_list with .sort(reverse=True, key=sort_on)
    empty_list.sort(reverse=True, key=sort_on)
    return empty_list

