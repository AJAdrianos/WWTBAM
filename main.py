import random
import csv

csv_path = "./questions.csv"

class Question:
    def __init__(self, question, options):
        self.question = question
        self.answer = options[-1]
        self.incorrect_options = options[0:3]
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

    def remove_two_incorrect_options(self):
        # Remove any two options that are not our self.answer
        for i in range(2):
            self.options.pop(self.incorrect_options[i])
            
class Round:
    def __init__(self, amount, is_safety_round):
        self.amount = amount
        self.is_safety_round = is_safety_round

class Game:
    questions = []
    round_amounts = {
        1: Round(100, False),
        2: Round(200, False),
        3: Round(300, False),
        4: Round(500, False),
        5: Round(1000, True),
        6: Round(2000, False),
        7: Round(4000, False),
        8: Round(8000, False),
        9: Round(16000, False),
        10: Round(32000, True),
        11: Round(64000, False),
        12: Round(125000, False),
        13: Round(250000, False),
        14: Round(500000, False),
        15: Round(1000000, False)
    }
    first_lifeline_used = False
    game_lost = False

    def __init__(self):
        self.load_questions(csv_path)
        
        print("Welcome to Who Wants To Be A Millionaire!")
        self.contestant_name = input("What is your name contestant? ")
        print("Welcome " + self.contestant_name + ", Let's get started!")


    def play_game(self):
        question_index = 0
        while (self.game_lost == False)  and (question_index != 15):
            self.show_question(question_index)
            self.check_response(question_index)
            question_index += 1
        else:
            if (self.game_lost):
                # Trigger game over logic
                self.game_over(question_index)

            if (question_index >= 15):
                # Trigger win log 
                self.victory()


    def victory(self):
        # Player won the game
        return ""

    def game_over(self, index):
        question_number = index + 1
        is_first_safety_amount = question_number >= 5
        is_second_safety_amount = question_number >= 10
        if is_second_safety_amount:
            print("You may have lost this game but you still get to walk away with R" + str(self.round_amounts[10].amount))
            return
        if is_first_safety_amount:
            print("You may have lost this game but you still get to walk away with R" + str(self.round_amounts[5].amount))
            return
        else:    
            print("Thank you for your time...")
        print("We will see you all again next week, same time, same place on WHo WANTS TO BE A MILLIONAIRE")


    def show_question(self, index):
        question = self.questions[index]
        print("\n")
        print(str(index + 1) + ". " + question.question)
        for key,value in question.options.items():
            print(value + ". " + key)

    def display_question(self, question):
        print(question.question)
        for key,value in question.options.items():
            print(value + ". " + key)

    def check_response(self, curr_question_index):
        question = self.questions[curr_question_index]
        response_valid = False
        while not response_valid:  
            response = input("Your response: ")
            if response == "1":
                # First Lifeline
                if self.first_lifeline_used == False:
                    question.remove_two_incorrect_options()
                    print("You have chosen to use the lifeline: remove two incorrect options")
                    print("This lifeline will no longer be available for use")
                    print("Please answer the following question...")
                    self.display_question(question=question)
                else: 
                    print("You have already used this lifeline!")
            
            else:
                # no lifeline is used so check if answer is correct
                response_valid = self.is_response_valid(response)
                if not response_valid:
                    print(response + " is not an option")
                    print("Please select an option from the ones provided!")
                else:
                    self.game_lost = not question.is_response_correct(response)

    def is_response_valid(self, response):
        if (response == "a" or response == "b" or response == "c" or response == "d"):
            return True
        return False

    def load_questions(self, csv_path):
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                question_to_ask = row[0]
                options = row[-4:]
                question = Question(question_to_ask, options)
                self.questions.append(question)

if __name__ == '__main__':
    game = Game()
    game.play_game()