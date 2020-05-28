import random

def question_numbers():
    
    while True:
        difficulty = input("Would you like the difficulty to be easy, medium, or hard? ").lower()
        
        if (difficulty == 'hard') or (difficulty == 'medium') or (difficulty == 'easy'):
            break
        else:
            print("Please enter one of three difficulties, not anyting else!")
            
    add_amount = int(input("How many addition questions would you like? "))
    sub_amount = int(input("How many subtraction questions would you like? "))
    mult_amount = int(input("How many multiplication questions would you like? "))
    div_amount = int(input("How many divsion questions would you like? "))
    
    return difficulty, add_amount, sub_amount, mult_amount, div_amount

def difficulty_to_range(difficulty):
    
    if difficulty == 'hard':
        add_range = 1000
        sub_range = 1000
        mult_range = 100
        div_range = 100
    
    elif difficulty == 'medium':
        add_range = 500
        sub_range = 500
        mult_range = 50
        div_range = 50
    
    elif difficulty == 'easy':
        add_range = 250
        sub_range = 250
        mult_range = 25
        div_range = 25
        
    return add_range, sub_range, mult_range, div_range
        
def addition_questions(add_amount,add_range):
    
    add_list = []
    
    for question in range (0,add_amount):
        first = random.randint(0,add_range)
        second = random.randint(0,add_range)
        add_question = ('What is {} + {}? '.format(first,second))
        
        for question1 in add_list:
            while True:
                if question1 == add_question:
                    first = random.randint(0,add_range)
                    second = random.randint(0,add_range)
                    add_question = ('What is {} + {}? '.format(first,second))
                
                else:
                    break
                    
        add_list.append(add_question)
        
    return add_list

def subtraction_questions(sub_amount,sub_range):
    
    sub_list = []
    
    for question in range (0,sub_amount):
        first = random.randint(0,sub_range)
        second = random.randint(0,sub_range)
        sub_question = ('What is {} - {}? '.format(first,second))
        
        for question1 in sub_list:
            while True:
                if question1 == sub_question:
                    first = random.randint(0,sub_range)
                    second = random.randint(0,sub_range)
                    sub_question = ('What is {} - {}? '.format(first,second))
                
                else:
                    break
                    
        sub_list.append(sub_question)
        
    return sub_list


def mult_questions(mult_amount,mult_range):
    
    mult_list = []
    
    for question in range (0,mult_amount):
        first = random.randint(0,mult_range)
        second = random.randint(0,mult_range)
        mult_question = ('What is {} x {}? '.format(first,second))
        
        for question1 in add_list:
            while True:
                if question1 == mult_question:
                    first = random.randint(0,mult_range)
                    second = random.randint(0,mult_range)
                    mult_question = ('What is {} x {}? '.format(first,second))
                
                else:
                    break
                    
        mult_list.append(mult_question)
        
    return mult_list

def div_questions(div_amount,div_range):
    
    div_list = []
    
    for question in range (0,div_amount):
        first = random.randint(0,div_range)
        possible_second = []
        for number in range(1,first+1):
            if first%number == 0:
                possible_second.append(number)
        second = random.choice(possible_second)
        div_question = ('What is {} / {}? '.format(first,second))
        
        for question1 in div_list:
            while True:
                if question1 == div_question:
                    first = random.randint(0,div_range)
                    possible_second = []
                    for number in range(1,first+1):
                        if first%number == 0:
                            possible_second.append(number)
                    second = random.choice(possible_second)
                    div_question = ('What is {} / {}? '.format(first,second))
                
                else:
                    break
                    
        div_list.append(div_question)
        
    return div_list

