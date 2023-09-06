# write your code here


#len for part 2 last one

person = {'name':'jana',
'age':14,
'hobbies':['gaming','drawing','math','piano']
}

print(person['name'])
print(person['age'])

person['age']= 17
person['country']=['finland']
print(person)
print(len(person))

person['hobbies'].append('bake')
print(person)

def check_hobby(person):
    if len(person['hobbies']) >=3 :
       print ('wow,you are amazing')
    else:
        print('add more hobbies')


check_hobby(person)