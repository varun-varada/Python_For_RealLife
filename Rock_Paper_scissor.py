import random
class Game:
    def in_put():
        choice=input("Enter rock/paper/scissor: ").lower()
        while choice not in ['rock','paper','scissor']:
            print(f" Invaild input select again")
            return in_put()
        return choice
    def computer_selection():
        reuslt=random.choice(['rock','paper','scissor'])
        return reuslt
    def game(user_input,comp_result):
        if(comp_result==user_input):
            return "It's a draw"
        elif((user_input=='rock' and comp_result=='scissor') or (user_input=='scissor' and comp_result=='paper') or (user_input=='paper' and comp_result=='rock')):
          return 'User won'
        elif((user_input=='rock' and comp_result=='paper') or
              (user_input=='scissor' and comp_result=='rock') or
              (user_input=='paper' and comp_result=='scissor')):
         return 'Computer won'
        
i=Game.in_put()
c=Game.computer_selection()
print(c)
print(Game.game(i,c))