import random

choices = 3				# excluding correct answer 
testing_period = 10
words = []
solution = []


# HELPER FUNCS
def optionify(raw):
	random.shuffle(raw)
	for i, option in enumerate(raw):
		print(chr(i + 97), ")", option)

def solution_helper(solution):
	print("-------------------------------------------")
	print(solution)


# PARSING
file = open("sample.txt", "r")

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

file.close()



# SELECT
for_test = random.sample(words, testing_period)

for i in range(testing_period):
	options = []
	print(for_test[i][0])

	solution.append(for_test[i][1])

	for j in range(choices):
		options.append(random.choice(words)[1])
	options.append(for_test[i][1])

	optionify(options)

solution_helper(solution)
