import sys

words = sys.stdin.readline().rstrip('\n')
wordsList = []

for _ in range(len(words)):
    wordsList.append(words)
    words = words[1:]

for i in sorted(wordsList):
    print(i)