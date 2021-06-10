students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(lst):
    for i in range(len(lst)):
        print(lst[i]['first_name'])

def iterateDictionary3(lst):
    for i in range(len(lst)):
        print(lst[i]['last_name'])

iterateDictionary2(students)

iterateDictionary3(students)