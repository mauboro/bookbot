import string

def count_letters(text):
    res = {}
    for l in text:
        if l.lower() in res:
            pass
        else: 
            res.update({l.lower(): text.lower().count(l.lower())})
    return res

with open("books/frankenstein.txt", "r") as f:
    content = f.read()
    count = count_letters(content)
    print("\n".join([f"The '{k}' was found {v} times." for k, v in count.items() if k in string.ascii_lowercase]))




