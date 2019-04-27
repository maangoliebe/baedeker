import random

file = open("sample.txt", "r")

words = []

for i, line in enumerate(file):
	print(i)
	tidy = line.split("/")
	
	words.append([])

	# add word into array
	words[i].append(tidy[0])

	# add definition
	words[i].append(tidy[1].strip())

	# add synonyms
	syns = [syn.strip() for syn in tidy[2].split(",")]
	words[i].append(syns)

print(random.choice(words)[0])


file.close()
