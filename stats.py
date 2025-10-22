
def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    text = text.lower()
    characters = {}

    for c in text:
        characters[c] = characters.get(c, 0) + 1
    return characters

#def stats(text):
   # word_count(text)
    #character_count(text)

#stats()
