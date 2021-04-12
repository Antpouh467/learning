# Подзадание №1: Написать программу, которая на любой вопрос отвечает "да"
# или "нет"

import random
from fuzzywuzzy import fuzz


questions = [                # Вопросы:
    'привет',
    'как дела',
    'пока не родила?',
    'нужно или нет',
    'гуляешь?',
    'зашел ли он',
    'дела как'
    ]
interrogative_word = {       # Вопросительные слова
    'ась',
    'аюшки',
    'где',
    'докуда',
    'зачем',
    'как-то',
    'каков',
    'какой',
    'куда',
    'насколько',
    'отколь',
    'откуда',
    'откудова',
    'отчего',
    'почему',
    'каков',
    'каковой',
    'который',
    'кто',
    'сколько',
    'чё',
    'чей',
    'что',
    'кем',
    'ком',
    'кому',
    'чему',
    'как',
    'ли',
    'неужели',
    'разве',
    'ужели',
    'ужель',
    }

with open('Homework_10_results.txt', 'w') as f:
    for question in questions:
        print('Запрос: ', question, file=f)
        q_word = set(question.split())
        while True:
            if q_word & interrogative_word or '?' in question:
                if random.getrandbits(1):
                    print('yes very much', file=f)
                else:
                    print('no.', file=f)
                break
            else:
                print('Это не вопрос', file=f)
                break

# Подзадание №2: Сделать так, чтобы она помнила отвеченные вопросы
# соответственно, при задании одного и того же вопроса должен быть ответ
# "такой вопрос уже был"
# Подзадание №3: Даже переформулированные
# *до известных пределов
# Добавляем строки вопросов в список строк

unique_questions = []
with open('Homework_10_results.txt', 'w') as f:
    for question in questions:
        print('Запрос: ', question, file=f)
        q_word = set(question.split())
        unique = 1    # переменная для учета уникальности вопроса
        for unique_question in unique_questions:
            # проверяем каждый вопрос на уникальность
            # рейтинг 90 - условный, особо не проверялся
            if fuzz.token_sort_ratio(unique_question, question) > 90:
                print('Такой вопрос уже был в такой форме: ',
                      unique_question, file=f)
                unique = 0    # помечаем неуникальность вопроса
                # т.о. если вопрос не уникальный, мы не будем его добавлять
                # в список уникальных вопросов
                # ^ (следующий if)
                # и также не будем проверять в нем наличие вопроса
                # ^ (следующий while)
                break
        if unique == 1:
            unique_questions.append(question)
        score = 0
        while unique == 1:
            if q_word & interrogative_word or '?' in question:
                if random.getrandbits(1):
                    print('yes very much', file=f)
                else:
                    print('no.', file=f)
                break
            else:
                print('Это не вопрос', file=f)
                break
