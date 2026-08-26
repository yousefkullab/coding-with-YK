# Note
# Joseph Language >>> j
# vowel a, e, i, o, u  >>> convert to >>> j

def translator(str):
    text = ""
    for letter in str:
        if letter.lower() in "aeiou":
            if letter.isupper():
                text = text + "Z"
            else:
                text = text + 'z'
        else:
            text = text + letter
    return text


text = input("Enter The Text To Translate: ")
print(translator(text))

