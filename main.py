from collections import defaultdict, Counter

prompt = input("Word: ")

def readTextFromFile(file_path): # Given a file path (.txt), turns all text into a string
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def nextWord(data, prompt): # nextWord takes a large string of words and the prompt the user entered to produce the word that is most likely to follow.

    followingWords = [] # Lits of words that follow

    for i in range(len(data) - 1): # Iterates through every word in our data
        if data[i].lower() == prompt.lower(): # If the words are euqal, the following word is stored in followingWords
            followingWords.append(data[i + 1])


    if not followingWords:  # The program returns if the word is not followed by anthing or does not exist in teh data
        return "None found"

    wordCounts = Counter(followingWords) # Counts the number of each word in the followingWords list
    mostCommonWord, frequency = wordCounts.most_common(1)[0] # Gets and returns the most commonly appearing word

    return mostCommonWord

data = readTextFromFile(r'C:\Users\Mahya\PycharmProjects\Word Completer\.venv\data.txt')
data = data.split()
sentence = ""

for i in range(20):
    sentence = sentence + nextWord(data, prompt) + " "
    prompt = nextWord(data, prompt)

print(sentence)


