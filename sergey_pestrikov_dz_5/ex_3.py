from itertools import zip_longest
#Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = zip_longest(tutors, klasses[:len(tutors)])
print(tuple(result))