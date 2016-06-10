import random
import sys
import os


# comment

'''
Multiline
'''
print("Hello World")
print("Learning Python")

name = "Emirhan"
print("Hello " + name)


'''
Operators:

** : power, //: integer division solution
'''

quote = "\"The blues they send to meet me won't defeat me,"

multi_line_quote = '''It won't be long till happiness steps up to greet me" '''

print("%s %s %s" % ('I like the lyrics', quote, multi_line_quote))

print('\n' * 2)

print("I don't want ", end="")
print("new line")


# Lists
grocery_list = ['Juice', 'Tomatoes', 'Bananas', 'Patatoes']

print(grocery_list[1:3]) # Give items from 1st to 3rd

other_events = ['Wash car', "Pick up kids", "Cash Check"]

to_do_list = [other_events,grocery_list] # List inside of list
print(to_do_list)

print((to_do_list[1][1])) # Second item from both lists

grocery_list.append('Onions') # Insert item in last
print(to_do_list)

grocery_list.insert(1, "Pickle") # Insert in specific index

grocery_list.remove("Pickle")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]
print(to_do_list)


to_do_list2 = other_events + grocery_list
print(len(to_do_list2))

print('\n' * 3)


# Tuples
pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

'''len(tuple) min(tuple) max(tuple) '''



# Dictionaries

super_villians = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Mirror Master': 'Sam Scudder',
                  'Pied Piper': 'Thomas Petterson'}

print(super_villians['Captain Cold'])
del  super_villians['Fiddler']

super_villians['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villians))
print(super_villians.get('Pied Piper'))
print(super_villians.keys())
print(super_villians.values())


# If Else conditions and operations
age = 30

if age > 18:
    print('You\'re old enough to drive')
else :
    print('You\'re not old enough to drive')


if age >= 21 :
    print('You are old enough')
elif age >= 18:
    print('You are old enough to drive a car')
else :
    print("You are not old enough")



if((age >= 1) and (age <= 18)) :
    print("You get a birthday")
elif (age == 21) or (age >= 65) :
    print("You get a birthday")
elif not(age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday party yay!")




# Loops
for x in range(0,10):
    print(x, " ", end="")

print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Patatoes', 'Bananas']

for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print(x)


num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in  range(0,3):
        print(num_list[x][y])


random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue
    i += 1



#Functions
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

string = print(addNumber(30,70))


print('What\'s your name')

#name = sys.stdin.readline()
#print('Hello', name)

long_string = "I'm never gonna stop the rain by complaining"

print(long_string[0:4])

print(long_string[-11:])

print(long_string[:-11])

print(long_string[:4] + "never gonna")

print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))

print('\n')

print(long_string.capitalize())
print(long_string.find('complaining'))
print((long_string.isalnum()))
print(len((long_string)))
print(long_string.replace('complaining', "crying"))

quote_list = long_string.split(" ")
print(quote_list)



#Files
test_file = open("test.txt", "wb") #to write: wb, to read and append: ab+

print(test_file.mode)
print(test_file.name)

test_file.write(bytes('Writing to the file\n', 'UTF-8'))
#test_file.closed()

test_file = open("test.txt", "r+")

test_in_file = test_file.read()
print(test_in_file)

#os.remove("test.txt")



#Objects
class Animal:
    __name = ""  # __ means private
    __height = 0
    __weight = 0
    __sound = 0

    #constructor
    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound


    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {}".format(self.__name,
                                                              self.__height,
                                                              self.__weight,
                                                              self.__sound)

cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())

class Dog(Animal):
    __owner = ""

    def __init__(self,name,height,weight,sound,owner):
        self.__owner = owner
        super(Dog,self).__init__(name,height,weight,sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {} His owner is {} ".format(self.get_name(),
                                                              self.get_height(),
                                                              self.get_weight(),
                                                              self.get_sound(),
                                                              self.__owner)


    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)


whiteFang = Dog("White Fang", 53, 27, "Ruff", "Emirhan")
print(whiteFang.toString())


class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(whiteFang)

whiteFang.multiple_sounds(3)




#351

L = [1,2,3,4,5]
L.index(1) #gives the index of element



'string'.split('i')


Array = [[1,2,3],[10,20,30]]

[print(i) for i in Array]

if("a" == "a"):
        print True
elif("a" == "b"):
        print False






















