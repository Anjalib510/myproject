import random

# simple text used for training
text = "generative ai is very useful generative ai can create text and images"

# convert the text into words
words = text.split()

# dictionary to store word relations
markov = {}

# building the markov chain
for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]

    if word not in markov:
        markov[word] = []

    markov[word].append(next_word)

# choose starting word randomly
current = random.choice(words)

# start sentence
sentence = current

# generate new text
for i in range(8):
    if current in markov:
        next_word = random.choice(markov[current])
        sentence = sentence + " " + next_word
        current = next_word
    else:
        break

# display result
print("Generated sentence is:")
print(sentence)