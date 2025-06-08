def get_num_words(text):
    text = text.split()
    return len(text)

def get_num_occurrence(text):
    emptydict = {}
    text = text.lower()
    for char in text:
        if char in emptydict:
            emptydict[char] += 1
        else:
            emptydict[char] = 1
    return emptydict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
