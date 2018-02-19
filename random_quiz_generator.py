# radnom_quiz_generator.py - generates 35 randomized tests with answer sheets included
# the tests are on states and their capitals

import random


capitals = {
	'Alabama' : 'Montgomery',
	'Alaska' : 'Juneau',
	'Arizona' : 'Phoenix',
	'Arkansas' : 'Little Rock',
	'California' : 'Sacramento',	
	'Colorado': 'Denver',	
	'Connecticut' : 'Hartford',
	'Delaware': 'Dover',
	'Florida' : 'Tallahassee',
	'Georgia' : 'Atlanta',
	'Hawaii' : 'Honolulu',	
	'Idaho' : 'Boise',	
	'Illinois' : 'Springfield',	
	'Indiana' : 'Indianapolis',
	'Iowa' : 'Des Moines',
	'Kansas' : 'Topeka',
	'Kentucky' : 'Frankfort',
	'Louisiana' : 'Baton Rouge',	
	'Maine' : 'Augusta',
	'Maryland' : 'Annapolis',
	'Massachusetts' : 'Boston',
	'Michigan' : 'Lansing',	
	'Minnesota' : 'St. Paul',
	'Mississippi' : 'Jackson',	
	'Missouri' : 'Jefferson City',
	'Montana' :	'Helena',
	'Nebraska' : 'Lincoln',
	'Nevada' : 'Carson City',
	'New Hampshire' : 'Concord',
	'New Jersey' : 'Trenton',
	'New Mexico' : 'Santa Fe',
	'New York' : 'Albany',
	'North Carolina' : 'Raleigh',
	'North Dakota' : 'Bismarck',
	'Ohio' : 'Columbus',
	'Oklahoma' : 'Oklahoma City',
	'Oregon' : 'Salem',
	'Pennsylvania' : 'Harrisburg',
	'Rhode Island' : 'Providence',
	'South Carolina' : 'Columbia',
	'South Dakota' : 'Pierre',
	'Tennessee' : 'Nashville',
	'Texas' : 'Austin',
	'Utah' : 'Salt Lake City',
	'Vermont' : 'Montpelier',
	'Virginia' : 'Richmond',
	'Washington' : 'Olympia',
	'West Virginia' : 'Charleston',
	'Wisconsin' : 'Madison',
	'Wyoming' : 'Cheyenne'
}

for quiz_number in range(35):
	#Creates the quize and answer key files 
	quiz_file = open('./Quiz_capitals/catpitalsquiz%s.txt' % (quiz_number+1), 'w')
	answer_key_file = open('./Quiz_capitals/answerkey%s.txt' % (quiz_number+1), 'w')

	#Write out the header for the quiz:
	quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quiz_file.write((' ' * 20) + 'State Capital Quiz (Form %s)' % (quiz_number+1))
	quiz_file.write('\n\n')

	#Shuffle through all the states
	states = list(capitals.keys())
	random.shuffle(states)


	# Loop through all 50 states
	for question_number in range(50):

		#Get right and wrong answers.
		correct_answer = capitals[states[question_number]]
		wrong_answers = list(capitals.values())
		# will remove the correct answer from the wrong answer list
		del wrong_answers[wrong_answers.index(correct_answer)]
		# will pull three random wrong answers from the wrong answer list
		wrong_answers = random.sample(wrong_answers, 3)
		# all possible answers on the test
		answer_opions = wrong_answers + [correct_answer]
		# these kids are really gonna have a hard time with this
		random.shuffle(answer_opions)


		#Write the question and the answer options to the quiz file
		quiz_file.write('%s. What is the capital of %s?\n' %(question_number+1, states[question_number]))

		for i in range(4):
			# A. blah
			quiz_file.write('    %s. %s\n' % ('ABCD'[i], answer_opions[i]))
		quiz_file.write('\n')

		#Write the anser key file:
		answer_key_file.write('%s. %s\n' % (quiz_number+1, 'ABCD'[answer_opions.index(correct_answer)]))

	# time to close everything up!
	quiz_file.close()
	answer_key_file.close()
	
