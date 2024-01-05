import random
import csv

csv_path = "./questions.csv"

class Question:
    def __init__(self, question, options):
        self.options = options
        self.question = question

        self.answer = self.options[-1]

        self.shuffle_options()

    def is_response_correct(self, response):
        return response == self.answer
    
    # options should be shuffled first as the answer is always the last option in the csv
    def shuffle_options(self):
        random.shuffle(self.options)
    
class Game:
    questions = []
    def __init__(self):
        self.load_questions(csv_path)
        
        print("Welcome to Who Wants To Be A Millionaire!")
        self.contestant_name = input("What is your name contestant? ")
        print("Welcome " + self.contestant_name + ", Let's get started!")

        print("1." + self.questions[0].question)
        print("a. {optionA}                                    b. {optionB} \nc. {optionC}                                    d. {optionD}".format(optionA=self.questions[0].options[0],optionB=self.questions[0].options[1],optionC=self.questions[0].options[2],optionD=self.questions[0].options[3]))

    def load_questions(self, csv_path):
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                question_to_ask = row[0]
                options = row[-4:]
                question = Question(question_to_ask, options)
                self.questions.append(question)

    def show_question(self, question_number):
        #ww
        return False

if __name__ == '__main__':
    game = Game()