def test_prep(add_list, sub_list, mult_list, div_list):
    comb_list = add_list + sub_list + mult_list + div_list
    total_amount = len(comb_list)
    random.shuffle(comb_list)
    comb_list_answers = []
    
    for question in comb_list:
        for element in question:
            if (element == '+') or (element == '-') or (element == 'x') or (element == '/'):
                index = question.index(element)
        
        if question[index] == '+':
            first = ''
            second = ''
            for digit in question[:index-1]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    first += digit
            for digit in question[index+1:]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    second += digit
            first = int(first)
            second = int(second)
            answer = first + second
            comb_list_answers.append(answer)
        
        elif question[index] == '-':
            first = ''
            second = ''
            for digit in question[:index-1]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    first += digit
            for digit in question[index+1:]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    second += digit
            first = int(first)
            second = int(second)
            answer = first - second
            comb_list_answers.append(answer)
        
        elif question[index] == 'x':
            first = ''
            second = ''
            for digit in question[:index-1]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    first += digit
            for digit in question[index+1:]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    second += digit
            first = int(first)
            second = int(second)
            answer = first * second
            comb_list_answers.append(answer)
        
        elif question[index] == '/':
            first = ''
            second = ''
            for digit in question[:index-1]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    first += digit
            for digit in question[index+1:]:
                if digit in ['0','1','2','3','4','5','6','7','8','9',]:
                    second += digit
            first = int(first)
            second = int(second)
            answer = first / second
            comb_list_answers.append(answer)
        

    return comb_list, comb_list_answers, total_amount

def test(comb_list,comb_list_answers):
    print("Answer the following questions: ")
    
    correct  = 0
    
    for question in comb_list:
        index = comb_list.index(question)
        answer = comb_list_answers[index]
        user_answer = int(input(question))
        
        if user_answer == answer:
            correct += 1
        
    return correct        


def score(correct, total_amount):
    print("You finished the quiz! Congratulations!")
    print("You got {} out of {} in total!".format(correct, total_amount))

def play_again_func():
    
    while True:
        same_settings = input("Do you want to play with the same settings? ").lower()
        
        if (same_settings == 'yes') or (same_settings == 'no'):
            if same_settings == 'yes':
                play_same = True
                
            elif same_settings == 'no':
                play_same = False
                
            break
            
        else:
            print("Please say 'yes' or 'no', not anyting else")
            
    return play_same

def make_lines(number):
    for display in range(0,number):
        print()
    
    
x = 0 

while True:
    
    if x>=1:
        play_again = input("Do you want to play again? Yes or No? ").lower()

        if play_again == 'yes':
            play_same = play_again_func()
            if (play_same):
                make_lines(3)
                print("NOW IT'S TIME FOR THE QUIZ!!!")
                make_lines(2)
                add_list = addition_questions(add_amount,add_range)
                sub_list = subtraction_questions(sub_amount,sub_range)
                mult_list = mult_questions(mult_amount,mult_range)
                div_list = div_questions(div_amount,div_range)
                comb_list, comb_list_answers, total_amount = test_prep(add_list, sub_list, mult_list, div_list)
                correct = test(comb_list,comb_list_answers)
                make_lines(3)
                score(correct, total_amount)    
                make_lines(2)
                
            else:
                make_lines(3)
                difficulty, add_amount, sub_amount, mult_amount, div_amount = question_numbers()
                add_range, sub_range, mult_range, div_range = difficulty_to_range(difficulty)
                make_lines(4)
                print("NOW IT'S TIME FOR THE QUIZ!!!")
                make_lines(2)
                add_list = addition_questions(add_amount,add_range)
                sub_list = subtraction_questions(sub_amount,sub_range)
                mult_list = mult_questions(mult_amount,mult_range)
                div_list = div_questions(div_amount,div_range)
                comb_list, comb_list_answers, total_amount = test_prep(add_list, sub_list, mult_list, div_list)
                correct = test(comb_list,comb_list_answers)
                make_lines(3)
                score(correct, total_amount)    
                make_lines(2)
        
        elif play_again == 'no':
            break
        
        else:
            print("Please say 'yes' or 'no'!")
    else:
        print("Welcome to Math Mastermind!!!")
        make_lines(3)
        difficulty, add_amount, sub_amount, mult_amount, div_amount = question_numbers()
        add_range, sub_range, mult_range, div_range = difficulty_to_range(difficulty)
        make_lines(4)
        print("NOW IT'S TIME FOR THE QUIZ!!!")
        make_lines(2)
        add_list = addition_questions(add_amount,add_range)
        sub_list = subtraction_questions(sub_amount,sub_range)
        mult_list = mult_questions(mult_amount,mult_range)
        div_list = div_questions(div_amount,div_range)
        comb_list, comb_list_answers, total_amount = test_prep(add_list, sub_list, mult_list, div_list)
        correct = test(comb_list,comb_list_answers)
        make_lines(3)
        score(correct, total_amount)    
        make_lines(2)
        x += 1
    
make_lines(2)        
print("Thank you for playing!")
        
