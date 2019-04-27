import random

file = open("sample.txt", "r")

testing_period = 4
words = []

for i, line in enumerate(file):
	tidy = line.split("/")
	
	words.append([])

	# add word into array
	words[i].append(tidy[0].strip())

	# add definition
	words[i].append(tidy[1].strip())

	# add synonyms
	syns = [syn.strip() for syn in tidy[2].split(",")]
	words[i].append(syns)


for_test = random.sample(words, testing_period)
for i in range(testing_period):
	print(for_test[i][0])


file.close()
