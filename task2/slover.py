from collections import defaultdict

words = input().split()

wordFrequency = defaultdict(int)
maxFrequency = 0

for word in words:
    wordFrequency[word] += 1
    if wordFrequency[word] > maxFrequency:
        maxFrequency = wordFrequency[word]

sortedWords = sorted(wordFrequency.keys(), key=lambda w: wordFrequency[w])
maxWordLength = len(max(sortedWords, key=len))

for word in sortedWords:
    frequency = wordFrequency[word]
    barLength = int(round((frequency * 10.0) / maxFrequency))
    wordColumn = word.rjust(maxWordLength, '_')
    barColumn = '.' * barLength

    print(f"{wordColumn} {barColumn}")
