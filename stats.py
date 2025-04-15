def word_count(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    lower = text.lower()
    get_char = {}
    for char in lower:
        if char not in get_char:
            get_char[char] = 1
        else:
            get_char[char] += 1
    return get_char


def sort_on(dict):
    return dict["num"]


def sort_list(dict):
    list_dict = []
    for ch in dict:
        list_dict.append({"char": ch, "num": dict[ch]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
