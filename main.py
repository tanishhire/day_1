import math 
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

# Name your function appropriately and think carefully about the signature
# Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms
# Use descriptive variable names, otherwise you may forget what a variable represents


def locate_card(cards, query):
    position = 0
    
    while True:
        if cards[position] == query:
            print(position)
            return position
        position += 1
        
        if position == len(cards):
            print(position)
            return -1


test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}
tests = []
tests.append(test)


# query occurs in the middle
tests.append({
    'input' : {
        'cards' : [13,11,10,7,4,3,1,0],
        'query': 1
    },
    'output' : 6
})

# query is the first element
tests.append({
    'input': {
        'cards' : [4,2,1,-1],
        'query' : 4
    },
    'output' : 0
})

# querty is the last element
tests.append({
    'input': {
        'cards' : [3, -1, 9, -127],
        'query' : -127
    },
    'output': 3
})

# cards containes just one element
tests.append({
    'input' : {
        'cards' : [6],
        'query' : 6
    },
    'output' : 0
})

# card does not contain query
tests.append({
    "input" : {
        'cards' : [9,7,5,2,-9],
        "query" : 4
    },
    'output' : -1
})

# card is empty

tests.append({
    'input' : {
        'cards' : [],
        "query" : 1
    },
    'output' : -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# print(tests)

evaluate_test_cases(locate_card, tests)

