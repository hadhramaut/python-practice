#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):  # 35 is the number of quizes 
    quizFile = open('capital_quiz_{}.txt'.format(quizNum + 1), 'w')
    answerKeyFile = open('quiz_keys_{}.txt'.format(quizNum + 1), 'w')

    quizFile.write("Name\nDate\nPeriod\n")
    quizFile.write((' ' * 20) + 'State Capital Quiz {}'.format(quizNum + 1))  # Indent
    quizFile.write('\n\n')

    states = list(capitals.keys())  # Create list with state names
    random.shuffle(states)  # Mix the list
    stateNumber = 0
    
    for state in states:

        stateNumber += 1

        correctAnswer = capitals[state]
        allAnswers = list(capitals.values())
        del allAnswers[allAnswers.index(correctAnswer)]  # Delete correct answer from the list
        wrongAnswers = random.sample(allAnswers, 3)  # Specify 3 wrong answers
        answerOptions = wrongAnswers + [correctAnswer]  # Create list with all answer variants
        random.shuffle(answerOptions)  # Mix the final list

        quizFile.write(('{}. Select the capital of {} state\n\n'.format(stateNumber, state)))
        for i in range(4):
            quizFile.write('{}: {}\n'.format('ABCD'[i], answerOptions[i]))
        quizFile.write('\n\n')
        answerKeyFile.write('{}. {}\n\n'.format(stateNumber, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
