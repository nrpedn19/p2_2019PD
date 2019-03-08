####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Reisha&Nidhi' # Only 10 chars displayed.
strategy_name = 'Collude unless betrayed'
strategy_description = 'Always collude except when other player betrays, then two rounds later you betray'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)<2:
        return 'c'
    elif their_history[-2:-1]=='b':
        return 'b'
    else:
        return 'c'
    
#other two strategies
'''def move(my_history, their_history, my_score, their_score):
    return 'c'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) % 5 == 0:
        return 'b'
    else:
        return 'c'''
        

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.