def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dictionary):
    sorted_l = sorted(dictionary.items(), reverse=True, key=lambda x: x[1])
    for key, value in sorted_l:
        if key.isalpha():
            print(key + ":", value)




