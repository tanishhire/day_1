# import math 
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases


# def test_location(cards, query, mid):
#     mid_number = cards[mid]
#     print(f"mid : {mid}, mid_number : {mid_number}")
#     if mid_number == query:
#         if mid-1 >= 0 and cards[mid-1] == query:
#             return 'left'
#         else:
#             return 'found'
#     elif mid_number < query:
#         return 'left'
#     else:
#         return 'right'



# def locate_card(cards, query):
#     lo = 0
#     hi = len(cards) - 1
    
#     while lo <= hi:
#         print(f"lo : {lo}, hi : {hi}")
#         mid = (lo + hi) // 2
#         result = test_location(cards, query, mid)

#         if result == 'found':
#             return mid
#         elif result == 'left':
#             hi = mid - 1
#         elif result == 'right':
#             lo = mid + 1      
#     return -1 

# test = {
#     'input': { 
#         'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
#         'query': 7
#     },
#     'output': 3
# }
# tests = []
# tests.append(test)


# # query occurs in the middle
# tests.append({
#     'input' : {
#         'cards' : [13,11,10,7,4,3,1,0],
#         'query': 1
#     },
#     'output' : 6
# })

# # query is the first element
# tests.append({
#     'input': {
#         'cards' : [4,2,1,-1],
#         'query' : 4
#     },
#     'output' : 0
# })

# # querty is the last element
# tests.append({
#     'input': {
#         'cards' : [3, -1, 9, -127],
#         'query' : -127
#     },
#     'output': 3
# })

# # cards containes just one element
# tests.append({
#     'input' : {
#         'cards' : [6],
#         'query' : 6
#     },
#     'output' : 0
# })

# # card does not contain query
# tests.append({
#     "input" : {
#         'cards' : [9,7,5,2,-9],
#         "query" : 4
#     },
#     'output' : -1
# })

# # card is empty

# tests.append({
#     'input' : {
#         'cards' : [],
#         "query" : 1
#     },
#     'output' : -1
# })

# # numbers can repeat in cards
# tests.append({
#     'input': {
#         'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#         'query': 3
#     },
#     'output': 7
# })

# # query occurs multiple times
# tests.append({
#     'input': {
#         'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#         'query': 6
#     },
#     'output': 2
# })

# # print(tests)

# evaluate_test_cases(locate_card, tests)

# # card6 = tests[6]['input']['cards']
# # query6 = tests[6]['input']['query']

# # locate_card(card6, query6)

large_test = {
    'input': {
        'cards': list(range(1000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
    
} 

def test_location(cards, query, mid):
    mid_number = cards[mid]
    # print(f"mid : {mid}, mid_number : {mid_number}")
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'



def locate_card(cards, query):
    lo = 0
    hi = len(cards) - 1
    
    while lo <= hi:
        # print(f"lo : {lo}, hi : {hi}")
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1      
    return -1 

def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
print(f"Result: {result}\nPassed: {passed}\nExecution Time: {runtime} ms")

result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
print(f"\nResult: {result}\nPassed: {passed}\nExecution Time: {runtime} ms")
