import random
import csv

csv_path = "./questions.csv"

class Question:
    def __init__(self, question, options):
        self.question = question
        self.answer = options[-1]

        self.shuffle_options(options)

    def is_response_correct(self, response):
        return response == self.options[self.answer]
    
    # options should be shuffled first as the answer is always the last option in the csv
    def shuffle_options(self, options):
        random.shuffle(options)
        self.options = {
            options[0]:"a",
            options[1]:"b",
            options[2]:"c",
            options[3]:"d",
        }
    
class Game:
    questions = []
    current_safety_net_amount = 0
    def __init__(self):
        self.load_questions(csv_path)
        
        print("Welcome to Who Wants To Be A Millionaire!")
        self.contestant_name = input("What is your name contestant? ")
        print("Welcome " + self.contestant_name + ", Let's get started!")

        for question in self.questions:
            index = 1
            print("\n" + str(index)+ ". " + question.question)
            for key, value in question.options.items():
                print(value + '. ' + key)
            response = input("Your response: ")
            index += 1
            print(question.is_response_correct(response))

        
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