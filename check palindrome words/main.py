word = input("enter any word: ")
reversed_word = word[::-1]

if word == reversed_word:
            print(reversed_word)
            print("The word is a palindrome")
else:
            print(reversed_word)
            print("The word is not a palindrome")