sentence = input("Enter a sentence\n")

newSentence = ""
pastFirstWord = False

for word in sentence.split():
    if pastFirstWord:
        newSentence += word.capitalize()
    else:
        newSentence += word.lower()
    pastFirstWord = True

print(newSentence)
