'''Coding Exercise: Reading Questions and Writing Results
Write a program that:

Reads questions from a file named questions.txt.✅
Each line in the file will contain a question and its answer in the format:
question=answer✅
Strip any line breaks from each line and append them into a list.✅
For each question:

Split the line using = to separate the question and the answer.✅
Print the question and wait for the user to input their answer.✅
Check if the user’s input matches the correct answer and update their score accordingly. ✅
At the end of the program:

Write the user's final score into a file named result.txt in the following format:✅
"Your final score is X/Y.
(Replace X with the score and Y with the total number of questions.)'''

import os

question_file = os.path.join(os.getcwd(),'questions.txt')
result_file = os.path.join(os.getcwd(),'result.txt')
with open(question_file,'r') as file:
	questions=file.readlines()
file.close()

questions = [question.strip() for question in questions]
questions_answers = [question.split('=') for question in questions]

mark = 0
for question,answer in questions_answers :

	try:
		user_inputs = input(f"{question}: ").split(" ")
		if len(user_inputs)>1:
			user_inputs = [user_input.lower().capitalize() for user_input in user_inputs]
			user_input = " ".join(user_inputs)
		else :
			user_input = user_inputs[0].lower().capitalize()
	except Exception as e:
		raise e
	if answer.strip() == user_input:
		print("Correct!")
		mark+=1
	else:
		print("Incorrect")
		print(answer)
final_score = f"Your final score is {mark}/{len(questions)}"
# Writing the result to a file

with open(result_file, 'w') as file:
	file.write(final_score)
file.close()