'''Collects data for the hierarchical model study.'''

import random
import time
import os
import msvcrt

# The prompts. The first number means true (1) or false (0). The second number
# is the distance between the categories.
sentences = {'Pasadena is Pasadena.' : (1, 0),
             'Pasadena is in California.' : (1, 1),
             'Pasadena is in the United States.' : (1, 2),
             'Pasadena is in North America.' : (1, 3),
             'London is London.' : (1, 0),
             'London is in England.' : (1, 1),
             'London is in the United Kingdom.' : (1, 2),
             'London is in Europe.' : (1, 3),
             'Pasadena is London.' : (0, 0),
             'Pasadena is in England.' : (0, 1),
             'London is in California.' : (0, 1),
             'Pasadena is in the United Kingdom.' : (0, 2),
             'London is in the United States.' : (0, 2),
             'Pasadena is in Europe.' : (0, 3),
             'London is in North America.' : (0, 3)}

# The number of times each prompt will appear for each test subject.
numTrials = 4

class dataPoint():
    '''Represents a response to a prompt.'''
    
    def __init__(self, prompt, number, reactionTime, truth, correct, distance):
        '''Initializes with all the characteristics.'''
        self.prompt = prompt
        self.number = number
        self.reactionTime = reactionTime
        self.truth = truth
        self.correct = correct
        self.distance = distance
    
    def getInfo(self):
        '''Returns a tuple of all the characteristics.'''
        info = (self.prompt, self.number, self.reactionTime, self.truth,
                self.correct, self.distance)
        return info
        
    def getStringInfo(self):
        '''Returns a string with all the characteristics.'''
        info = self.prompt + '\n' + str(self.number) + '\n' +\
            str(self.reactionTime) + '\n' + str(self.truth) + '\n' +\
            str(self.correct) + '\n' + str(self.distance)
        return info

class dataPoints():
    '''Represents all responses of one test subject.'''
    
    def __init__(self, ID, data):
        '''Initalizes with the test subject ID and the list of data points.'''
        self.ID = ID
        self.data = data
    
    def getData(self):
        '''Returns the list of data points.'''
        return self.data[:]
    
    def save(self):
        '''Saves the responses of this test subject in a file.'''
        filename = 'test' + str(self.ID)
        f = open(filename, 'w')
        for dataPoint in self.data:
            f.write(dataPoint.getStringInfo())
            f.write('\n\n')
        f.close()


def intro():
    '''Explains the procedure to the test subject.'''
    os.system('cls')
    print "You will receive 60 prompts, one at a time."
    print "Each prompt can be true or false."
    print "Press k if it is true, and s if it is false."
    print "For example, if the prompt is 'A rose is a flower', press k."
    print "If the prompt is 'A rose is an animal', press s."
    print "Accuracy and speed are both important, but accuracy more so."
    print "However, don't worry if you get something wrong. Keep going."
    raw_input("Press Enter when you are ready to do two EXAMPLE prompts.")
    response = ''
    while response != 'k':
        os.system('cls')
        time.sleep(0.5)
        print "Boston is in the United States."
        response = msvcrt.getch()
    while response != 's':
        os.system('cls')
        time.sleep(0.5)        
        print "Paris is in North America."
        response = msvcrt.getch()
    os.system('cls')

def collect(ID):
    '''Used for testing. Displays prompts on the screen and returns a list of
    responses and their characteristics.'''
    data = []
    intro()
    print "You will now be presented with 60 REAL prompts."
    raw_input("Press Enter when you are ready to begin.")
    for i in range(numTrials):
        prompts = sentences.keys()
        # Randomize the order of the prompts.
        random.shuffle(prompts)
        for prompt in prompts:
            # Clear the screen and wait for 0.5 seconds.
            os.system('cls')
            time.sleep(0.5)
            # Print the prompt.
            print prompt
            t0 = time.clock()
            # Get the response.
            response = msvcrt.getch()
            t1 = time.clock()
            # Calculate how long it took the subject to respond.
            t = t1 - t0
            # Convert the response to 1 or 0.
            if response == 'k':
                response = 1
            else:
                response = 0
            # 1 if the prompt is true, 0 if it is false.
            truth = sentences[prompt][0]
            # Check if the response was correct.
            if response == truth:
                correct = 1
            else:
                correct = 0
            # The distance between category levels.
            distance = sentences[prompt][1]
            # Add the data point to the current list of data points.
            data.append(dataPoint(prompt, i + 1, t, truth, correct, distance))
    os.system('cls')    
    print "END"
    results = dataPoints(ID, data)
    results.save()

if __name__ == '__main__':
    while True:
        command = raw_input()
        if command == 'exit':
            break
        elif command == 'new':
            currentID = raw_input("Enter ID: ")
            collect(currentID)
        elif command == 'intro':
            intro()