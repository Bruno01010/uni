calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return any(str_elem.lower() == string.lower() for str_elem in list_to_search) 
"""
Если хотя бы один элемент равен True, функция any() возвращает True, 
если все элементы равны False, функция возвращает False
"""

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)