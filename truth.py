import random

def t_question():
   with open('t_question.txt', 'r') as f:
      
      t_questions = f.readlines()

   return random.choice(t_questions)


if __name__ == '__main__':
   t_question()