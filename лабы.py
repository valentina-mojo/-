x=18+(1/10)*(30+(33/44))+50+(55/88)/(9/10) #0 лаба 1
print(x)

sum(range(0,88888888)) #0 лаба 2

a=[3,4,56,100,2,2,3] #0 лаба 3
print(sum(a)/len(a))

исходная_строка="xxxxx"  #1 лаба 1
новая_строка=""
for a in исходная_строка:
    if a=="x":
        новая_строка+="y"
    else:
        новая_строка+=a
print(исходная_строка)
print(новая_строка)

числа=[1,2,3,4,5,3,6,5,4,15,4] #1 лаба 2
произведение=1
for x in числа:
    if (x//5==x/5) and(x//3==x/3):
        произведение*=x
print(произведение)

s = 'python' #1 лаба 3
s = s.replace('h', 't')
print(s)

student=['Ивушкина М.Г.', 1992,'студент-магистрант','Пермь'] #2 лаба 1
print(student)

student={ #2 лаба 2
    ('Ивушкина','Маргарита','Генриховна'):
    {'год рождения':1992,
     'курс':'студент-магистрант',
     'город':'Пермь'}}
print(student)

#2 лаба 3: списки можно скомбинировать вместе,
# словарь – это неупорядоченный набор пар ключ:значение,
# и ключи обязательно должны быть уникальными

student=['Ивушкина','Маргарита','Генриховна']#3 лаба 1
i = 0 
while i < len(student):
    print(i, student[i])
    i += 1

student={'Ивушкина','Маргарита','Генриховна'}#3 лаба 2
for key in student:
    print(key)

a = 1  #3 лаба 3
while a==1:
    b = input('Как тебя зовут?')
    print('Привет', b, ', Добро пожаловать')


import numpy #4 лаба 1
x=numpy.sum(range(0,100))
print(numpy.mean(x))

import numpy #4 лаба 2
n=int(input('Введите ваше число:'))
x=numpy.sum(range(0,n))
print(numpy.mean(x))

import numpy #4 лаба 3
x=numpy.random.randint(0,100)
print(numpy.mean(x))


def nomer(): #5 лаба 1
    nomer = [23, 24, 25, 26]
    f = 23
    print("Начинаю поиск")
    for element in users:
        if nomer == f:
            break
        else:
            print("нет в списке")
print("есть в списке")

def nomer(): #5 лаба 2
    nomer = {23, 24, 25, 26}
    f = 23
    print("Начинаю поиск")
    for element in users:
        if nomer == f:
            break
        else:
            print("нет в списке")
print("есть в списке")

def nomer(a,b): #5 лаба 3
    if a>b:
        return a
    else:
        return b
print(nomer(5,-9))


class Employee:  #6 лаба 1
    emp_count = 0  
    def __init__(self, name, height):  
        self.name = name  
        self.height = height 
    def display_employee(self):  
        print('Имя: {}. Рост: {}'.format(self.name, self.height))  
emp1 = Employee("Макс", 150)  
emp2 = Employee("Наташа", 160)  
emp1.display_employee()  
emp2.display_employee()  

class Employee:  #6 лаба 2
    emp_count = 0  
    def __init__(self, name, height):  
        self.name = name  
        self.height = height
emp1 = Employee("Макс", 150)  
emp2 = Employee("Наташа", 160)
for name in Employee:
    if name == Наташа:
        print("поиск")




числа=[1,2,3,4,5,3,6,5,4,15,4] #8 лаба (взято из 1)
произведение=1
for x in числа:
    if (x//5==x/5) and(x//3==x/3):
        произведение*=x
print(произведение)

числа=[1,2,3,4,5,3,6,5,4,15,4] #8 лаба (взято из 1)
произведение=1
for x in числа:
    if (x//5==x/5) and(x//3==x/3):
        произведение*=x
print(произведение)

numbers=[1,2,3,4,5,3,6,5,4,15,4] #8 лаба (взято из 1)
product=1
for x in numbers:
    if (x//5==x/5) and(x//3==x/3):
        product*=x
        print(product)

import re    #9 лаба
from sys import stderr
from random import randint
from itertools import product
from pprint import pprint
NOT_FOUND = '$'
MIN_WORD_SIMILARITY = 0
MIN_QUESTION_SIMILARITY = 0.5

class Brain():
    memory = dict()
    answers = ('да','нет')    

    def __fuzzy_key_search(self, words):
        answer = NOT_FOUND
        for key in self.memory:
            rez = []
            for w1, w2 in product(key, words):
                w = self.__compare(w1, w2)
                if w > MIN_WORD_SIMILARITY: 
                    rez += [ (w, w1, w2) ]
            pprint(rez, stderr)
            if sum((x[0] for x in rez)) / len(rez) > MIN_QUESTION_SIMILARITY:
                answer = self.memory[key]
        assert answer != NOT_FOUND    
        return answer
        
    def __compare(self, s1, s2):
        count = 0  
        for ngram in ( s1[i:i+3] for i in range(len(s1)-1) ):
            count += s2.count(ngram)
        return count / max(len(s1), len(s2))
    
    def think(self, question):
        words = tuple(re.sub(r'[!;:?,.-]',' ', question).split())
        try: 
            return "Я уже отвечала, ответ был %s." % self.memory[words] 
        except KeyError: 
            try: 
                answer = self.__fuzzy_key_search(words)
