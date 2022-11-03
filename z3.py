# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
«как тебя зовут?» –> меня зовут Анатолий
import json
print('Simple bot for GB homework')
FILE_NAME = '2_z3_answers.json'
try: 
    f = open(FILE_NAME, 'r')
except IOError:
    print('file '+FILE_NAME+' does not exist!')
else:
    def answer(req, dict):
        from random import randint
        if req in dict['inputs']:
            if dict['inputs'][req] in dict['answers']:
                tmp = dict['answers'][dict['inputs'][req]]
                return tmp[randint(0,len(tmp)-1)]
        return dict["err"][0, len(dict["err"])]

    bot_answers = json.loads(f.read())
    req = ''
    print('Type "bye" for exit bot')
    while 1:
        req = input('write something to the bot: ').lower()
        print(answer(req, bot_answers))
        if req == "bye":
            break
