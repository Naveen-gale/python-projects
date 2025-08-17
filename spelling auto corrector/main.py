from textblob import TextBlob


for i in range(5):
    words = input("Enter a word: ")
    print("wrong Word: ", words)  

    corrected_word = TextBlob(words).correct()
    print("Corrected Word: ", corrected_word)