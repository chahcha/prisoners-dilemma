####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
########
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Genji'
strategy_name = 'Be cool until they betray'
strategy_description = 'Dont cheat.'
    
def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history:
        return 'b'
    else:
        return 'c'
   
    
    