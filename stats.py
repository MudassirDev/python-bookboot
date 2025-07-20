def get_words_count(content:str):
    list_of_words = content.split()
    return len(list_of_words)

def get_chars_count(content:str):
    chars = {}
    for c in content:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_dicts(chars:dict):
    list = []
    for key in chars:
        list.append({
            "char": key,
            "num": chars[key]
        })
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(item:dict):
    return item["num"]
